#!/usr/bin/env python3
"""Harvest, probe, generate, and verify the no-key public API catalog."""
from __future__ import annotations

import html
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "apis.json")
SEED = os.path.join(ROOT, "catalog.json")
KNOWN = os.path.join(ROOT, "scripts", "known_endpoints.json")

CAT_MAP = {
    "exchange": "Currency Exchange",
    "weather": "Weather",
    "geo": "Geocoding",
    "testdata": "Test Data",
    "language": "Dictionaries",
    "news": "News",
    "crypto": "Cryptocurrency",
    "time": "Calendar",
    "science": "Science & Math",
    "entertainment": "Entertainment",
    "developer": "Development",
    "Anti-Malware": "Security",
    "Patent": "Government",
    "Social": "Development",
    "URL Shorteners": "Development",
}


def norm_cat(name: str) -> str:
    return CAT_MAP.get(name, name)
SKILL = os.path.join(ROOT, "SKILL.md")
README = os.path.join(ROOT, "README.md")
REFS = os.path.join(ROOT, "references")
UA = "agent-public-apis-verify/1.0 (+https://github.com/hfcorriez/agent-public-apis)"
TIMEOUT = 10
WORKERS = 20
MIN_LIVE = 400

SRC_PUBLIC = "https://raw.githubusercontent.com/public-apis/public-apis/master/README.md"
SRC_MARCEL = "https://raw.githubusercontent.com/marcelscruz/public-apis/main/db/resources.json"

SKIP_HOST_PARTS = (
    "github.com",
    "gitlab.com",
    "bitbucket.org",
    "postman.com",
    "god.gw.postman.com",
    "twitter.com",
    "x.com",
    "youtube.com",
    "linkedin.com",
    "facebook.com",
    "medium.com",
    "npmjs.com",
    "pypi.org",
)

KEY_HINTS = (
    "apikey=",
    "api_key=",
    "access_key=",
    "access-key=",
    "token=",
    "your_api_key",
    "your-api-key",
    "yourapikey",
    "api=your",
)
PLACEHOLDER_RE = re.compile(
    r"YOUR_API_KEY|your_api_key|<address|<easting|<northing|\{api[_-]?key\}|\{token\}|<[^/>]+>",
    re.I,
)
SKIP_PATH_PARTS = (
    "manifest.json",
    "/favicon",
    "/static/img/",
    "apple-touch-icon",
    "robots.txt",
    "/widgets/embed-image",
    "/branding/",
)
AUTH_ERR = ("api key", "access key", "apikey required", "missing_access_key", "unauthorized", "invalid key")
STATUS_ERR = ("error", "fail", "failed", "invalid_request", "invalid request", "page not found 404")


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:60] or "api"


def host_of(url: str) -> str:
    try:
        return urlparse(url).netloc.lower()
    except Exception:
        return ""


def skip_host(url: str) -> bool:
    h = host_of(url)
    if h == "api.github.com":
        return False
    for p in SKIP_HOST_PARTS:
        if h == p or h.endswith("." + p):
            return True
    return False


def skip_path(url: str) -> bool:
    low = url.lower()
    return any(p in low for p in SKIP_PATH_PARTS)


def clean_url(url: str) -> str:
    # Only named entities that appear in README tables. Do not html.unescape
    # the whole string — `&current_weather` would become `¤t_weather`.
    url = (url or "").strip()
    url = url.replace("&amp;", "&").replace("&quot;", "").replace("&lt;", "<").replace("&gt;", ">")
    if url.endswith("&quot"):
        url = url[:-5]
    return url.rstrip("\"'").strip()


def looks_like_key_url(url: str) -> bool:
    low = (url or "").lower()
    if any(h in low for h in KEY_HINTS):
        return True
    if PLACEHOLDER_RE.search(url or ""):
        return True
    if re.search(r"[?&]api=", url or "", re.I) and not re.search(r"[?&]api=v\d", url or "", re.I):
        return True
    return False


