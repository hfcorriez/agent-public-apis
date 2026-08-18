# Music

## Genrenator
`GET https://binaryjazz.us/wp-json/wp/v2/pages/182`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `musicbrainz`.

## Musicbrainz
`GET https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json`
Fields: type, isnis, disambiguation, id, name, ipis, sort-name, type-id. Limit: x-ratelimit-limit 1200. Fallback: `genrenator`.
