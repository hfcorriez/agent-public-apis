# Calendar

## Nager.Date Holidays
`GET https://date.nager.at/api/v3/PublicHolidays/2026/US`
Fields: date, localName, name, countryCode, fixed, global, counties, launchYear. Limit: unknown. Fallback: `sunrise`.

## Sunrise-Sunset
`GET https://api.sunrise-sunset.org/json?lat=36.72&lng=-4.42&formatted=0`
Fields: results, status, tzid. Limit: unknown. Fallback: `timeapi`.

## Time API
`GET https://timeapi.io/api/Time/current/zone?timeZone=UTC`
Fields: year, month, day, hour, minute, seconds, milliSeconds, dateTime. Limit: unknown. Fallback: `nager`.

## caldays
`GET https://caldays.com/api/holidays/us`
Fields: code, country, countryLocal, locale, year, license, count, holidays. Limit: unknown. Fallback: `the-calendar`.

## Nager Gb
`GET https://date.nager.at/api/v3/PublicHolidays/2026/GB`
Fields: date, localName, name, countryCode, fixed, global, counties, launchYear. Limit: unknown. Fallback: `nager`.

## The Calendar
`GET https://the-calendar.net/api/holidays/us-federal/2026.json`
Fields: country, kind, year, source, holidays. Limit: unknown. Fallback: `uk-bank-holidays`.

## UK Bank Holidays
`GET https://www.gov.uk/bank-holidays.json`
Fields: england-and-wales, scotland, northern-ireland. Limit: unknown. Fallback: `caldays`.