def usable_url(url: str) -> bool:
    if not url.startswith("https://"):
        return False
    if skip_host(url) or skip_path(url) or looks_like_key_url(url):
        return False
    return True


def parse_public_apis(md: str) -> list[dict]:
    category = "misc"
    out = []
    for line in md.splitlines():
        if line.startswith("### "):
            category = line[4:].strip()
            continue
        m = re.match(
            r"\| \[([^\]]+)\]\(([^)]+)\) \|([^|]*)\|([^|]*)\|([^|]*)\|",
            line,
        )
        if not m:
            continue
        name, url, desc, auth, https = [x.strip() for x in m.groups()]
        auth_n = auth.strip("`").lower()
        if auth_n not in ("no", ""):
            continue
        if https.lower() != "yes":
            continue
        url = clean_url(url)
        if not usable_url(url):
            continue
        out.append(
            {
                "name": name,
                "url": url,
                "description": desc.strip(),
                "category": norm_cat(category),
                "source": "public-apis",
            }
        )
    return out


def parse_marcel(raw: str) -> list[dict]:
    data = json.loads(raw)
    out = []
    for e in data.get("entries", []):
        auth = (e.get("Auth") or "").strip().lower()
        if auth not in ("", "no"):
            continue
        url = clean_url(e.get("Link") or "")
        if not usable_url(url):
            continue
        out.append(
            {
                "name": e.get("API") or "unnamed",
                "url": url,
                "description": (e.get("Description") or "").strip(),
                "category": norm_cat(e.get("Category") or "misc"),
                "source": "marcelscruz",
            }
        )
    return out


def load_seed() -> list[dict]:
    if not os.path.isfile(SEED):
        return []
    data = json.load(open(SEED))
    out = []
    for api in data.get("apis", []):
        out.append(
            {
                "name": api["name"],
                "url": api["url"],
                "description": api.get("name", ""),
                "category": norm_cat(api.get("category") or "misc"),
                "source": "seed",
                "id": api["id"],
                "json_path": api.get("json_path") or "",
                "fallback": api.get("fallback") or "",
                "preferred": True,
            }
        )
    return out


def load_known() -> list[dict]:
    if not os.path.isfile(KNOWN):
        return []
    out = []
    for api in json.load(open(KNOWN)):
        out.append(
            {
                "name": api.get("name") or api["id"],
                "url": api["url"],
                "description": "",
                "category": norm_cat(api.get("category") or "misc"),
                "source": "known-endpoint",
                "id": api["id"],
                "json_path": api.get("json_path") or "",
                "fallback": "",
                "preferred": False,
            }
        )
    return out


def guess_urls(listed: str) -> list[str]:
    listed = clean_url(listed)
    urls = []
    if usable_url(listed):
        urls.append(listed.rstrip("/"))
    parsed = urlparse(listed)
    if skip_host(listed) or not parsed.scheme.startswith("https"):
        return urls
    origin = f"{parsed.scheme}://{parsed.netloc}"
    path = parsed.path.lower()
    extras = []
    if any(x in path for x in ("/doc", "/docs", "/documentation", "/about")):
        extras.extend([origin, origin + "/api", origin + "/v1", origin + "/api/v1"])
    elif path in ("", "/"):
        if "api" in parsed.netloc.lower():
            extras.extend([origin + "/api", origin + "/v1", origin + "/v2"])
    for u in extras:
        if u not in urls and usable_url(u):
            urls.append(u)
    return urls[:3]


def dedupe_candidates(items: list[dict]) -> list[dict]:
    by_key: dict[str, dict] = {}
    for it in items:
        key = (it.get("id") or "") + "|" + host_of(it["url"]) + "|" + slug(it["name"])
        prev = by_key.get(key)
        if prev is None or it.get("preferred") or (prev.get("source") != "seed" and it.get("source") == "seed"):
            if prev and prev.get("preferred"):
                continue
            by_key[key] = it
    return list(by_key.values())


