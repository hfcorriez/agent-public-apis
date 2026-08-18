# Test Data

## Dog CEO
`GET https://dog.ceo/api/breeds/image/random`
Fields: message, status. Limit: unknown. Fallback: `jsonplaceholder`.

## DummyJSON
`GET https://dummyjson.com/products/1`
Fields: id, title, description, category, price, discountPercentage, rating, stock. Limit: x-ratelimit-limit 100. Fallback: `randomuser`.

## Fake Store
`GET https://fakestoreapi.com/products/1`
Fields: id, title, price, description, category, image, rating. Limit: unknown. Fallback: `dogceo`.

## httpbingo
`GET https://httpbingo.org/get`
Fields: args, headers, method, origin, url. Limit: unknown. Fallback: `fakestore`.

## JSONPlaceholder
`GET https://jsonplaceholder.typicode.com/posts/1`
Fields: userId, id, title, body. Limit: x-ratelimit-limit 1000. Fallback: `dummyjson`.

## Random User
`GET https://randomuser.me/api/?results=1`
Fields: results, info. Limit: unknown. Fallback: `httpbingo`.

## AddressMock
`GET https://addressmock.com/api/addresses?count=10&state=CA`
Fields: count, type, results, notice, docs. Limit: unknown. Fallback: `uuid-generator`.

## Bacon Ipsum
`GET https://baconipsum.com/api/?type=meat-and-filler`
Fields: json-list. Limit: unknown. Fallback: `mockae`.

## Dicebear Avatars
`GET https://api.dicebear.com/10.x/lorelei/svg?seed=Felix`
Fields: xml. Limit: unknown. Fallback: `addressmock`.

## Dogceo Breed
`GET https://dog.ceo/api/breed/hound/images/random`
Fields: message, status. Limit: unknown. Fallback: `dogceo`.

## Dummyjson User
`GET https://dummyjson.com/users/1`
Fields: id, firstName, lastName, maidenName, age, gender, email, phone. Limit: x-ratelimit-limit 100. Fallback: `dogceo-breed`.

## JSONing
`GET https://jsoning.com/wp-json/wp/v2/pages/177`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `what-the-commit`.

## Jsonplaceholder Users
`GET https://jsonplaceholder.typicode.com/users/1`
Fields: id, name, username, email, address, phone, website, company. Limit: x-ratelimit-limit 1000. Fallback: `dummyjson-user`.

## Mockae
`GET https://mockae.com/wp-json/wp/v2/pages/10`
Fields: id, date, date_gmt, guid, modified, modified_gmt, slug, status. Limit: unknown. Fallback: `jsoning`.

## restful-api
`GET https://api.restful-api.dev/objects/7`
Fields: id, name, data. Limit: unknown. Fallback: `bacon-ipsum`.

## RoboHash
`GET https://robohash.org/api`
Fields: binary. Limit: unknown. Fallback: `totalshiftleft-sandbox`.

## RoboHash
`GET https://robohash.org/api/v2`
Fields: binary. Limit: unknown. Fallback: `what-the-commit-2`.

## TotalShiftLeft Sandbox
`GET https://demo.totalshiftleft.ai/openapi.json`
Fields: openapi, info, components, paths, servers, tags, externalDocs. Limit: x-ratelimit-limit 100. Fallback: `restful-api`. Role: spec-only.

## UUID Generator
`GET https://www.uuidtools.com/api/generate/v1`
Fields: json-list. Limit: x-ratelimit-limit 60. Fallback: `robohash`.

## Uuidtools
`GET https://www.uuidtools.com/api/generate/v4`
Fields: json-list. Limit: x-ratelimit-limit 60. Fallback: `jsonplaceholder-users`.

## What The Commit
`GET https://whatthecommit.com/index.json`
Fields: hash, commit_message, permalink. Limit: unknown. Fallback: `addressmock`.

## What The Commit
`GET https://whatthecommit.com/index.txt`
Fields: text. Limit: unknown. Fallback: `yes-no`.

## Yes No
`GET https://yesno.wtf/api`
Fields: answer, forced, image. Limit: unknown. Fallback: `what-the-commit`.
