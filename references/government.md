# Government

## Api Colombia
`GET https://api-colombia.com/api/v1/Country/Colombia`
Fields: id, name, description, stateCapital, surface, population, languages, timeZone. Limit: unknown. Fallback: `city-gdynia`.

## Bank Negara Malaysia Open Data
`GET https://api.bnm.gov.my/api/specification/categories`
Fields: servers, categories. Limit: unknown. Fallback: `city-gda-sk`.

## Brazil Central Bank Open Data
`GET https://dadosabertos.bcb.gov.br/api`
Fields: version. Limit: unknown. Fallback: `city-new-york-open-data`.

## Brazil CNPJ
`GET https://api.cnpj.wiki/v1/cnpj/00000000000191`
Fields: cnpj, cnpj_base, razao_social, nome_fantasia, matriz_filial, situacao_cadastral, situacao_especial, data_inicio_atividade. Limit: x-ratelimit-limit 60. Fallback: `tollmint`.

## Brazilian Chamber of Deputies Open Data
`GET https://dadosabertos.camara.leg.br/api/v2/api-docs`
Fields: openapi, info, servers, tags, paths, components. Limit: retry-after 30. Fallback: `city-toronto-open-data`. Role: spec-only.

## City, Gdańsk
`GET https://ckan.multimediagdansk.pl/api`
Fields: version. Limit: unknown. Fallback: `city-gdynia`.

## City, Gdynia
`GET https://otwartedane.gdynia.pl/api`
Fields: version. Limit: unknown. Fallback: `city-new-york-open-data`.

## City, New York Open Data
`GET https://opendata.cityofnewyork.us/wp-json/wp/v2/pages/40`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `neotimo-dgfip-mirror`.

## City, Toronto Open Data
`GET https://open.toronto.ca/wp-json/wp/v2/pages/2`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `brazil-central-bank-open-data`.

## Indian Mandi Prices
`GET https://mandi-api.onrender.com/v1`
Fields: success, message, endpoints. Limit: unknown. Fallback: `brazilian-chamber-of-deputies-open-data`.

## Istanbul (İBB) Open Data
`GET https://data.ibb.gov.tr/api`
Fields: version. Limit: unknown. Fallback: `open-government-ireland`.

## Neotimo DGFiP Mirror
`GET https://neotimo.com/api/v1/neotimo/annuaire/routing/80438439400016`
Fields: data. Limit: unknown. Fallback: `istanbul-i-bb-open-data`.

## Open Government, Argentina
`GET https://datos.gob.ar/api`
Fields: version. Limit: unknown. Fallback: `open-government-queensland-government`.

## Open Government, Indonesia
`GET https://data.go.id/api/minio/news?file=backend/1786336057772-DTI-CX.jpg`
Fields: binary. Limit: unknown. Fallback: `open-government-switzerland`.

## Open Government, Ireland
`GET https://data.gov.ie/api`
Fields: version. Limit: unknown. Fallback: `open-government-argentina`.

## Open Government, Lithuania
`GET https://data.gov.lt/partner/api/1/`
Fields: swagger, info, host, schemes, basePath, consumes, produces, securityDefinitions. Limit: unknown. Fallback: `open-government-queensland-government`. Role: spec-only.

## Open Government, Queensland Government
`GET https://www.data.qld.gov.au/api`
Fields: version. Limit: unknown. Fallback: `open-government-lithuania`.

## Open Government, Spain
`GET https://datos.gob.es/api`
Fields: version. Limit: unknown. Fallback: `open-government-indonesia`.

## Open Government, Switzerland
`GET https://opendata.swiss/api/3/action/package_search?fq=tags:economy`
Fields: help, success, result. Limit: unknown. Fallback: `openmercantil`.

## OpenMercantil
`GET https://openmercantil.es/api/v1/search?q=mercadona&limit=5`
Fields: query, count, offset, items, _source_catalog, _data_sources_used, _attributions. Limit: x-ratelimit-limit 200. Fallback: `api-colombia`.

## Tollmint
`GET https://api.tollmint.com`
Fields: service, description, website, products, start_here, payment. Limit: unknown. Fallback: `bank-negara-malaysia-open-data`.

## USPTO
`GET https://www.uspto.gov/data.json`
Fields: @type, conformsTo, @context, describedBy, dataset. Limit: unknown. Fallback: `api-colombia`.