def curl_one(url: str) -> dict:
    body_path = None
    try:
        import tempfile

        fd, body_path = tempfile.mkstemp(prefix="agent-public-apis-")
        os.close(fd)
        proc = subprocess.run(
            [
                "curl",
                "-sS",
                "-L",
                "--max-time",
                str(TIMEOUT),
                "-o",
                body_path,
                "-D",
                "-",
                "-w",
                "\n__HTTP__%{http_code}",
                "-H",
                f"User-Agent: {UA}",
                "-H",
                "Accept: application/json, application/xml, text/plain, */*",
                url,
            ],
            capture_output=True,
            text=True,
            timeout=TIMEOUT + 5,
        )
        mixed = proc.stdout or ""
        http = "000"
        headers = mixed
        if "__HTTP__" in mixed:
            headers, http = mixed.rsplit("__HTTP__", 1)
            http = http.strip() or "000"
        ctype = ""
        rate = "unknown"
        for line in headers.splitlines():
            low = line.lower()
            if low.startswith("content-type:"):
                ctype = line.split(":", 1)[1].strip()
            if low.startswith("x-ratelimit-limit:"):
                rate = "x-ratelimit-limit " + line.split(":", 1)[1].strip()
            if low.startswith("retry-after:"):
                rate = "retry-after " + line.split(":", 1)[1].strip()
        try:
            with open(body_path, "rb") as f:
                raw = f.read(200_000)
        except OSError:
            raw = b""
        return {
            "url": url,
            "http": http,
            "ctype": ctype,
            "rate": rate,
            "body": raw,
            "err": (proc.stderr or "").strip()[:120],
        }
    except Exception as exc:
        return {"url": url, "http": "000", "ctype": "", "rate": "unknown", "body": b"", "err": str(exc)[:120]}
    finally:
        if body_path:
            try:
                os.unlink(body_path)
            except OSError:
                pass


def classify_body(body: bytes, ctype: str) -> tuple[bool, str, list[str]]:
    ct = (ctype or "").lower()
    if "text/html" in ct:
        return False, "html", []
    head = body.lstrip()[:300].lower()
    if head.startswith(b"<!doctype") or head.startswith(b"<html") or head.startswith(b"<head"):
        return False, "html", []
    if not body or len(body.strip()) < 2:
        return False, "empty", []
    text = None
    try:
        text = body.decode("utf-8", "replace")
    except Exception:
        text = ""
    stripped = text.lstrip()
    if stripped[:1] in "{[":
        try:
            data = json.loads(text)
        except Exception:
            return False, "bad-json", []
        if isinstance(data, dict):
            keys = list(data.keys())[:8]
            blob = json.dumps(data).lower()[:500]
            if any(h in blob for h in AUTH_ERR) and any(
                k.lower() in ("error", "errors", "message", "success") for k in keys
            ):
                if data.get("success") is False or "error" in data or "errors" in data:
                    return False, "auth-error", keys
            if data.get("success") is False and not any(k for k in keys if k not in ("success", "error", "errors", "message")):
                return False, "success-false", keys
            st = data.get("status")
            if isinstance(st, str) and (st.lower() in STATUS_ERR or "not found" in st.lower()):
                return False, "error-body", keys
            err_val = data.get("error")
            if err_val and err_val is not False:
                if isinstance(err_val, str) and err_val.lower() not in ("", "ok", "false", "0"):
                    return False, "error-body", keys
                if isinstance(err_val, (dict, list)):
                    return False, "error-body", keys
            kind = "openapi-spec" if ("openapi" in keys or "swagger" in keys) else "json"
            return True, kind, keys
        if isinstance(data, list):
            if not data:
                return True, "json-list", []
            first = data[0]
            keys = list(first.keys())[:8] if isinstance(first, dict) else []
            return True, "json-list", keys
    if "json" in ct:
        return False, "claimed-json", []
    if "xml" in ct or stripped.startswith("<?xml") or stripped.startswith("<"):
        if "html" in ct:
            return False, "html", []
        return True, "xml", []
    if ct.startswith("image/") or ct.startswith("audio/") or ct.startswith("video/"):
        return True, "binary", []
    if "text/plain" in ct or "text/csv" in ct:
        return True, "text", []
    # unknown non-html with a body: reject, too likely a website
    return False, "other", []


