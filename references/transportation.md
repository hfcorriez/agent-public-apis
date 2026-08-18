# Transportation

## ADS-B Exchange
`GET https://www.adsbexchange.com/wp-json/wp/v2/pages/443`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `openvan`.

## BC Ferries
`GET https://www.bcferriesapi.ca/api`
Fields: BOW, DUK, FUL, HSB, LNG, NAN, SWB, TSA. Limit: unknown. Fallback: `strait-of-hormuz-ship-monitor`.

## BC Ferries
`GET https://www.bcferriesapi.ca/v2`
Fields: capacityRoutes, nonCapacityRoutes. Limit: unknown. Fallback: `transport-for-paris-france`.

## Can I enter
`GET https://canienter.com/openapi.json`
Fields: openapi, info, externalDocs, servers, x-service-info, components, paths. Limit: unknown. Fallback: `ads-b-exchange`. Role: spec-only.

## OpenVan
`GET https://openvan.camp/docs.openapi`
Fields: text. Limit: unknown. Fallback: `transport-for-los-angeles-us`.

## Strait of Hormuz Ship Monitor
`GET https://hormuz.data-tracking.net/llms.txt`
Fields: text. Limit: unknown. Fallback: `bc-ferries`.

## Transport for Los Angeles, US
`GET https://developer.metro.net/wp-json/wp/v2/pages/6`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `transport-for-switzerland`.

## Transport for Paris, France
`GET https://data.ratp.fr/api/v2`
Fields: links. Limit: unknown. Fallback: `ads-b-exchange`.

## Transport for Switzerland
`GET https://transport.opendata.ch/v1`
Fields: date, author, version. Limit: unknown. Fallback: `transport-for-toronto-canada`.

## Transport for Toronto, Canada
`GET https://myttc.ca/finch_station.json`
Fields: name, uri, stops, time. Limit: unknown. Fallback: `ads-b-exchange`.
