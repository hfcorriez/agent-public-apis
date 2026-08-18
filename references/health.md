# Health

## Covid Tracking Project
`GET https://api.covidtracking.com/v2/us/daily/2021-01-02.json`
Fields: meta, data. Limit: unknown. Fallback: `open-data-nhs-scotland`.

## Humanitarian Data Exchange
`GET https://data.humdata.org/api`
Fields: version. Limit: unknown. Fallback: `medlineplus-genetics`.

## Makeup
`GET https://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush`
Fields: id, brand, name, price, price_sign, currency, image_link, product_link. Limit: unknown. Fallback: `verified-supplement-data`.

## MedlinePlus Genetics
`GET https://medlineplus.gov/download/genetics/condition/alzheimer-disease.json`
Fields: _comment, name, ghr_page, text-list, inheritance-pattern-list, related-gene-list, synonym-list, db-key-list. Limit: unknown. Fallback: `nppes`.

## NPPES
`GET https://npiregistry.cms.hhs.gov/api`
Fields: Errors. Limit: unknown. Fallback: `covid-tracking-project`.

## Open Data NHS Scotland
`GET https://www.opendata.nhs.scot/api`
Fields: version. Limit: unknown. Fallback: `psychologie-et-s-r-nit`.

## Psychologie et Sérénité
`GET https://psychologieetserenite.com/api/v1/openapi.json`
Fields: openapi, info, servers, paths, components, x-rate-limit, x-license, x-citation. Limit: unknown. Fallback: `makeup`. Role: spec-only.

## Verified Supplement Data
`GET https://verifiedsupplementdata.com/api/v1/recommend/index.json`
Fields: name, description, version, usage, supplements, interactionCheck, dataSources, affiliateDisclosure. Limit: unknown. Fallback: `humanitarian-data-exchange`.
