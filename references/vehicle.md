# Vehicle

## Auto Body Shop Directory
`GET https://autobodyshopnear.com/api/v1/public/shops/by-city?city=Houston&state=TX&limit=20&offset=0`
Fields: success, data. Limit: unknown. Fallback: `problemsbyvin`.

## ProblemsByVin
`GET https://problemsbyvin.com/data/catalog.json`
Fields: name, description, homepage, license, updated, update_cadence, dataset_count, datasets. Limit: unknown. Fallback: `auto-body-shop-directory`.
