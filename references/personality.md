# Personality

## Advice Slip
`GET https://api.adviceslip.com/advice`
Fields: slip. Limit: unknown. Fallback: `akshaykumar-rest`.

## akshaykumar-rest
`GET https://akshaykumar-rest.vercel.app/api/409`
Fields: binary. Limit: unknown. Fallback: `indian-quotes`.

## Indian Quotes
`GET https://indian-quotes-api.vercel.app/api/quotes/random`
Fields: id, quote, tags, author_id, created_at, author. Limit: x-ratelimit-limit 100. Fallback: `joke-father`.

## Joke Father
`GET https://jokefather.com/api/jokes/random`
Fields: id, setup, punchline. Limit: unknown. Fallback: `kimiquotes`.

## kimiquotes
`GET https://kimiquotes.pages.dev/api`
Fields: message. Limit: unknown. Fallback: `joke-father`.

## Personality.fyi
`GET https://personality.fyi/api/v1/types`
Fields: types, count. Limit: unknown. Fallback: `zen-quotes`.

## Quotes on Design
`GET https://quotesondesign.com/wp-json/wp/v2/pages/2333`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `zen-quotes-2`.

## Zen Quotes
`GET https://zenquotes.io/api/v2`
Fields: q, a, h. Limit: unknown. Fallback: `advice-slip`.

## Zen Quotes
`GET https://zenquotes.io/api/quotes`
Fields: q, a, c, h. Limit: unknown. Fallback: `quotes-on-design`.
