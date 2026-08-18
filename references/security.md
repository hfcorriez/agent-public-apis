# Security

## ChronoVerify
`GET https://chronoverify.com/openapi.json`
Fields: openapi, info, paths, components, servers. Limit: unknown. Fallback: `defend-network`. Role: spec-only.

## dead-drop
`GET https://api.dead-drop.xyz/api/v1/docs/openapi.json`
Fields: openapi, info, servers, tags, components, paths. Limit: x-ratelimit-limit 100. Fallback: `defend-network`. Role: spec-only.

## Defend Network
`GET https://defend.network/api/v1/cves/latest.json`
Fields: meta, cves. Limit: unknown. Fallback: `phishstats`.

## PhishStats
`GET https://api.phishstats.info/api/phishing`
Fields: id, url, redirect_url, ip, countrycode, countryname, regioncode, regionname. Limit: unknown. Fallback: `chronoverify`.

## ScanMalware
`GET https://scanmalware.com/api/v1/rss`
Fields: xml. Limit: unknown. Fallback: `chronoverify`.
