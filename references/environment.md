# Environment

## Luchtmeetnet
`GET https://api-docs.luchtmeetnet.nl/view/metadata/SVmsWg5g`
Fields: activeVersionTag, latestAvailableVersionTag, collection, environments, user, run, web, team. Limit: unknown. Fallback: `uk-carbon-intensity`.

## UK Carbon Intensity
`GET https://api.carbonintensity.org.uk/intensity`
Fields: data. Limit: unknown. Fallback: `website-carbon`.

## Website Carbon
`GET https://api.websitecarbon.com/data?bytes=12345678&green=1`
Fields: bytes, green, gco2e, rating, statistics, cleanerThan. Limit: unknown. Fallback: `luchtmeetnet`.
