# Documents & Productivity

## DocForge
`GET https://docforge-api.vercel.app/api`
Fields: name, version, status, timestamp, auth, endpoints. Limit: unknown. Fallback: `kiprio-pdf-text`.

## FastApi Simple Calculator
`GET https://fastapi-calculadora.onrender.com/openapi.json`
Fields: openapi, info, paths, components. Limit: unknown. Fallback: `docforge`. Role: spec-only.

## Kiprio PDF Text
`GET https://kiprio.com/v1/pdf-text`
Fields: product, description, usage, limits, rate_limits, returns, signup_url, docs_url. Limit: unknown. Fallback: `reportforge`.

## ReportForge
`GET https://reportforge-api.vercel.app/api`
Fields: name, version, status, timestamp, description, auth, endpoints. Limit: unknown. Fallback: `docforge`.

## WakaTime
`GET https://wakatime.com/api/v1/editors`
Fields: data, total, total_pages. Limit: unknown. Fallback: `fastapi-simple-calculator`.
