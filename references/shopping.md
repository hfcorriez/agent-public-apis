# Shopping

## CompareFairly
`GET https://comparefairly.com/llms.txt`
Fields: text. Limit: unknown. Fallback: `marketplace-fee-data`.

## Marketplace Fee Data
`GET https://www.sellerscalc.com/data/fees.json`
Fields: name, description, lastReviewed, license, attribution, disclaimer, platforms. Limit: unknown. Fallback: `comparefairly`.
