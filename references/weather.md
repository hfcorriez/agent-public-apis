# Weather

## MET Norway
`GET https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.10&lon=9.58`
Fields: type, geometry, properties. Limit: unknown. Fallback: `open-meteo-air`.

## Open-Meteo
`GET https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true`
Fields: latitude, longitude, generationtime_ms, utc_offset_seconds, timezone, timezone_abbreviation, elevation, current_weather_units. Limit: unknown. Fallback: `wttr`.

## Open-Meteo Air Quality
`GET https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&current=us_aqi`
Fields: latitude, longitude, generationtime_ms, utc_offset_seconds, timezone, timezone_abbreviation, elevation, current_units. Limit: unknown. Fallback: `open-meteo`.

## wttr.in
`GET https://wttr.in/London?format=j1`
Fields: current_condition, nearest_area, request, weather. Limit: unknown. Fallback: `met-no`.

## Hail History
`GET https://hail-history-noaa.netlify.app/api`
Fields: status, name, version, description, endpoints, resolution, upstream, auth. Limit: unknown. Fallback: `rainviewer`.

## Openmeteo Marine
`GET https://marine-api.open-meteo.com/v1/marine?latitude=54.32&longitude=10.15&current=wave_height`
Fields: latitude, longitude, generationtime_ms, utc_offset_seconds, timezone, timezone_abbreviation, elevation, current_units. Limit: unknown. Fallback: `hail-history`.

## openSenseMap
`GET https://api.opensensemap.org`
Fields: text. Limit: unknown. Fallback: `hail-history`.

## RainViewer
`GET https://www.rainviewer.com/.well-known/api-catalog`
Fields: linkset. Limit: unknown. Fallback: `us-weather`.

## US Weather
`GET https://api.weather.gov/openapi.json`
Fields: openapi, info, servers, paths, components, security, externalDocs. Limit: unknown. Fallback: `world-time-weather`. Role: spec-only.

## World Time & Weather
`GET https://worldtimeweather.com/api/v1/cities.json`
Fields: version, cities, timezones, endpoints, license, generated_at, data. Limit: unknown. Fallback: `opensensemap`.

## wttr.in
`GET https://wttr.in/index.json`
Fields: text. Limit: unknown. Fallback: `hail-history`.
