#!/usr/bin/env python3
"""Second-pass URL discovery for candidates that failed the first probe."""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pipeline import (  # noqa: E402
    DATA,
    assign_fallbacks,
    classify_body,
    curl_one,
    dedupe_candidates,
    generate_docs,
    harvest,
    host_of,
    load_catalog,
    looks_like_key_url,
    skip_host,
    slug,
    unique_ids,
    write_apis,
)

WORKERS = 24
PATHS = ("/api", "/api/v1", "/v1", "/openapi.json", "/swagger.json", "/health")

URL_RE = re.compile(r"https://[a-zA-Z0-9._~:/?#\[\]@!$&'()*+,;=%-]+")
CURL_RE = re.compile(r"curl[^\n]*?(https://[^\s'\"\\]+)")


def extract_urls(base: str, body: bytes) -> list[str]:
    try:
        text = body.decode("utf-8", "replace")
    except Exception:
        return []
    found = []
    for m in URL_RE.findall(text):
        found.append(m.rstrip(").,;\"'"))
    for m in CURL_RE.findall(text):
        found.append(m.rstrip(").,;\"'"))
    # relative api links
    for rel in re.findall(r'href=["\']([^"\']+)["\']', text, re.I):
        if rel.startswith("/") and any(x in rel.lower() for x in ("/api", "/v1", "/v2", ".json")):
            found.append(urljoin(base, rel))
    out = []
    seen = set()
    base_host = host_of(base)
    for u in found:
        if not u.startswith("https://") or looks_like_key_url(u) or skip_host(u):
            continue
        if u in seen:
            continue
        low = u.lower()
        same = host_of(u) == base_host or host_of(u).endswith("." + base_host) or base_host.endswith("." + host_of(u))
        apiish = any(x in low for x in ("/api", "/v1", "/v2", "/v3", ".json", "openapi", "swagger", "graphql"))
        if same and apiish:
            seen.add(u)
            out.append(u.split("#")[0])
        elif apiish and "api." in host_of(u):
            seen.add(u)
            out.append(u.split("#")[0])
        if len(out) >= 6:
            break
    return out


def path_guesses(listed: str) -> list[str]:
    p = urlparse(listed)
    if p.scheme != "https" or skip_host(listed):
        return []
    origin = f"{p.scheme}://{p.netloc}"
    urls = []
    for path in PATHS:
        urls.append(origin + path)
    return urls


def discover(cand: dict) -> list[str]:
    listed = cand["url"]
    urls = []
    if listed.startswith("https://") and not skip_host(listed) and not looks_like_key_url(listed):
        res = curl_one(listed)
        ok, kind, _ = classify_body(res["body"], res["ctype"])
        if res["http"] == "200" and ok:
            return [listed]
        if res["http"] == "200" and kind == "html":
            urls.extend(extract_urls(listed, res["body"]))
    host = host_of(listed)
    if "api" in host or not urls:
        urls.extend(path_guesses(listed))
    seen = set()
    out = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out[:5]


def probe_urls(cand: dict, urls: list[str]) -> dict | None:
    for url in urls:
        res = curl_one(url)
        ok, kind, keys = classify_body(res["body"], res["ctype"])
        if res["http"] == "200" and ok:
            return {
                "id": cand.get("id") or slug(cand["name"]),
                "name": cand["name"],
                "category": cand["category"],
                "description": cand.get("description") or "",
                "url": url,
                "source": cand.get("source") or "enrich",
                "json_path": cand.get("json_path") or (keys[0] if keys else ""),
                "fields": keys,
                "kind": kind,
                "rate_limit": res["rate"],
                "preferred": bool(cand.get("preferred")),
                "fallback": cand.get("fallback") or "",
            }
    return None


def main() -> int:
    existing = []
    live_hosts = set()
    live_ids = set()
    if os.path.isfile(DATA):
        existing = load_catalog()
        live_hosts = {host_of(e["url"]) for e in existing}
        live_ids = {e["id"] for e in existing}
        print(f"existing live {len(existing)}")
    cands = harvest()
    todo = []
    for c in cands:
        if c.get("id") in live_ids:
            continue
        if host_of(c["url"]) in live_hosts and c.get("source") != "seed":
            # still try different names on same host? skip to reduce noise
            continue
        if skip_host(c["url"]):
            continue
        todo.append(c)
    print(f"enrich todo {len(todo)}")

    found = []
    done = 0

    def work(c):
        urls = discover(c)
        return probe_urls(c, urls)

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futs = {pool.submit(work, c): c for c in todo}
        for fut in as_completed(futs):
            done += 1
            try:
                entry = fut.result()
            except Exception:
                entry = None
            if entry:
                found.append(entry)
            if done % 40 == 0 or done == len(todo):
                print(f"  {done}/{len(todo)}  new {len(found)}", flush=True)

    merged = unique_ids(existing + found)
    assign_fallbacks(merged)
    merged.sort(key=lambda e: (e["category"].lower(), not e.get("preferred"), e["name"].lower()))
    write_apis(merged)
    generate_docs(merged)
    print(f"total live {len(merged)}")
    return 0 if len(merged) >= 400 else 1


if __name__ == "__main__":
    sys.exit(main())
