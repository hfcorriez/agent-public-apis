# Open Data

## API Setu
`GET https://apisetu.gov.in/apisetu_logo.png`
Fields: binary. Limit: unknown. Fallback: `open-scholarships`.

## ArgentinaDatos
`GET https://api.argentinadatos.com/static/logos/bcra.png`
Fields: binary. Limit: unknown. Fallback: `college-roi`.

## BotsArchive
`GET https://api.botsarchive.com/getBotID.php`
Fields: ok, message. Limit: unknown. Fallback: `eosl`.

## College ROI
`GET https://le-teen.com/og/api.png`
Fields: binary. Limit: unknown. Fallback: `sofiaplan`.

## CollegeScoreCard.ed.gov
`GET https://collegescorecard.ed.gov/data/_payload.json?d2847bd9-1fde-4288-9b9e-4097fbc6d9e1`
Fields: data, prerenderedAt. Limit: unknown. Fallback: `lottolens-ph`.

## Dimdom
`GET https://api.dimdom.pl`
Fields: text. Limit: unknown. Fallback: `onyx-bazaar`.

## EOSL
`GET https://eosl.ai/og/api.png`
Fields: binary. Limit: unknown. Fallback: `api-setu`.

## i6eal Open AI Data
`GET https://i6eal.de/data/catalog/dcat.jsonld`
Fields: @context, @id, @type, dct:identifier, dct:title, dct:description, dct:publisher, dct:modified. Limit: unknown. Fallback: `opensanctions`.

## InfraNode
`GET https://infranode.dev/api/v1/cities/berlin/weather`
Fields: data, meta. Limit: retry-after 60. Fallback: `argentinadatos`.

## LottoLens PH
`GET https://remo65588-boop.github.io/lottolens-ph-public-data/api/v1/metadata.json`
Fields: apiVersion, datasetVersion, fixedSnapshot, snapshotDate, resultRecordCount, scheduleRecordCount, coverage, games. Limit: unknown. Fallback: `botsarchive`.

## ModelPartFinder Error Codes
`GET https://modelpartfinder.com/api/v1/error-code/Whirlpool/F01`
Fields: ok, brand, code, description, appliance, recommended_skus, source_url. Limit: unknown. Fallback: `wikipedia-2`.

## Nobel Prize
`GET https://api.nobelprize.org/2.1/laureates`
Fields: laureates, meta, links. Limit: unknown. Fallback: `i6eal-open-ai-data`.

## Onyx Bazaar
`GET https://onyx-actions.onrender.com/bazaar`
Fields: view, rows, stats. Limit: unknown. Fallback: `dimdom`.

## Onyx Bazaar
`GET https://onyx-actions.onrender.com/index.json`
Fields: index, version, as_of, headline_correction, total_economy, biggest_segments, fact_verification_buyer, segments. Limit: unknown. Fallback: `ume-open-data`.

## Open Scholarships
`GET https://scholarships.grudged.io/scholarships.json`
Fields: meta, results. Limit: unknown. Fallback: `nobel-prize`.

## OpenSanctions
`GET https://api.opensanctions.org/openapi.json`
Fields: openapi, info, paths, components, tags. Limit: unknown. Fallback: `modelpartfinder-error-codes`. Role: spec-only.

## Sofiaplan
`GET https://sofiaplan.bg/wp-json/wp/v2/pages/7258`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `dimdom`.

## Statistics of the World
`GET https://statisticsoftheworld.com/api/v1/countries`
Fields: count, total, offset, limit, data. Limit: x-ratelimit-limit 1000. Fallback: `infranode`.

## Tilth
`GET https://www.tilth.uk/api/v1/public/fertiliser/dataset?product=AN_UK`
Fields: provider, dataset, license, schema_version, unit, currency, disclaimer, product. Limit: unknown. Fallback: `warnely`.

## Umeå Open Data
`GET https://opendata.umea.se/api/v2`
Fields: links. Limit: unknown. Fallback: `api-setu`.

## Voidly
`GET https://voidly.ai/.well-known/agent-card.json`
Fields: name, description, url, provider, version, capabilities, authentication, defaultInputModes. Limit: unknown. Fallback: `tilth`.

## Warnely
`GET https://www.warnely.com/api/v1/countries`
Fields: count, methodology, licence, attribution, countries. Limit: unknown. Fallback: `statistics-of-the-world`.

## Wikipedia
`GET https://www.mediawiki.org/w/rest.php/v1/search`
Fields: xml. Limit: unknown. Fallback: `voidly`.
