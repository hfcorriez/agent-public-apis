# Entertainment

## Chuck Norris Jokes
`GET https://api.chucknorris.io/jokes/random`
Fields: categories, created_at, icon_url, id, updated_at, url, value. Limit: unknown. Fallback: `pokeapi`.

## JokeAPI
`GET https://v2.jokeapi.dev/joke/Programming?type=single`
Fields: error, category, type, joke, flags, id, safe, lang. Limit: retry-after 60. Fallback: `chucknorris`.

## PokéAPI
`GET https://pokeapi.co/api/v2/pokemon/ditto`
Fields: abilities, base_experience, cries, forms, game_indices, height, held_items, id. Limit: unknown. Fallback: `tvmaze`.

## Rick and Morty
`GET https://rickandmortyapi.com/api/character/1`
Fields: id, name, status, species, type, gender, origin, location. Limit: unknown. Fallback: `jokeapi`.

## TVmaze
`GET https://api.tvmaze.com/shows/1`
Fields: id, url, name, type, language, genres, status, runtime. Limit: unknown. Fallback: `rickmorty`.

## CosmyDay Astrology
`GET https://api.cosmyday.com/events/upcoming?days=30&min_importance=60`
Fields: timezone, computed_with, covers, from, to, count, events. Limit: unknown. Fallback: `imgflip`.

## Deny By Default as a Service
`GET https://dbdaas.rajathjaiprakash.com/help`
Fields: name, description, endpoints, content_negotiation. Limit: unknown. Fallback: `cosmyday-astrology`.

## Deny By Default as a Service
`GET https://dbdaas.rajathjaiprakash.com/api/v2`
Fields: reason, type. Limit: unknown. Fallback: `cosmyday-astrology`.

## elonmu.sh
`GET https://elonmu.sh/api`
Fields: source, title, description, url, urlImage, publishDate. Limit: unknown. Fallback: `hp-api`.

## Hp Api
`GET https://hp-api.onrender.com/api/characters`
Fields: id, name, alternate_names, species, gender, house, dateOfBirth, yearOfBirth. Limit: unknown. Fallback: `opentdb`.

## Imgflip
`GET https://api.imgflip.com/get_memes`
Fields: success, data. Limit: unknown. Fallback: `justmeme-wtf`.

## JokeAPI
`GET https://v2.jokeapi.dev/languages?format=txt`
Fields: text. Limit: retry-after 60. Fallback: `deny-by-default-as-a-service`.

## justmeme.wtf
`GET https://justmeme.wtf/api/v1/templates`
Fields: success, templates, total, page, limit. Limit: x-ratelimit-limit 60. Fallback: `memesio`.

## Kanye
`GET https://api.kanye.rest/`
Fields: quote. Limit: unknown. Fallback: `hp-api`.

## Memesio
`GET https://memesio.com/api/free/templates?q=friday+deploy&pageSize=10&mode=hybrid&mediaType=all`
Fields: searchMode, fallbackApplied, mediaType, total, nextPage, page, pageSize, items. Limit: x-ratelimit-limit 3. Fallback: `elonmu-sh`.

## Official Ten
`GET https://official-joke-api.appspot.com/jokes/ten`
Fields: type, setup, punchline, id. Limit: unknown. Fallback: `pokeapi-berry`.

## Officialjoke
`GET https://official-joke-api.appspot.com/random_joke`
Fields: type, setup, punchline, id. Limit: unknown. Fallback: `kanye`.

## Opentdb
`GET https://opentdb.com/api.php?amount=1`
Fields: response_code, results. Limit: unknown. Fallback: `cosmyday-astrology`.

## Pokeapi Berry
`GET https://pokeapi.co/api/v2/berry/1`
Fields: firmness, flavors, growth_time, id, item, max_harvest, name, natural_gift_power. Limit: unknown. Fallback: `rickmorty-loc`.

## Rickmorty Loc
`GET https://rickandmortyapi.com/api/location/1`
Fields: id, name, type, dimension, residents, url, created. Limit: unknown. Fallback: `chucknorris`.

## Sample Movies
`GET https://api.sampleapis.com/movies/animation`
Fields: id, title, posterURL, imdbId. Limit: unknown. Fallback: `useless-today`.

## Useless Today
`GET https://uselessfacts.jsph.pl/api/v2/facts/today`
Fields: id, text, source, source_url, language, permalink. Limit: unknown. Fallback: `official-ten`.

## Uselessfacts
`GET https://uselessfacts.jsph.pl/api/v2/facts/random`
Fields: id, text, source, source_url, language, permalink. Limit: unknown. Fallback: `officialjoke`.
