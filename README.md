# agent-public-apis

Public APIs, agent-ready — 411 verified, no keys, no signup.

A distilled, machine-verified edition of [public-apis](https://github.com/public-apis/public-apis): every entry is probed live over HTTPS, requires no API key and no registration, and ships in a format agents can use directly as a skill.

- `SKILL.md` — index + recommended curls (drop it into your agent as a skill)
- `data/apis.json` — full verified catalog (name, endpoint, category, example, response fields, rate limits, verified-at)
- `references/` — per-category entries, loaded on demand
- `verify.sh` — re-probe the whole catalog

```bash
./verify.sh           # all catalog entries must be live
./verify.sh --refresh # re-harvest upstream lists and rebuild
```

Rules baked into every entry: no key, HTTPS only, send a User-Agent, one request then cache, use `fallback` if the primary dies.

## Sources

Distilled from [public-apis/public-apis](https://github.com/public-apis/public-apis) and [marcelscruz/public-apis](https://github.com/marcelscruz/public-apis), with OpenAPI structure hints from [apis.guru](https://apis.guru). Only entries that pass live verification are included.

## License

MIT