def probe_candidate(cand: dict) -> dict | None:
    if cand.get("preferred") or cand.get("source") in ("seed", "known-endpoint"):
        urls = [cand["url"]]
    else:
        urls = guess_urls(cand["url"])
    if not urls:
        return None
    last_reason = "no-url"
    for url in urls:
        res = curl_one(url)
        ok, kind, keys = classify_body(res["body"], res["ctype"])
        if res["http"] == "200" and ok:
            entry = {
                "id": cand.get("id") or slug(cand["name"]),
                "name": cand["name"],
                "category": cand["category"],
                "description": cand.get("description") or "",
                "url": url,
                "source": cand.get("source") or "harvest",
                "json_path": cand.get("json_path") or (keys[0] if keys else ""),
                "fields": keys,
                "kind": kind,
                "spec_only": kind == "openapi-spec",
                "rate_limit": res["rate"],
                "preferred": bool(cand.get("preferred")),
                "fallback": cand.get("fallback") or "",
            }
            return entry
        last_reason = f"{res['http']}/{kind}"
    cand["_fail"] = last_reason
    return None


def unique_ids(entries: list[dict]) -> list[dict]:
    seen: dict[str, int] = {}
    out = []
    for e in entries:
        base = e["id"]
        n = seen.get(base, 0)
        if n:
            e = dict(e)
            e["id"] = f"{base}-{n+1}"
        seen[base] = n + 1
        out.append(e)
    return out


def assign_fallbacks(entries: list[dict]) -> None:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_cat[e["category"]].append(e)
    for group in by_cat.values():
        ids = [e["id"] for e in group]
        for i, e in enumerate(group):
            if e.get("fallback") and e["fallback"] in ids:
                continue
            e["fallback"] = ids[(i + 1) % len(ids)] if len(ids) > 1 else ""


def harvest() -> list[dict]:
    print("fetching sources...", flush=True)
    md = fetch(SRC_PUBLIC)
    marcel = fetch(SRC_MARCEL)
    pub = parse_public_apis(md)
    mar = parse_marcel(marcel)
    seed = load_seed()
    known = load_known()
    print(f"  public-apis no-auth https: {len(pub)}")
    print(f"  marcelscruz no-auth https: {len(mar)}")
    print(f"  seed: {len(seed)}")
    print(f"  known endpoints: {len(known)}")
    merged = dedupe_candidates(seed + known + pub + mar)
    print(f"  candidates after dedupe: {len(merged)}")
    return merged


def probe_all(cands: list[dict], label: str) -> list[dict]:
    live = []
    total = len(cands)
    done = 0
    t0 = time.time()
    print(f"probing {total} {label} (workers={WORKERS}, timeout={TIMEOUT}s)...", flush=True)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futs = {pool.submit(probe_candidate, c): c for c in cands}
        for fut in as_completed(futs):
            done += 1
            try:
                entry = fut.result()
            except Exception:
                entry = None
            if entry:
                live.append(entry)
            if done % 50 == 0 or done == total:
                print(f"  {done}/{total}  live {len(live)}  {time.time()-t0:.0f}s", flush=True)
    return live


def write_apis(entries: list[dict]) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for e in entries:
        e["verified_at"] = now
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    payload = {
        "version": 2,
        "generated_at": now,
        "user_agent": UA,
        "count": len(entries),
        "apis": entries,
    }
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")


def cat_slug(name: str) -> str:
    return slug(name)


