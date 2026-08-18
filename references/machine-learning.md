# Machine Learning

## AI Economics Tools
`GET https://piszczek.pl/tools/api`
Fields: name, author, human_ui, openapi, usage, privacy, attribution, citation_policy. Limit: unknown. Fallback: `not-human-search`. Role: spec-only.

## DreamThreads
`GET https://mydreamthreads.xyz/dream-interpretation-api/openapi.json`
Fields: openapi, info, externalDocs, servers, security, tags, paths, components. Limit: unknown. Fallback: `tensorfeed`. Role: spec-only.

## Not Human Search
`GET https://nothumansearch.ai/api/v1`
Fields: $schema, ai_plugin_manifest, auth, base_url, description, endpoints, mcp_endpoint, name. Limit: unknown. Fallback: `dreamthreads`.

## Statlyte
`GET https://statlyte.com/api/v1/models`
Fields: updated_at, source, count, models. Limit: unknown. Fallback: `ai-economics-tools`.

## TensorFeed
`GET https://tensorfeed.ai/api/agents/news`
Fields: ok, source, updated, count, articles, sanitization. Limit: x-ratelimit-limit 120. Fallback: `statlyte`.
