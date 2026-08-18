# Video

## An API of Ice And Fire
`GET https://anapioficeandfire.com/api`
Fields: books, characters, houses. Limit: unknown. Fallback: `swapi`.

## Final Space
`GET https://finalspaceapi.com/api/v0/`
Fields: type, name, path, fullUrl. Limit: x-ratelimit-limit 500. Fallback: `swapi-2`.

## Iceandfire Book
`GET https://anapioficeandfire.com/api/books/1`
Fields: url, name, isbn, authors, numberOfPages, publisher, country, mediaType. Limit: unknown. Fallback: `swapi-py4e`.

## Shoof Aflam
`GET https://shoofaflam.tv/api/platforms.json`
Fields: id, name_ar, name_en, slug, color, logo_text, price_sa, price_eg. Limit: unknown. Fallback: `an-api-of-ice-and-fire`.

## SWAPI
`GET https://swapi.dev/api/`
Fields: people, planets, films, species, vehicles, starships. Limit: unknown. Fallback: `tvmaze-2`.

## SWAPI
`GET https://www.swapi.tech/api`
Fields: message, result, apiVersion, timestamp, support. Limit: x-ratelimit-limit 100. Fallback: `an-api-of-ice-and-fire`.

## Swapi Py4E
`GET https://swapi.py4e.com/api/people/1/`
Fields: name, height, mass, hair_color, skin_color, eye_color, birth_year, gender. Limit: unknown. Fallback: `an-api-of-ice-and-fire`.

## TVMaze
`GET https://api.tvmaze.com/search/shows?q=girls`
Fields: score, show. Limit: unknown. Fallback: `shoof-aflam`.
