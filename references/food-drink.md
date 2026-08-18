# Food & Drink

## Brewery
`GET https://api.openbrewerydb.org/v1/breweries?per_page=1`
Fields: id, name, brewery_type, address_1, address_2, address_3, city, state_province. Limit: x-ratelimit-limit 120. Fallback: `coffee`.

## Cocktail Random
`GET https://www.thecocktaildb.com/api/json/v1/1/random.php`
Fields: drinks. Limit: unknown. Fallback: `brewery`.

## Cocktaildb
`GET https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita`
Fields: drinks. Limit: unknown. Fallback: `open-food-facts`.

## Coffee
`GET https://coffee.alexflipnote.dev/random.json`
Fields: file. Limit: unknown. Fallback: `sample-coffee`.

## Meal Random
`GET https://www.themealdb.com/api/json/v1/1/random.php`
Fields: meals. Limit: unknown. Fallback: `cocktail-random`.

## Mealdb
`GET https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata`
Fields: meals. Limit: unknown. Fallback: `cocktaildb`.

## Open Food Facts
`GET https://world.openfoodfacts.org/api/v2/product/737628064502.xml`
Fields: xml. Limit: unknown. Fallback: `whiskyhunter`.

## Sample Beers
`GET https://api.sampleapis.com/beers/ale`
Fields: price, name, rating, image, id. Limit: unknown. Fallback: `mealdb`.

## Sample Coffee
`GET https://api.sampleapis.com/coffee/hot`
Fields: title, description, ingredients, image, id. Limit: unknown. Fallback: `sample-beers`.

## WhiskyHunter
`GET https://whiskyhunter.net/api`
Fields: swagger, info, host, schemes, basePath, consumes, produces, securityDefinitions. Limit: unknown. Fallback: `open-food-facts`. Role: spec-only.
