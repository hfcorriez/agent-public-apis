# Cryptocurrency

## Coinbase Spot
`GET https://api.coinbase.com/v2/prices/BTC-USD/spot`
Fields: data. Limit: unknown. Fallback: `coingecko`.

## CoinGecko
`GET https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd`
Fields: bitcoin. Limit: unknown. Fallback: `kraken`.

## Coinlore
`GET https://api.coinlore.net/api/ticker/?id=90`
Fields: id, symbol, name, nameid, rank, price_usd, percent_change_24h, percent_change_1h. Limit: unknown. Fallback: `coinbase`.

## Gemini Public Ticker
`GET https://api.gemini.com/v1/pubticker/btcusd`
Fields: bid, ask, last, volume. Limit: unknown. Fallback: `coinlore`.

## Kraken Public Ticker
`GET https://api.kraken.com/0/public/Ticker?pair=XBTUSD`
Fields: error, result. Limit: unknown. Fallback: `gemini`.

## Alpha (Mossland)
`GET https://alpha.moss.land/api/health`
Fields: status, service, db, seo_pages, ts, worst_status. Limit: unknown. Fallback: `coinlobster`.

## Bitcoin Halving
`GET https://why21million.com/api/halving/850000`
Fields: height, era, rewardBtc, blocksIntoEra, blocksUntilNextHalving, nextHalvingBlock, source. Limit: unknown. Fallback: `blazephoenix`.

## BlazePhoenix
`GET https://blazephoenix.xyz/api`
Fields: ok, name, version, description, endpoints, docs, sdk, contact. Limit: unknown. Fallback: `block-lottos`.

## Block Lottos
`GET https://blocklottos.com/openapi.json`
Fields: openapi, info, servers, paths, tags, externalDocs, x-blocklottos-active-contracts. Limit: unknown. Fallback: `openchainbench`. Role: spec-only.

## Blockchain Stats
`GET https://api.blockchain.com/v3/exchange/tickers/BTC-USD`
Fields: symbol, price_24h, volume_24h, last_trade_price. Limit: unknown. Fallback: `alpha-mossland`.

## Blockchain Ticker
`GET https://blockchain.info/ticker`
Fields: ARS, AUD, BRL, CAD, CHF, CLP, CNY, CZK. Limit: unknown. Fallback: `blockchain-stats`.

## btcnode.uk
`GET https://btcnode.uk/openapi.json`
Fields: openapi, info, paths. Limit: unknown. Fallback: `bitcoin-halving`. Role: spec-only.

## Coinbase Eth
`GET https://api.coinbase.com/v2/prices/ETH-USD/spot`
Fields: data. Limit: unknown. Fallback: `coinbase`.

## CoinLobster
`GET https://coinlobster.com/openapi.json`
Fields: openapi, info, servers, security, tags, components, paths. Limit: unknown. Fallback: `zennet`. Role: spec-only.

## Coinpaprika
`GET https://api.coinpaprika.com/v1/tickers/btc-bitcoin`
Fields: id, name, symbol, rank, total_supply, max_supply, beta_value, first_data_at. Limit: unknown. Fallback: `fng`.

## Fng
`GET https://api.alternative.me/fng/`
Fields: name, data, metadata. Limit: unknown. Fallback: `blockchain-ticker`.

## monerometrics
`GET https://api.monerometrics.net/openapi.json`
Fields: openapi, info, paths, components. Limit: unknown. Fallback: `vaultvision`. Role: spec-only.

## OpenChainBench
`GET https://openchainbench.com/api/openapi.json`
Fields: openapi, info, servers, paths, components. Limit: unknown. Fallback: `blazephoenix`. Role: spec-only.

## Ophis
`GET https://ophis.fi/openapi.json`
Fields: openapi, info, servers, externalDocs, paths, components. Limit: unknown. Fallback: `blazephoenix`. Role: spec-only.

## VaultVision
`GET https://vaultvision.tech/openapi.json`
Fields: openapi, info, externalDocs, servers, tags, paths, components. Limit: unknown. Fallback: `ophis`. Role: spec-only.

## Zennet
`GET https://zennet.cloud/api/markets`
Fields: assets. Limit: unknown. Fallback: `monerometrics`.
