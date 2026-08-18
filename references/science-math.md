# Science & Math

## Art Institute of Chicago
`GET https://api.artic.edu/api/v1/artworks/129884?fields=id,title,artist_display`
Fields: data, info, config. Limit: unknown. Fallback: `usgs`.

## GBIF Species Match
`GET https://api.gbif.org/v1/species/match?name=Puma%20concolor`
Fields: usageKey, scientificName, canonicalName, rank, status, confidence, matchType, kingdom. Limit: unknown. Fallback: `openfda`.

## Open Library Search
`GET https://openlibrary.org/search.json?q=dune&limit=1`
Fields: numFound, start, numFoundExact, num_found, documentation_url, q, offset, docs. Limit: unknown. Fallback: `gbif`.

## openFDA Drug Labels
`GET https://api.fda.gov/drug/label.json?limit=1`
Fields: meta, results. Limit: unknown. Fallback: `carbonuk`.

## UK Carbon Intensity
`GET https://api.carbonintensity.org.uk/intensity`
Fields: data. Limit: unknown. Fallback: `artic`.

## USGS Earthquakes
`GET https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson`
Fields: type, metadata, features, bbox. Limit: unknown. Fallback: `wikipedia`.

## Wikipedia REST Summary
`GET https://en.wikipedia.org/api/rest_v1/page/summary/Earth`
Fields: type, title, displaytitle, namespace, wikibase_item, titles, pageid, thumbnail. Limit: unknown. Fallback: `openlibrary`.

## Artic List
`GET https://api.artic.edu/api/v1/artworks?limit=1`
Fields: pagination, data, info, config. Limit: unknown. Fallback: `crossref-doi`.

## Crossref
`GET https://api.crossref.org/works?query=climate&rows=1`
Fields: status, message-type, message-version, message. Limit: unknown. Fallback: `cyclecalcs`.

## Crossref Doi
`GET https://api.crossref.org/works/10.1037/0003-066X.59.1.29`
Fields: status, message-type, message-version, message. Limit: unknown. Fallback: `artic`.

## CycleCalcs
`GET https://www.cyclecalcs.com/v2`
Fields: endpoint, computed_at, query, data, warnings, links, meta, attribution. Limit: x-ratelimit-limit 300. Fallback: `iseven-humor`.

## Gbif Tiger
`GET https://api.gbif.org/v1/species/match?name=Panthera%20tigris`
Fields: usageKey, scientificName, canonicalName, rank, status, confidence, matchType, kingdom. Limit: unknown. Fallback: `openfda-food`.

## isEven (humor)
`GET https://api.isevenapi.xyz/api/iseven/6/`
Fields: ad, iseven. Limit: unknown. Fallback: `isro`.

## ISRO
`GET https://isro.vercel.app/api/spacecrafts`
Fields: spacecrafts. Limit: unknown. Fallback: `moonlora`.

## Moonlora
`GET https://moonlora.com/api/v1/phase?date=1969-07-20`
Fields: date, phase, illumination, moonAgeDays, moonSign, nextFullMoon, nextNewMoon, attribution. Limit: unknown. Fallback: `satellite-passes`.

## Openfda Food
`GET https://api.fda.gov/food/enforcement.json?limit=1`
Fields: meta, results. Limit: unknown. Fallback: `artic-list`.

## Satellite Passes
`GET https://sat.terrestre.ar/openapi.json`
Fields: openapi, info, servers, paths, components. Limit: unknown. Fallback: `share`. Role: spec-only.

## SHARE
`GET https://share.osf.io/api/v2`
Fields: data. Limit: unknown. Fallback: `iseven-humor`.

## Sunrise and Sunset
`GET https://api.sunrise-sunset.org/v2?lat=36.7201600&lng=-4.4203400`
Fields: date, tzid, utc_offset, lat, lng, sunrise, sunset, solar_noon. Limit: unknown. Fallback: `moonlora`.

## Tallytopia
`GET https://tallytopia.com/api/v1/calculate/mortgage-payment?principal=300000&annualRate=7&years=30`
Fields: calculator, title, inputs, steps, result, disclaimer, docs. Limit: unknown. Fallback: `sunrise-and-sunset`.

## Usgs Day
`GET https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson`
Fields: type, metadata, features, bbox. Limit: unknown. Fallback: `wiki-moon`.

## Wiki Moon
`GET https://en.wikipedia.org/api/rest_v1/page/summary/Moon`
Fields: type, title, displaytitle, namespace, wikibase_item, titles, pageid, thumbnail. Limit: unknown. Fallback: `gbif-tiger`.
