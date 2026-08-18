# Anime

## Jikan
`GET https://api.jikan.moe/v4/anime/1`
Fields: data. Limit: unknown. Fallback: `nekos`.

## Jikan Top
`GET https://api.jikan.moe/v4/top/anime?limit=1`
Fields: pagination, data. Limit: unknown. Fallback: `jikan`.

## Nekos
`GET https://nekos.best/api/v2/endpoints`
Fields: lurk, shoot, sleep, clap, shrug, stare, wave, poke. Limit: unknown. Fallback: `nekosia-api`.

## Nekos Neko
`GET https://nekos.best/api/v2/neko`
Fields: results. Limit: unknown. Fallback: `jikan-top`.

## Nekosia API
`GET https://api.sefinek.net/api/v2/moecounter/@nekosia-api-oRsj4TjLf8iq-production`
Fields: xml. Limit: unknown. Fallback: `jikan`.