def gh_anchor(text: str) -> str:
    s = text.lower()
    s = re.sub(r"[^a-z0-9 -]", "", s)
    s = s.replace(" ", "-").strip("-")
    return s


def md_cell(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def generate_docs(entries: list[dict]) -> None:
    os.makedirs(REFS, exist_ok=True)
    for name in os.listdir(REFS):
        if name.endswith(".md"):
            os.unlink(os.path.join(REFS, name))

    by_cat: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_cat[e["category"]].append(e)

    ref_files: dict[str, str] = {}
    for cat, group in sorted(by_cat.items(), key=lambda kv: kv[0].lower()):
        group = sorted(group, key=lambda e: (not e.get("preferred"), e["name"].lower()))
        chunks: list[list[dict]] = []
        current: list[dict] = []
        lines_used = 3
        for e in group:
            need = 5
            if lines_used + need > 490:
                chunks.append(current)
                current = []
                lines_used = 3
            current.append(e)
            lines_used += need
        if current:
            chunks.append(current)
        base = cat_slug(cat)
        for i, chunk in enumerate(chunks):
            fname = f"{base}.md" if len(chunks) == 1 else f"{base}-{i+1}.md"
            path = os.path.join(REFS, fname)
            if i == 0:
                ref_files[cat] = fname
            lines = [f"# {cat}", ""]
            if len(chunks) > 1:
                lines.append(f"Part {i+1}/{len(chunks)}.")
                lines.append("")
            for e in chunk:
                fields = ", ".join(e.get("fields") or []) or e.get("json_path") or e.get("kind") or "—"
                role = " Role: spec-only." if e.get("spec_only") or e.get("kind") == "openapi-spec" else ""
                lines.append(f"## {e['name']}")
                lines.append(f"`GET {e['url']}`")
                fb = e.get("fallback") or "—"
                lines.append(f"Fields: {fields}. Limit: {e.get('rate_limit') or 'unknown'}. Fallback: `{fb}`.{role}")
                lines.append("")
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines).rstrip() + "\n")

    # SKILL.md: usage + index + top picks from seed/preferred
    recs_by_cat: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        if e.get("preferred"):
            recs_by_cat[e["category"]].append(e)
    for cat, group in by_cat.items():
        if cat not in recs_by_cat:
            recs_by_cat[cat] = group[:3]

    skill = [
        "---",
        "name: agent-public-apis",
        "description: Call verified no-key public APIs. Use when the user needs a free HTTPS API with no signup — weather, geo, news, crypto, dictionaries, test data, or any category in the index.",
        "---",
        "",
        "# agent-public-apis",
        "",
        "Verified no-key HTTPS APIs. Catalog is `data/apis.json`. Full entries live in `references/`. Re-check with `./verify.sh`.",
        "",
        "```bash",
        'curl -sS -L -H "User-Agent: agent-public-apis/1.0" -H "Accept: application/json" "<url>"',
        "```",
        "",
        "Rules: no key, HTTPS only, send a User-Agent, one request then cache, use `fallback` if the primary dies.",
        "",
        "## Index",
        "",
    ]
    for cat in sorted(by_cat, key=lambda s: s.lower()):
        n = len(by_cat[cat])
        fname = ref_files[cat]
        skill.append(f"- [{cat}](references/{fname}) ({n})")
    skill.append("")
    skill.append("## Recommended")
    skill.append("")
    # keep recommended section short: preferred seed categories only
    preferred_cats = [c for c, g in recs_by_cat.items() if any(e.get("preferred") for e in g)]
    for cat in sorted(preferred_cats, key=lambda s: s.lower()):
        picks = [e for e in recs_by_cat[cat] if e.get("preferred")][:3]
        if not picks:
            continue
        skill.append(f"### {cat}")
        for e in picks:
            fields = ", ".join((e.get("fields") or [])[:4]) or e.get("json_path") or ""
            skill.append(f"- **{e['name']}** `{e['url']}` — {fields}")
        skill.append("")
    skill.append("## Refresh")
    skill.append("")
    skill.append("```bash")
    skill.append("./verify.sh           # re-probe data/apis.json, require 100% live and ≥400")
    skill.append("./verify.sh --refresh # re-harvest sources, probe, regenerate docs")
    skill.append("```")
    skill.append("")
    text = "\n".join(skill)
    lines = text.count("\n") + 1
    if lines > 250:
        raise SystemExit(f"SKILL.md would be {lines} lines, cap is 250")
    with open(SKILL, "w", encoding="utf-8") as f:
        f.write(text if text.endswith("\n") else text + "\n")
    write_readme(entries, by_cat)
    print(f"wrote SKILL.md ({lines} lines), README.md, {len(os.listdir(REFS))} reference files")


