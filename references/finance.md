# Finance

## AlQANAAS Gold Data
`GET https://alqanaas.com/gold-data.json`
Fields: @context, @type, @id, name, description, url, creator, dateModified. Limit: unknown. Fallback: `casheva`.

## Casheva
`GET https://casheva.com/api/v1/dolar`
Fields: ok, actualizado, casas, fuente, condiciones. Limit: unknown. Fallback: `econdb`.

## DolarAPI
`GET https://api.argentinadatos.com/static/assets/arq/Desktop_banner_10.png`
Fields: binary. Limit: unknown. Fallback: `alqanaas-gold-data`.

## Econdb
`GET https://www.econdb.com/api`
Fields: sources, datasets, series, maritime/vessels, retail/items. Limit: unknown. Fallback: `zelothorn`.

## Top 5 Stocks
`GET https://top5stocks.netlify.app/api/v1/openapi.json`
Fields: openapi, info, x-documentation, x-history-scope, servers, components, paths. Limit: unknown. Fallback: `alqanaas-gold-data`. Role: spec-only.

## Zelothorn
`GET https://zelothorn.com/api/v1/company/AAPL`
Fields: ticker, cik, company, summary, earnings, filings, links, generatedAt. Limit: unknown. Fallback: `top-5-stocks`.
