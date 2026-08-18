---
name: agent-public-apis
description: Call verified no-key public APIs. Use when the user needs a free HTTPS API with no signup — weather, geo, news, crypto, dictionaries, test data, or any category in the index.
---

# agent-public-apis

Verified no-key HTTPS APIs. Catalog is `data/apis.json`. Full entries live in `references/`. Re-check with `./verify.sh`.

```bash
curl -sS -L -H "User-Agent: agent-public-apis/1.0" -H "Accept: application/json" "<url>"
```

Rules: no key, HTTPS only, send a User-Agent, one request then cache, use `fallback` if the primary dies.

## Index

- [Animals](references/animals.md) (7)
- [Anime](references/anime.md) (5)
- [Art & Design](references/art-design.md) (8)
- [Blockchain](references/blockchain.md) (4)
- [Books](references/books.md) (5)
- [Business](references/business.md) (3)
- [Calendar](references/calendar.md) (7)
- [Cryptocurrency](references/cryptocurrency.md) (21)
- [Currency Exchange](references/currency-exchange.md) (17)
- [Development](references/development.md) (40)
- [Dictionaries](references/dictionaries.md) (10)
- [Documents & Productivity](references/documents-productivity.md) (5)
- [Email](references/email.md) (4)
- [Entertainment](references/entertainment.md) (23)
- [Environment](references/environment.md) (3)
- [Finance](references/finance.md) (6)
- [Food & Drink](references/food-drink.md) (10)
- [Games & Comics](references/games-comics.md) (23)
- [Geocoding](references/geocoding.md) (28)
- [Government](references/government.md) (22)
- [Health](references/health.md) (8)
- [Jobs](references/jobs.md) (5)
- [Machine Learning](references/machine-learning.md) (5)
- [Music](references/music.md) (2)
- [News](references/news.md) (6)
- [Open Data](references/open-data.md) (23)
- [Open Source Projects](references/open-source-projects.md) (4)
- [Personality](references/personality.md) (9)
- [Photography](references/photography.md) (2)
- [Programming](references/programming.md) (3)
- [Science & Math](references/science-math.md) (22)
- [Security](references/security.md) (5)
- [Shopping](references/shopping.md) (2)
- [Sports & Fitness](references/sports-fitness.md) (10)
- [Test Data](references/test-data.md) (23)
- [Transportation](references/transportation.md) (10)
- [Vehicle](references/vehicle.md) (2)
- [Video](references/video.md) (8)
- [Weather](references/weather.md) (11)

## Recommended

### Calendar
- **Nager.Date Holidays** `https://date.nager.at/api/v3/PublicHolidays/2026/US` — date, localName, name, countryCode
- **Sunrise-Sunset** `https://api.sunrise-sunset.org/json?lat=36.72&lng=-4.42&formatted=0` — results, status, tzid
- **Time API** `https://timeapi.io/api/Time/current/zone?timeZone=UTC` — year, month, day, hour

### Cryptocurrency
- **Coinbase Spot** `https://api.coinbase.com/v2/prices/BTC-USD/spot` — data
- **CoinGecko** `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd` — bitcoin
- **Coinlore** `https://api.coinlore.net/api/ticker/?id=90` — id, symbol, name, nameid

### Currency Exchange
- **Currency API (Cloudflare Pages)** `https://latest.currency-api.pages.dev/v1/currencies/usd.json` — date, usd
- **Frankfurter** `https://api.frankfurter.dev/v1/latest?from=USD&to=EUR` — amount, base, date, rates
- **Open ExchangeRate-API** `https://open.er-api.com/v6/latest/USD` — result, provider, documentation, terms_of_use

### Development
- **Chess.com Public** `https://api.chess.com/pub/player/hikaru` — avatar, player_id, @id, url
- **GitHub Users** `https://api.github.com/users/octocat` — login, id, node_id, avatar_url
- **npm Registry** `https://registry.npmjs.org/react/latest` — bugs, dist, main, name

### Dictionaries
- **Datamuse** `https://api.datamuse.com/words?rel_syn=happy&max=5` — word, score
- **Free Dictionary API** `https://api.dictionaryapi.dev/api/v2/entries/en/hello` — word, phonetics, meanings, license
- **LanguageTool languages** `https://api.languagetool.org/v2/languages` — name, code, longCode

### Entertainment
- **Chuck Norris Jokes** `https://api.chucknorris.io/jokes/random` — categories, created_at, icon_url, id
- **JokeAPI** `https://v2.jokeapi.dev/joke/Programming?type=single` — error, category, type, joke
- **PokéAPI** `https://pokeapi.co/api/v2/pokemon/ditto` — abilities, base_experience, cries, forms

### Geocoding
- **country.is** `https://api.country.is/` — ip, country
- **geoJS** `https://get.geojs.io/v1/ip/geo.json` — accuracy, area_code, asn, city
- **ipify** `https://api.ipify.org?format=json` — ip

### News
- **DEV.to** `https://dev.to/api/articles?per_page=1` — type_of, id, title, description
- **HN Algolia** `https://hn.algolia.com/api/v1/search?query=ai&hitsPerPage=1` — exhaustive, exhaustiveNbHits, exhaustiveTypo, hits
- **Lobsters** `https://lobste.rs/hottest.json` — short_id, created_at, title, url

### Science & Math
- **Art Institute of Chicago** `https://api.artic.edu/api/v1/artworks/129884?fields=id,title,artist_display` — data, info, config
- **GBIF Species Match** `https://api.gbif.org/v1/species/match?name=Puma%20concolor` — usageKey, scientificName, canonicalName, rank
- **Open Library Search** `https://openlibrary.org/search.json?q=dune&limit=1` — numFound, start, numFoundExact, num_found

### Test Data
- **Dog CEO** `https://dog.ceo/api/breeds/image/random` — message, status
- **DummyJSON** `https://dummyjson.com/products/1` — id, title, description, category
- **Fake Store** `https://fakestoreapi.com/products/1` — id, title, price, description

### Weather
- **MET Norway** `https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.10&lon=9.58` — type, geometry, properties
- **Open-Meteo** `https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true` — latitude, longitude, generationtime_ms, utc_offset_seconds
- **Open-Meteo Air Quality** `https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&current=us_aqi` — latitude, longitude, generationtime_ms, utc_offset_seconds

## Refresh

```bash
./verify.sh           # re-probe data/apis.json, require 100% live and ≥400
./verify.sh --refresh # re-harvest sources, probe, regenerate docs
```
