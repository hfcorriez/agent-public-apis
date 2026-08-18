# News

## DEV.to
`GET https://dev.to/api/articles?per_page=1`
Fields: type_of, id, title, description, readable_publish_date, slug, path, url. Limit: unknown. Fallback: `lobsters`.

## HN Algolia
`GET https://hn.algolia.com/api/v1/search?query=ai&hitsPerPage=1`
Fields: exhaustive, exhaustiveNbHits, exhaustiveTypo, hits, hitsPerPage, nbHits, nbPages, page. Limit: unknown. Fallback: `spaceflight`.

## Lobsters
`GET https://lobste.rs/hottest.json`
Fields: short_id, created_at, title, url, score, flags, comment_count, description. Limit: unknown. Fallback: `hn-algolia`.

## Spaceflight News
`GET https://api.spaceflightnewsapi.net/v4/articles/?limit=1`
Fields: count, next, previous, results. Limit: unknown. Fallback: `devto`.

## Lobsters Newest
`GET https://lobste.rs/newest.json`
Fields: short_id, created_at, title, url, score, flags, comment_count, description. Limit: unknown. Fallback: `devto`.

## Noozra
`GET https://noozra.com/api/articles?category=tech&limit=5`
Fields: articles, next_before, next_before_id, count. Limit: unknown. Fallback: `devto`.
