# Geocoding

## country.is
`GET https://api.country.is/`
Fields: ip, country. Limit: unknown. Fallback: `ipify`.

## geoJS
`GET https://get.geojs.io/v1/ip/geo.json`
Fields: accuracy, area_code, asn, city, continent_code, country, country_code, country_code3. Limit: unknown. Fallback: `zippopotam`.

## ipify
`GET https://api.ipify.org?format=json`
Fields: ip. Limit: unknown. Fallback: `ipwho`.

## ipwho.is
`GET https://ipwho.is/`
Fields: ip, success, type, continent, continent_code, country, country_code, region. Limit: unknown. Fallback: `geojs`.

## Open-Meteo Geocoding
`GET https://geocoding-api.open-meteo.com/v1/search?name=Berlin&count=1`
Fields: results, generationtime_ms. Limit: unknown. Fallback: `country-is`.

## Zippopotam
`GET https://api.zippopotam.us/us/90210`
Fields: country, country abbreviation, post code, places. Limit: unknown. Fallback: `open-meteo-geocode`.

## BdAPIs
`GET https://bdapis.com/api/v2`
Fields: status. Limit: unknown. Fallback: `ducks-unlimited`.

## BdAPIs
`GET https://bdapis.com/api`
Fields: status, data. Limit: unknown. Fallback: `ip-address-details`.

## Cep.la
`GET https://cep.la/wp-json/wp/v2/pages/21`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `bdapis`.

## Country
`GET https://api.country.is/openapi.json`
Fields: openapi, info, paths, components. Limit: unknown. Fallback: `cep-la`. Role: spec-only.

## Ducks Unlimited
`GET https://gis.ducks.org/data.json`
Fields: @context, @type, conformsTo, describedBy, dataset. Limit: unknown. Fallback: `ipgeo`.

## Freeipapi
`GET https://freeipapi.com/api/json`
Fields: ipVersion, ipAddress, latitude, longitude, countryName, countryCode, capital, phoneCodes. Limit: x-ratelimit-limit 60. Fallback: `ipguide`.

## Geojs Ip
`GET https://get.geojs.io/v1/ip.json`
Fields: ip. Limit: unknown. Fallback: `country-is`.

## HackMyIP
`GET https://hackmyip.com/api/ip`
Fields: success, data. Limit: x-ratelimit-limit 100. Fallback: `ifconfig`.

## Ifconfig
`GET https://ifconfig.co/json`
Fields: ip, ip_decimal, country, country_iso, country_eu, region_name, region_code, metro_code. Limit: unknown. Fallback: `freeipapi`.

## IP Address Details
`GET https://ipinfo.io`
Fields: ip, hostname, city, region, country, loc, org, postal. Limit: unknown. Fallback: `ipgeo`.

## ip.app
`GET https://ip.app`
Fields: ip, ip_version. Limit: unknown. Fallback: `bdapis`.

## Ipapi Co
`GET https://ipapi.co/json/`
Fields: ip, network, version, city, region, region_code, country, country_name. Limit: unknown. Fallback: `bdapis`.

## IPGEO
`GET https://api.techniknews.net/ipgeo`
Fields: status, continent, country, countryCode, regionName, city, zip, lat. Limit: unknown. Fallback: `ip-app`.

## Ipguide
`GET https://ip.guide/`
Fields: ip, network, location. Limit: unknown. Fallback: `nominatim`.

## Ipify V6
`GET https://api64.ipify.org?format=json`
Fields: ip. Limit: unknown. Fallback: `zip-nyc`.

## LatLng
`GET https://api.latlng.work/api?q=Seattle,WA`
Fields: type, features. Limit: x-ratelimit-limit 60. Fallback: `rest-countries`.

## Nominatim
`GET https://nominatim.openstreetmap.org/search?q=London&format=json&limit=1`
Fields: place_id, licence, osm_type, osm_id, lat, lon, class, type. Limit: unknown. Fallback: `ipapi-co`.

## Open Topo Data
`GET https://api.opentopodata.org/v1/test-dataset?locations=56,123`
Fields: results, status. Limit: unknown. Fallback: `postali`.

## PostalCodes
`GET https://postalcodes.info/openapi.json`
Fields: openapi, info, servers, tags, paths, components. Limit: unknown. Fallback: `country`. Role: spec-only.

## Postali
`GET https://postali.app/api/v1/mx/cp/06700`
Fields: cp, estado, estado_slug, municipio, municipio_slug, asentamientos. Limit: unknown. Fallback: `latlng`.

## REST Countries
`GET https://static-03.restcountries.com/rest-countries/static/images/clients/v1/apple-icon.png`
Fields: binary. Limit: unknown. Fallback: `postalcodes`.

## Zip Nyc
`GET https://api.zippopotam.us/us/10001`
Fields: country, country abbreviation, post code, places. Limit: unknown. Fallback: `country-is`.
