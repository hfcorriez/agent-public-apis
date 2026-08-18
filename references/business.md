# Business

## Legal Sandbox Georgia
`GET https://legal.ge/api/openapi.json`
Fields: openapi, info, servers, tags, paths, components. Limit: unknown. Fallback: `mydentify`. Role: spec-only.

## Mydentify
`GET https://mydentify.com/openapi.json`
Fields: openapi, info, servers, security, externalDocs, x-cors, paths, components. Limit: unknown. Fallback: `legal-sandbox-georgia`. Role: spec-only.

## Pick an Agency
`GET https://www.pickanagency.com/api/v1/search?service=SEO&city=Berlin&min_rating=4.5&limit=5`
Fields: count, results, meta. Limit: unknown. Fallback: `legal-sandbox-georgia`.
