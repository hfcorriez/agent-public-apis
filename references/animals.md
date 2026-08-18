# Animals

## Cat Facts
`GET https://catfact.ninja/docs?api-docs.json`
Fields: openapi, info, paths, components, tags. Limit: unknown. Fallback: `cataas`. Role: spec-only.

## Cataas
`GET https://cataas.com/api/cats?tags=cute`
Fields: id, tags, mimetype, createdAt. Limit: unknown. Fallback: `xeno-canto`.

## Catapi
`GET https://api.thecatapi.com/v1/images/search`
Fields: id, url, width, height. Limit: unknown. Fallback: `cat-facts`.

## RandomDog
`GET https://random.dog/woof.json`
Fields: fileSizeBytes, url. Limit: unknown. Fallback: `randomfox`.

## Randomfox
`GET https://randomfox.ca/floof/`
Fields: image, link. Limit: unknown. Fallback: `catapi`.

## RandomFox
`GET https://randomfox.ca/floof`
Fields: image, link. Limit: unknown. Fallback: `randomdog`.

## xeno-canto
`GET https://xeno-canto.org/api/3/recordings`
Fields: message. Limit: unknown. Fallback: `randomfox`.
