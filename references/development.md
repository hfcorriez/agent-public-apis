# Development

## Chess.com Public
`GET https://api.chess.com/pub/player/hikaru`
Fields: avatar, player_id, @id, url, name, username, title, followers. Limit: unknown. Fallback: `github-user`.

## GitHub Users
`GET https://api.github.com/users/octocat`
Fields: login, id, node_id, avatar_url, gravatar_id, url, html_url, followers_url. Limit: x-ratelimit-limit 60. Fallback: `npm-registry`.

## npm Registry
`GET https://registry.npmjs.org/react/latest`
Fields: bugs, dist, main, name, engines, exports, gitHead, license. Limit: unknown. Fallback: `chess`.

## 24 Pull Requests
`GET https://24pullrequests.com/projects.json`
Fields: description, github_url, main_language. Limit: unknown. Fallback: `api-status-check`.

## API Status Check
`GET https://apistatuscheck.com/api/badge/stripe`
Fields: xml. Limit: unknown. Fallback: `format-json-online-dummy-api`.

## CDNJS
`GET https://api.cdnjs.com/libraries/jquery`
Fields: name, latest, sri, description, keywords, version, filename, homepage. Limit: unknown. Fallback: `domaindb-info`.

## Chess Magnus
`GET https://api.chess.com/pub/player/magnuscarlsen`
Fields: avatar, player_id, @id, url, name, username, title, followers. Limit: unknown. Fallback: `rubygems-rake`.

## Codex Reset
`GET https://codex-reset.com/llms.txt`
Fields: text. Limit: unknown. Fallback: `cdnjs`.

## DigitalOcean Status
`GET https://status.digitalocean.com/api/v2/summary.json`
Fields: page, components, incidents, scheduled_maintenances, status. Limit: unknown. Fallback: `ipify-2`.

## DigitalOcean Status
`GET https://status.digitalocean.com/index.json`
Fields: page, status, components, incidents. Limit: unknown. Fallback: `ifttt`.

## DigMyName
`GET https://api.digmyname.com/functions/v1/public-api/openapi.json`
Fields: openapi, info, servers, paths. Limit: unknown. Fallback: `domaindb-info`. Role: spec-only.

## DomainDb Info
`GET https://api.domainsdb.info`
Fields: message, status. Limit: unknown. Fallback: `codex-reset`.

## ExtendsClass JSON Storage
`GET https://extendsclass.com/json-storage.openapi.json`
Fields: openapi, info, servers, paths, components. Limit: unknown. Fallback: `phone-specs`. Role: spec-only.

## Format JSON Online Dummy API
`GET https://formatjsononline.com/api/users/paginated?page=1&limit=2`
Fields: success, data, links, meta. Limit: unknown. Fallback: `iplocate`.

## Gh Octocat Repos
`GET https://api.github.com/users/octocat/repos?per_page=1`
Fields: id, node_id, name, full_name, private, owner, html_url, description. Limit: x-ratelimit-limit 60. Fallback: `chess-magnus`.

## Git.io
`GET https://github.blog/wp-json/wp/v2/posts/31356`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `chess`.

## Github Zen
`GET https://api.github.com/zen`
Fields: text. Limit: x-ratelimit-limit 60. Fallback: `24-pull-requests`.

## Hashnode
`GET https://cdn.hashnode.com/res/hashnode/image/upload/v1724758488980/4a54c25f-34b1-43ca-ad10-2229ed7b660e.jpeg?w=100`
Fields: binary. Limit: unknown. Fallback: `git-io`.

## Hipsum
`GET https://hipsum.co/wp-json/wp/v2/pages/5`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `digmyname`.

## Httpbingo Ip
`GET https://httpbingo.org/ip`
Fields: origin. Limit: unknown. Fallback: `npm-lodash`.

## HTTPie
`GET https://httpie.io/api/feed/atom`
Fields: xml. Limit: unknown. Fallback: `ipquery`.

## IFTTT
`GET https://platform.ifttt.com/index.json`
Fields: data. Limit: unknown. Fallback: `ipify-2`.

## IPify
`GET https://api.ipify.org?format=json`
Fields: ip. Limit: unknown. Fallback: `hipsum`.

## IPLocate
`GET https://iplocate.io/api/lookup/`
Fields: ip, country, country_code, is_eu, city, continent, latitude, longitude. Limit: x-ratelimit-limit 50. Fallback: `httpie`.

## IPQuery
`GET https://api.ipquery.io`
Fields: text. Limit: unknown. Fallback: `yamline`.

## MyIPRightNow
`GET https://myiprightnow.com/api/ip`
Fields: ip, version, city, region, country, postalCode, timezone, network. Limit: unknown. Fallback: `qr-code-crafter`.

## Npm Lodash
`GET https://registry.npmjs.org/lodash/latest`
Fields: bugs, dist, icon, main, name, author, gitHead, license. Limit: unknown. Fallback: `gh-octocat-repos`.

## OutageDeck
`GET https://outagedeck.com/api/v1/providers?category=cloud&status=degraded&sort=severity`
Fields: meta, data. Limit: x-ratelimit-limit 120. Fallback: `qr-code`.

## Phone Specs
`GET https://phone-specs-api-production.up.railway.app/openapi.json`
Fields: openapi, info, paths, components. Limit: unknown. Fallback: `myiprightnow`. Role: spec-only.

## Postmanecho
`GET https://postman-echo.com/get?foo=bar`
Fields: args, headers, url. Limit: unknown. Fallback: `qr-barcode`.

## QR & Barcode
`GET https://solsigs.com/openapi.json`
Fields: openapi, info, servers, security, tags, components, paths, x-mcp-integration. Limit: unknown. Fallback: `tinymind-agent-tools`. Role: spec-only.

## QR code
`GET https://qrtag.net/api/qr.png`
Fields: binary. Limit: unknown. Fallback: `qr-barcode`.

## QR Code Crafter
`GET https://qrcodecrafter.com/.well-known/webmcp.json`
Fields: version, name, description, lastUpdated, site, api, agentGuidance, tools. Limit: unknown. Fallback: `quickchart`.

## QuickChart
`GET https://quickchart.io/openapi.json`
Fields: openapi, info, servers, tags, paths, components. Limit: unknown. Fallback: `reqres`. Role: spec-only.

## ReqRes
`GET https://reqres.in/api/`
Fields: name, version, description, documentation, endpoints, features. Limit: unknown. Fallback: `rubygems`.

## Rubygems
`GET https://rubygems.org/api/v1/gems/rails.json`
Fields: name, downloads, version, version_created_at, version_downloads, platform, authors, info. Limit: unknown. Fallback: `github-zen`.

## Rubygems Rake
`GET https://rubygems.org/api/v1/gems/rake.json`
Fields: name, downloads, version, version_created_at, version_downloads, platform, authors, info. Limit: unknown. Fallback: `chess`.

## SQLable
`GET https://sqlable.com/wp-json/wp/v2/pages/226`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `cdnjs`.

## TinyMind Agent Tools
`GET https://tinymind.eu/api/haiku`
Fields: date, line1, line2, line3, total_collection, today_index, note, maintained_by. Limit: unknown. Fallback: `24-pull-requests`.

## YAMLine
`GET https://yamline.com/wp-json/wp/v2/pages/50`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `sqlable`.
