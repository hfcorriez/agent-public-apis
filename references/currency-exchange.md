# Currency Exchange

## Currency API (Cloudflare Pages)
`GET https://latest.currency-api.pages.dev/v1/currencies/usd.json`
Fields: date, usd. Limit: unknown. Fallback: `frankfurter`.

## Frankfurter
`GET https://api.frankfurter.dev/v1/latest?from=USD&to=EUR`
Fields: amount, base, date, rates. Limit: unknown. Fallback: `er-api`.

## Open ExchangeRate-API
`GET https://open.er-api.com/v6/latest/USD`
Fields: result, provider, documentation, terms_of_use, time_last_update_unix, time_last_update_utc, time_next_update_unix, time_next_update_utc. Limit: unknown. Fallback: `currency-api`.

## Awesomeapi
`GET https://economia.awesomeapi.com.br/json/last/USD-BRL`
Fields: USDBRL. Limit: unknown. Fallback: `exchangerate-jsdelivr2`.

## Cambio Uruguay
`GET https://api.cambio-uruguay.com`
Fields: origin, type, code, date, buy, name, sell. Limit: unknown. Fallback: `national-bank-of-poland`.

## Currency Jsdelivr
`GET https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json`
Fields: date, usd. Limit: unknown. Fallback: `vatcomply`.

## Czech National Bank
`GET https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.xml`
Fields: xml. Limit: unknown. Fallback: `frankfurter-2`.

## Exchangerate Jsdelivr2
`GET https://latest.currency-api.pages.dev/v1/currencies/eur.json`
Fields: date, eur. Limit: unknown. Fallback: `cambio-uruguay`.

## Exchangerate V4
`GET https://api.exchangerate-api.com/v4/latest/USD`
Fields: provider, WARNING_UPGRADE_TO_V6, terms, base, date, time_last_updated, rates. Limit: unknown. Fallback: `currency-jsdelivr`.

## Frankfurter
`GET https://api.frankfurter.dev/v2/openapi.json`
Fields: openapi, info, servers, paths, components. Limit: unknown. Fallback: `paralelo-bo`. Role: spec-only.

## Frankfurter Gbp
`GET https://api.frankfurter.dev/v1/latest?from=GBP&to=USD`
Fields: amount, base, date, rates. Limit: unknown. Fallback: `nbp-usd`.

## National Bank of Poland
`GET https://api.nbp.pl/api/cenyzlota`
Fields: data, cena. Limit: unknown. Fallback: `czech-national-bank`.

## Nbp
`GET https://api.nbp.pl/api/exchangerates/tables/a/?format=json`
Fields: table, no, effectiveDate, rates. Limit: unknown. Fallback: `awesomeapi`.

## Nbp Usd
`GET https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json`
Fields: table, currency, code, rates. Limit: unknown. Fallback: `vatcomply-eur`.

## paralelo.bo
`GET https://paralelo.bo/api/openapi.json`
Fields: openapi, info, servers, paths, components. Limit: unknown. Fallback: `cambio-uruguay`. Role: spec-only.

## Vatcomply
`GET https://api.vatcomply.com/rates?base=USD`
Fields: date, base, rates. Limit: unknown. Fallback: `nbp`.

## Vatcomply Eur
`GET https://api.vatcomply.com/rates?base=EUR`
Fields: date, base, rates. Limit: unknown. Fallback: `currency-api`.
