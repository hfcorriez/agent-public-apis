# Sports & Fitness

## DiscGolf
`GET https://io.discgolfapi.com/v1/courses?country=GB&limit=5`
Fields: schema_version, generated_at, attribution, attribution_required, license, license_url, terms_url, no_warranty. Limit: unknown. Fallback: `racing-alpha`.

## F1 API
`GET https://f1api.dev/api/2026/11/race`
Fields: api, url, limit, offset, total, season, races. Limit: unknown. Fallback: `tourneyradar`.

## Football (Soccer) Videos
`GET https://www.scorebat.com/api`
Fields: error, currentTime, response. Limit: unknown. Fallback: `football-soccer-videos-2`.

## Football (Soccer) Videos
`GET https://www.scorebat.com/api/v2`
Fields: error, currentTime, response. Limit: unknown. Fallback: `openf1`.

## OpenF1
`GET https://api.openf1.org`
Fields: text. Limit: unknown. Fallback: `openligadb`.

## OpenLigaDB
`GET https://api.openligadb.de/getmatchdata/bl1/2020/1`
Fields: matchID, matchDateTime, timeZoneID, leagueId, leagueName, leagueSeason, leagueShortcut, matchDateTimeUTC. Limit: unknown. Fallback: `squiggle`.

## Racing Alpha
`GET https://racingalpha.co.uk/api/v1/today`
Fields: date, races, attribution. Limit: unknown. Fallback: `f1-api`.

## SportScore
`GET https://sportscore.com/api/widget/matches/?sport=football&limit=10`
Fields: sport, count, matches, updated. Limit: unknown. Fallback: `openligadb`.

## Squiggle
`GET https://api.squiggle.com.au/?q=teams`
Fields: teams. Limit: unknown. Fallback: `discgolf`.

## TourneyRadar
`GET https://tourneyradar-api.vercel.app`
Fields: name, version, docs, endpoints. Limit: unknown. Fallback: `football-soccer-videos`.
