# Books

## Bhagavad Gita telugu
`GET https://gita-api.vercel.app/openapi.json`
Fields: openapi, info, paths, components. Limit: unknown. Fallback: `kdp-intelligence`. Role: spec-only.

## Gutendex
`GET https://gutendex.com/books/?search=pride`
Fields: count, next, previous, results. Limit: unknown. Fallback: `bhagavad-gita-telugu`.

## KDP Intelligence
`GET https://kdp-intelligence-api.vercel.app/openapi.json`
Fields: openapi, info, paths, components. Limit: unknown. Fallback: `open-library-2`. Role: spec-only.

## Open Library
`GET https://openlibrary.org/data.json`
Fields: body, title, m, key, type, latest_revision, revision, created. Limit: unknown. Fallback: `bhagavad-gita-telugu`.

## Stephen King
`GET https://stephen-king-api.onrender.com/api/books`
Fields: data. Limit: unknown. Fallback: `bhagavad-gita-telugu`.