def write_readme(entries: list[dict], by_cat: dict[str, list[dict]]) -> None:
    cats = sorted(by_cat, key=lambda s: s.lower())
    spec_n = sum(1 for e in entries if e.get("spec_only") or e.get("kind") == "openapi-spec")
    lines = [
        "# agent-public-apis",
        "",
        f"Public APIs, agent-ready — {len(entries)} verified, no keys, no signup.",
        "",
        "A distilled, machine-verified edition of [public-apis](https://github.com/public-apis/public-apis): every entry is probed live over HTTPS, requires no API key and no registration, and ships in a format agents can use directly as a skill.",
        "",
        "Every catalog entry is no-key, HTTPS-only, and live-verified (`verify.sh`). Spec-only rows are marked in Notes — the probe hit an OpenAPI/docs URL, not a live data endpoint.",
        "",
        "- `SKILL.md` — index + recommended curls (drop it into your agent as a skill)",
        "- `data/apis.json` — full verified catalog (name, endpoint, category, example, response fields, rate limits, verified-at)",
        "- `references/` — per-category entries, loaded on demand",
        "- `verify.sh` — re-probe the whole catalog",
        "",
        "```bash",
        "./verify.sh           # all catalog entries must be live",
        "./verify.sh --refresh # re-harvest upstream lists and rebuild",
        "```",
        "",
        "Rules baked into every entry: no key, HTTPS only, send a User-Agent, one request then cache, use `fallback` if the primary dies.",
        "",
        f"## Catalog ({len(cats)} categories, {len(entries)} APIs",
    ]
    if spec_n:
        lines[-1] += f", {spec_n} spec-only"
    lines[-1] += ")"
    lines.append("")
    for cat in cats:
        n = len(by_cat[cat])
        lines.append(f"- [{cat}](#{gh_anchor(cat)}) ({n})")
    lines.append("")
    for cat in cats:
        group = sorted(by_cat[cat], key=lambda e: e["name"].lower())
        lines.append(f"## {cat}")
        lines.append("")
        lines.append("| Name | Purpose | Endpoint | Notes |")
        lines.append("| --- | --- | --- | --- |")
        for e in group:
            note = "spec-only" if e.get("spec_only") or e.get("kind") == "openapi-spec" else ""
            lines.append(
                f"| {md_cell(e['name'])} | {md_cell(e.get('description') or '')} | `{md_cell(e['url'])}` | {note} |"
            )
        lines.append("")
    lines.extend(
        [
            "## Sources",
            "",
            "Distilled from [public-apis/public-apis](https://github.com/public-apis/public-apis) and [marcelscruz/public-apis](https://github.com/marcelscruz/public-apis), with OpenAPI structure hints from [apis.guru](https://apis.guru). Only entries that pass live verification are included.",
            "",
            "## License",
            "",
            "MIT",
            "",
        ]
    )
    text = "\n".join(lines)
    with open(README, "w", encoding="utf-8") as f:
        f.write(text if text.endswith("\n") else text + "\n")


def cmd_docs() -> int:
    entries = load_catalog()
    generate_docs(entries)
    return 0


def cmd_refresh() -> int:
    cands = harvest()
    live = probe_all(cands, "candidates")
    live = unique_ids(live)
    assign_fallbacks(live)
    live.sort(key=lambda e: (e["category"].lower(), not e.get("preferred"), e["name"].lower()))
    write_apis(live)
    generate_docs(live)
    print(f"first pass live {len(live)} (min {MIN_LIVE})")
    if len(live) < MIN_LIVE:
        print("running enrich pass...", flush=True)
        enrich = os.path.join(ROOT, "scripts", "enrich.py")
        rc = subprocess.call([sys.executable, enrich])
        return rc
    return 0


def walk_path(data, path: str):
    cur = data
    for part in path.split("."):
        if part == "":
            continue
        if isinstance(cur, list):
            if part.isdigit():
                cur = cur[int(part)]
            elif cur and isinstance(cur[0], dict) and part in cur[0]:
                cur = cur[0][part]
            else:
                raise KeyError(part)
        elif isinstance(cur, dict):
            if part not in cur:
                raise KeyError(part)
            cur = cur[part]
        else:
            raise TypeError(type(cur).__name__)
    return cur


def load_catalog() -> list[dict]:
    data = json.load(open(DATA))
    return data["apis"]


def _verify_once(e: dict) -> tuple[str, dict]:
    res = curl_one(e["url"])
    ok, kind, keys = classify_body(res["body"], res["ctype"])
    status = "OK"
    detail = kind
    if res["http"] != "200":
        status = "FAIL"
        detail = f"http {res['http']} {res.get('err') or ''}".strip()
    elif not ok:
        status = "FAIL"
        detail = kind
    elif e.get("json_path") and kind.startswith("json"):
        try:
            data = json.loads(res["body"].decode("utf-8", "replace"))
            cur = walk_path(data, e["json_path"])
            if cur is None or cur is False or cur == "":
                status = "FAIL"
                detail = "empty or false value"
            else:
                detail = f"path {e['json_path']}"
        except Exception as exc:
            status = "FAIL"
            detail = f"path {e['json_path']}: {exc}"
    return status, {"id": e["id"], "http": res["http"], "detail": detail, "category": e.get("category") or ""}


def verify_one(e: dict) -> tuple[str, dict]:
    status, row = _verify_once(e)
    if status != "OK" and row["http"] in ("000", "429", "503"):
        status, row = _verify_once(e)
    return status, row


def cmd_verify() -> int:
    if not os.path.isfile(DATA):
        print("missing data/apis.json — run ./verify.sh --refresh", file=sys.stderr)
        return 2
    apis = load_catalog()
    print(f"{'STATUS':<6} {'ID':<28} {'CATEGORY':<22} {'HTTP':>4}  DETAIL")
    print("-" * 90)
    ok = fail = 0
    fails = []
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futs = [pool.submit(verify_one, e) for e in apis]
        for e, fut in zip(apis, futs):
            status, row = fut.result()
            if status == "OK":
                ok += 1
            else:
                fail += 1
                fails.append(row)
            print(f"{status:<6} {row['id']:<28} {row['category']:<22} {row['http']:>4}  {row['detail']}")
    print("-" * 90)
    print(f"checked {len(apis)}  ok {ok}  fail {fail}")
    if fail or len(apis) < MIN_LIVE:
        print("FAILED")
        for row in fails:
            print(f"  {row['id']}  {row['http']}  {row['detail']}")
        if len(apis) < MIN_LIVE:
            print(f"  count {len(apis)} < {MIN_LIVE}")
        return 1
    print("ALL OK")
    return 0


def main(argv: list[str]) -> int:
    if argv and argv[0] == "refresh":
        return cmd_refresh()
    if argv and argv[0] == "docs":
        return cmd_docs()
    if argv and argv[0] in ("verify", ""):
        return cmd_verify()
    print("usage: pipeline.py verify|refresh|docs", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
