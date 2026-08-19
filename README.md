# agent-public-apis

Public APIs, agent-ready — 411 verified, no keys, no signup.

A distilled, machine-verified edition of [public-apis](https://github.com/public-apis/public-apis): every entry is probed live over HTTPS, requires no API key and no registration, and ships in a format agents can use directly as a skill.

Every catalog entry is no-key, HTTPS-only, and live-verified (`verify.sh`). Spec-only rows are marked in Notes — the probe hit an OpenAPI/docs URL, not a live data endpoint.

- `SKILL.md` — index + recommended curls (drop it into your agent as a skill)
- `data/apis.json` — full verified catalog (name, endpoint, category, example, response fields, rate limits, verified-at)
- `references/` — per-category entries, loaded on demand
- `verify.sh` — re-probe the whole catalog

```bash
./verify.sh           # all catalog entries must be live
./verify.sh --refresh # re-harvest upstream lists and rebuild
```

Rules baked into every entry: no key, HTTPS only, send a User-Agent, one request then cache, use `fallback` if the primary dies.

## Catalog (39 categories, 411 APIs, 37 spec-only)

- [Animals](#animals) (7)
- [Anime](#anime) (5)
- [Art & Design](#art-design) (8)
- [Blockchain](#blockchain) (4)
- [Books](#books) (5)
- [Business](#business) (3)
- [Calendar](#calendar) (7)
- [Cryptocurrency](#cryptocurrency) (21)
- [Currency Exchange](#currency-exchange) (17)
- [Development](#development) (40)
- [Dictionaries](#dictionaries) (10)
- [Documents & Productivity](#documents-productivity) (5)
- [Email](#email) (4)
- [Entertainment](#entertainment) (23)
- [Environment](#environment) (3)
- [Finance](#finance) (6)
- [Food & Drink](#food-drink) (10)
- [Games & Comics](#games-comics) (23)
- [Geocoding](#geocoding) (28)
- [Government](#government) (22)
- [Health](#health) (8)
- [Jobs](#jobs) (5)
- [Machine Learning](#machine-learning) (5)
- [Music](#music) (2)
- [News](#news) (6)
- [Open Data](#open-data) (23)
- [Open Source Projects](#open-source-projects) (4)
- [Personality](#personality) (9)
- [Photography](#photography) (2)
- [Programming](#programming) (3)
- [Science & Math](#science-math) (22)
- [Security](#security) (5)
- [Shopping](#shopping) (2)
- [Sports & Fitness](#sports-fitness) (10)
- [Test Data](#test-data) (23)
- [Transportation](#transportation) (10)
- [Vehicle](#vehicle) (2)
- [Video](#video) (8)
- [Weather](#weather) (11)

## Animals

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Cat Facts | Random cat facts | `https://catfact.ninja/docs?api-docs.json` | spec-only |
| Cataas | Cat as a service (cats pictures and gifs) | `https://cataas.com/api/cats?tags=cute` |  |
| Catapi |  | `https://api.thecatapi.com/v1/images/search` |  |
| RandomDog | Random pictures of dogs | `https://random.dog/woof.json` |  |
| Randomfox |  | `https://randomfox.ca/floof/` |  |
| RandomFox | Random pictures of foxes | `https://randomfox.ca/floof` |  |
| xeno-canto | Bird recordings | `https://xeno-canto.org/api/3/recordings` |  |

## Anime

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Jikan |  | `https://api.jikan.moe/v4/anime/1` |  |
| Jikan Top |  | `https://api.jikan.moe/v4/top/anime?limit=1` |  |
| Nekos |  | `https://nekos.best/api/v2/endpoints` |  |
| Nekos Neko |  | `https://nekos.best/api/v2/neko` |  |
| Nekosia API | Anime API with cute random images. Dominated colors & compressed images & avoiding duplicates. | `https://api.sefinek.net/api/v2/moecounter/@nekosia-api-oRsj4TjLf8iq-production` |  |

## Art & Design

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| ColorMagic | Color Palette Generator | `https://colormagic.app/api/_payload.json?0db3f926-1e79-4c1a-8961-202cb53807e2` |  |
| DiceBear | Free avatar generation library with multiple styles | `https://api.dicebear.com/10.x/lorelei/svg?seed=Felix` |  |
| DummyImage | Generate placeholder images with custom size, colors and text | `https://dummyimage.com/v1` |  |
| DummyImage | Generate placeholder images with custom size, colors and text | `https://dummyimage.com/v2` |  |
| Icons8 | Icons (find "search icon" hyperlink in page) | `https://img.icons8.com/api` |  |
| Lordicon | Icons with predone Animations | `https://media.lordicon.com/assets/icons/main/mobile-menu.json` |  |
| Metmuseum |  | `https://collectionapi.metmuseum.org/public/collection/v1/objects/436535` |  |
| Metropolitan Museum of Art | Met Museum of Art | `https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=1` |  |

## Blockchain

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Chainpoint | Chainpoint is a global network for anchoring data to the Bitcoin blockchain | `https://tierion.com/static/d/747/path---chainpoint-860-c90-ji1aqI4kRpdvolJLtiXk7HHE.json` |  |
| ClearTrace | Cross-frontend DEX attribution and execution quality data across Ethereum and L2s | `https://cleartracedata.com/openapi.json` | spec-only |
| TWZRD Agent Intel | Solana on-chain agent trust scoring via MCP; 4 free tools to score, resolve and verify AI agent wallets | `https://intel.twzrd.xyz` |  |
| WealthVille | Liquidity pool scores and Enter/Hold/Exit verdicts for Solana and EVM chains | `https://wealthville.net/api/v1/scores/top?limit=10` |  |

## Books

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Bhagavad Gita telugu | Bhagavad Gita API in telugu and odia languages | `https://gita-api.vercel.app/openapi.json` | spec-only |
| Gutendex |  | `https://gutendex.com/books/?search=pride` |  |
| KDP Intelligence | KDP niche demand scores, competition analysis and revenue estimates | `https://kdp-intelligence-api.vercel.app/openapi.json` | spec-only |
| Open Library | Books, book covers and related data | `https://openlibrary.org/data.json` |  |
| Stephen King | The varied works and characters of the prolific author Stephen King | `https://stephen-king-api.onrender.com/api/books` |  |

## Business

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Legal Sandbox Georgia | Find verified legal specialists in Georgia from natural-language queries | `https://legal.ge/api/openapi.json` | spec-only |
| Mydentify | Startup-directory research and weekly product leaderboard data | `https://mydentify.com/openapi.json` | spec-only |
| Pick an Agency | Search 47,000+ marketing agencies by service, location and rating | `https://www.pickanagency.com/api/v1/search?service=SEO&city=Berlin&min_rating=4.5&limit=5` |  |

## Calendar

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| caldays | Public holidays for 195+ countries | `https://caldays.com/api/holidays/us` |  |
| Nager Gb |  | `https://date.nager.at/api/v3/PublicHolidays/2026/GB` |  |
| Nager.Date Holidays | Nager.Date Holidays | `https://date.nager.at/api/v3/PublicHolidays/2026/US` |  |
| Sunrise-Sunset | Sunrise-Sunset | `https://api.sunrise-sunset.org/json?lat=36.72&lng=-4.42&formatted=0` |  |
| The Calendar | Public holidays for US states and 30 countries plus sports and finance calendars as static JSON | `https://the-calendar.net/api/holidays/us-federal/2026.json` |  |
| Time API | Time API | `https://timeapi.io/api/Time/current/zone?timeZone=UTC` |  |
| UK Bank Holidays | Bank holidays in England and Wales, Scotland and Northern Ireland | `https://www.gov.uk/bank-holidays.json` |  |

## Cryptocurrency

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Alpha (Mossland) | Korean crypto channel stance + RAG Q&A + canonical entity/topic/event store | `https://alpha.moss.land/api/health` |  |
| Bitcoin Halving | Halving era, block reward, and schedule arithmetic for any Bitcoin block height | `https://why21million.com/api/halving/850000` |  |
| BlazePhoenix | On-chain DEX aggregator quotes and route execution data | `https://blazephoenix.xyz/api` |  |
| Block Lottos | On-chain lottery, draw history, jackpot and advertising endpoints | `https://blocklottos.com/openapi.json` | spec-only |
| Blockchain Stats |  | `https://api.blockchain.com/v3/exchange/tickers/BTC-USD` |  |
| Blockchain Ticker |  | `https://blockchain.info/ticker` |  |
| btcnode.uk | Bitcoin blockchain data, fees, mempool, SEC insider trades, Reddit sentiment. x402 micropayments for paid endpoints. | `https://btcnode.uk/openapi.json` | spec-only |
| Coinbase Eth |  | `https://api.coinbase.com/v2/prices/ETH-USD/spot` |  |
| Coinbase Spot | Coinbase Spot | `https://api.coinbase.com/v2/prices/BTC-USD/spot` |  |
| CoinGecko | CoinGecko | `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd` |  |
| CoinLobster | Live executed whale trades across 15 exchanges and on-chain DEX with an unusualness radar | `https://coinlobster.com/openapi.json` | spec-only |
| Coinlore | Coinlore | `https://api.coinlore.net/api/ticker/?id=90` |  |
| Coinpaprika |  | `https://api.coinpaprika.com/v1/tickers/btc-bitcoin` |  |
| Fng |  | `https://api.alternative.me/fng/` |  |
| Gemini Public Ticker | Gemini Public Ticker | `https://api.gemini.com/v1/pubticker/btcusd` |  |
| Kraken Public Ticker | Kraken Public Ticker | `https://api.kraken.com/0/public/Ticker?pair=XBTUSD` |  |
| monerometrics | Reorg-aware Monero (XMR) network metrics, mining-pool centralization and chain reorganizations | `https://api.monerometrics.net/openapi.json` | spec-only |
| OpenChainBench | Open dataset of crypto infrastructure benchmarks: RPC latency, oracles, bridges, prediction markets | `https://openchainbench.com/api/openapi.json` | spec-only |
| Ophis | Natural-language intent parser for DEX swaps across 11 EVM chains | `https://ophis.fi/openapi.json` | spec-only |
| VaultVision | Read-only Hyperliquid vault data, risk rankings, and research signals | `https://vaultvision.tech/openapi.json` | spec-only |
| Zennet | x402 pay-per-use APIs: Polymarket signals, CEX/DEX spreads, contract risk scores, gas oracle | `https://zennet.cloud/api/markets` |  |

## Currency Exchange

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Awesomeapi |  | `https://economia.awesomeapi.com.br/json/last/USD-BRL` |  |
| Cambio Uruguay | Real-time buy/sell rates from every Uruguayan exchange house, with conversion and history | `https://api.cambio-uruguay.com` |  |
| Currency API (Cloudflare Pages) | Currency API (Cloudflare Pages) | `https://latest.currency-api.pages.dev/v1/currencies/usd.json` |  |
| Currency Jsdelivr |  | `https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json` |  |
| Czech National Bank | A collection of exchange rates | `https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.xml` |  |
| Exchangerate Jsdelivr2 |  | `https://latest.currency-api.pages.dev/v1/currencies/eur.json` |  |
| Exchangerate V4 |  | `https://api.exchangerate-api.com/v4/latest/USD` |  |
| Frankfurter | Frankfurter | `https://api.frankfurter.dev/v1/latest?from=USD&to=EUR` |  |
| Frankfurter | Exchange rates, currency conversion and time series | `https://api.frankfurter.dev/v2/openapi.json` | spec-only |
| Frankfurter Gbp |  | `https://api.frankfurter.dev/v1/latest?from=GBP&to=USD` |  |
| National Bank of Poland | A collection of currency exchange rates (data in XML and JSON) | `https://api.nbp.pl/api/cenyzlota` |  |
| Nbp |  | `https://api.nbp.pl/api/exchangerates/tables/a/?format=json` |  |
| Nbp Usd |  | `https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json` |  |
| Open ExchangeRate-API | Open ExchangeRate-API | `https://open.er-api.com/v6/latest/USD` |  |
| paralelo.bo | Bolivia parallel-market USD/BOB exchange rate, aggregated from P2P sources every 60s | `https://paralelo.bo/api/openapi.json` | spec-only |
| Vatcomply |  | `https://api.vatcomply.com/rates?base=USD` |  |
| Vatcomply Eur |  | `https://api.vatcomply.com/rates?base=EUR` |  |

## Development

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| 24 Pull Requests | Project to promote open source collaboration during December | `https://24pullrequests.com/projects.json` |  |
| API Status Check | Real-time status and uptime monitoring for 270+ APIs and services | `https://apistatuscheck.com/api/badge/stripe` |  |
| CDNJS | Library info on CDNJS | `https://api.cdnjs.com/libraries/jquery` |  |
| Chess Magnus |  | `https://api.chess.com/pub/player/magnuscarlsen` |  |
| Chess.com Public | Chess.com Public | `https://api.chess.com/pub/player/hikaru` |  |
| Codex Reset | OpenAI Codex usage-limit reset history, verified announcements and 24h/48h reset probability | `https://codex-reset.com/llms.txt` |  |
| DigitalOcean Status | Status of all DigitalOcean services | `https://status.digitalocean.com/api/v2/summary.json` |  |
| DigitalOcean Status | Status of all DigitalOcean services | `https://status.digitalocean.com/index.json` |  |
| DigMyName | Domain availability and registrar pricing across 52 TLDs | `https://api.digmyname.com/functions/v1/public-api/openapi.json` | spec-only |
| DomainDb Info | Domain name search to find all domains containing particular words/phrases/etc | `https://api.domainsdb.info` |  |
| ExtendsClass JSON Storage | A simple JSON store API | `https://extendsclass.com/json-storage.openapi.json` | spec-only |
| Format JSON Online Dummy API | A free tool to generate dummy JSON data for testing and prototyping. | `https://formatjsononline.com/api/users/paginated?page=1&limit=2` |  |
| Gh Octocat Repos |  | `https://api.github.com/users/octocat/repos?per_page=1` |  |
| Git.io | Git.io URL shortener | `https://github.blog/wp-json/wp/v2/posts/31356` |  |
| GitHub Users | GitHub Users | `https://api.github.com/users/octocat` |  |
| Github Zen |  | `https://api.github.com/zen` |  |
| Hashnode | A blogging platform built for developers | `https://cdn.hashnode.com/res/hashnode/image/upload/v1724758488980/4a54c25f-34b1-43ca-ad10-2229ed7b660e.jpeg?w=100` |  |
| Hipsum | Hipster-themed lorem ipsum generator for placeholder text | `https://hipsum.co/wp-json/wp/v2/pages/5` |  |
| Httpbingo Ip |  | `https://httpbingo.org/ip` |  |
| HTTPie | a free command-line HTTP client for the API era | `https://httpie.io/api/feed/atom` |  |
| IFTTT | IFTTT Connect API | `https://platform.ifttt.com/index.json` |  |
| IPify | A simple IP Address API | `https://api.ipify.org?format=json` |  |
| IPLocate | IP geolocation and threat data API | `https://iplocate.io/api/lookup/` |  |
| IPQuery | A free IP Geolocation and proxy/tor/VPN detection API | `https://api.ipquery.io` |  |
| MyIPRightNow | Public IP address with network, location, and connection details | `https://myiprightnow.com/api/ip` |  |
| Npm Lodash |  | `https://registry.npmjs.org/lodash/latest` |  |
| npm Registry | npm Registry | `https://registry.npmjs.org/react/latest` |  |
| OutageDeck | Live status and incidents for 170+ cloud and SaaS providers from official feeds | `https://outagedeck.com/api/v1/providers?category=cloud&status=degraded&sort=severity` |  |
| Phone Specs | Real-time smartphone specifications database for 263 devices | `https://phone-specs-api-production.up.railway.app/openapi.json` | spec-only |
| Postmanecho |  | `https://postman-echo.com/get?foo=bar` |  |
| QR & Barcode | QR codes and barcodes (Code 128, EAN-13, Data Matrix, PDF417 + more). SVG or PNG output | `https://solsigs.com/openapi.json` | spec-only |
| QR code | Create an easy to read QR code and URL shortener | `https://qrtag.net/api/qr.png` |  |
| QR Code Crafter | Generate static QR codes in SVG, PNG, JPG, WebP, PDF, or EPS | `https://qrcodecrafter.com/.well-known/webmcp.json` |  |
| QuickChart | Generate chart and graph images | `https://quickchart.io/openapi.json` | spec-only |
| ReqRes | A hosted REST-API ready to respond to your AJAX requests | `https://reqres.in/api/` |  |
| Rubygems |  | `https://rubygems.org/api/v1/gems/rails.json` |  |
| Rubygems Rake |  | `https://rubygems.org/api/v1/gems/rake.json` |  |
| SQLable | CSV to JSONL conversion API | `https://sqlable.com/wp-json/wp/v2/pages/226` |  |
| TinyMind Agent Tools | Free APIs by an AI agent on a VPS: actor lookup, word-of-the-day, poems, jokes, ping | `https://tinymind.eu/api/haiku` |  |
| YAMLine | Convert YAML to JSON (on-the-fly) | `https://yamline.com/wp-json/wp/v2/pages/50` |  |

## Dictionaries

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Datamuse | Datamuse | `https://api.datamuse.com/words?rel_syn=happy&max=5` |  |
| Dict World |  | `https://api.dictionaryapi.dev/api/v2/entries/en/world` |  |
| Free Dictionary | Definitions, phonetics, pronounciations, parts of speech, examples, synonyms | `https://api.dictionaryapi.dev/api/v2/entries/en/hello` |  |
| Free Dictionary API | Free Dictionary API | `https://api.dictionaryapi.dev/api/v2/entries/en/hello` |  |
| LanguageTool languages | LanguageTool languages | `https://api.languagetool.org/v2/languages` |  |
| MyMemory Translate | MyMemory Translate | `https://api.mymemory.translated.net/get?q=Hello&langpair=en|es` |  |
| Urban |  | `https://api.urbandictionary.com/v0/define?term=api` |  |
| Urban Hello |  | `https://api.urbandictionary.com/v0/define?term=hello` |  |
| Wiktionary | Collaborative dictionary data | `https://en.wiktionary.org/w/rest.php/v1/search` |  |
| Wiktionary |  | `https://en.wiktionary.org/api/rest_v1/page/definition/hello` |  |

## Documents & Productivity

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| DocForge | Convert between Markdown, HTML, CSV, JSON, and YAML formats | `https://docforge-api.vercel.app/api` |  |
| FastApi Simple Calculator | Math, Stadistics, Conversions, Currency and more | `https://fastapi-calculadora.onrender.com/openapi.json` | spec-only |
| Kiprio PDF Text | Extract plain text from PDF documents for LLM and RAG pipelines | `https://kiprio.com/v1/pdf-text` |  |
| ReportForge | Generate styled HTML reports from CSV or JSON data with built-in templates | `https://reportforge-api.vercel.app/api` |  |
| WakaTime | Automated time tracking leaderboards for programmers | `https://wakatime.com/api/v1/editors` |  |

## Email

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| AGPC Domain Check | Check a domain's SPF, DKIM, DMARC and MX with a graded shareable report | `https://guild.tradeuniquecapital.com/api/check?domain=example.com` |  |
| mail.gw | 10 Minute Mail | `https://docs.mail.gw/_nuxt/manifest.c0c86816.json` |  |
| mail.tm | Temporary Email Service | `https://api.mail.tm` |  |
| MailCheck.ai | Prevent users to sign up with temporary email addresses | `https://api.webshot.co/EVWMY5` |  |

## Entertainment

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Chuck Norris Jokes | Chuck Norris Jokes | `https://api.chucknorris.io/jokes/random` |  |
| CosmyDay Astrology | Natal charts and sky events computed from Swiss Ephemeris | `https://api.cosmyday.com/events/upcoming?days=30&min_importance=60` |  |
| Deny By Default as a Service | Random creative rejection and acceptance reasons | `https://dbdaas.rajathjaiprakash.com/help` |  |
| Deny By Default as a Service | Random creative rejection and acceptance reasons | `https://dbdaas.rajathjaiprakash.com/api/v2` |  |
| elonmu.sh | Get random news article featuring Elon Musk | `https://elonmu.sh/api` |  |
| Hp Api |  | `https://hp-api.onrender.com/api/characters` |  |
| Imgflip | Gets an array of popular memes | `https://api.imgflip.com/get_memes` |  |
| JokeAPI | JokeAPI | `https://v2.jokeapi.dev/joke/Programming?type=single` |  |
| JokeAPI | Jokes in multiple formats | `https://v2.jokeapi.dev/languages?format=txt` |  |
| justmeme.wtf | Free meme API with 2400+ templates, search, trending, and AI generation | `https://justmeme.wtf/api/v1/templates` |  |
| Kanye |  | `https://api.kanye.rest/` |  |
| Memesio | Meme creation API with templates, editable captions and hosted share links | `https://memesio.com/api/free/templates?q=friday+deploy&pageSize=10&mode=hybrid&mediaType=all` |  |
| Official Ten |  | `https://official-joke-api.appspot.com/jokes/ten` |  |
| Officialjoke |  | `https://official-joke-api.appspot.com/random_joke` |  |
| Opentdb |  | `https://opentdb.com/api.php?amount=1` |  |
| Pokeapi Berry |  | `https://pokeapi.co/api/v2/berry/1` |  |
| PokéAPI | PokéAPI | `https://pokeapi.co/api/v2/pokemon/ditto` |  |
| Rick and Morty | Rick and Morty | `https://rickandmortyapi.com/api/character/1` |  |
| Rickmorty Loc |  | `https://rickandmortyapi.com/api/location/1` |  |
| Sample Movies |  | `https://api.sampleapis.com/movies/animation` |  |
| TVmaze | TVmaze | `https://api.tvmaze.com/shows/1` |  |
| Useless Today |  | `https://uselessfacts.jsph.pl/api/v2/facts/today` |  |
| Uselessfacts |  | `https://uselessfacts.jsph.pl/api/v2/facts/random` |  |

## Environment

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Luchtmeetnet | Predicted and actual air quality components for The Netherlands (RIVM) | `https://api-docs.luchtmeetnet.nl/view/metadata/SVmsWg5g` |  |
| UK Carbon Intensity | The Official Carbon Intensity API for Great Britain developed by National Grid | `https://api.carbonintensity.org.uk/intensity` |  |
| Website Carbon | API to estimate the carbon footprint of loading web pages | `https://api.websitecarbon.com/data?bytes=12345678&green=1` |  |

## Finance

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| AlQANAAS Gold Data | Live XAUUSD, country gold prices, and weekly gold research in JSON and CSV | `https://alqanaas.com/gold-data.json` |  |
| Casheva | Financial data for Argentina, Spain and Mexico: USD rates, inflation, Euribor, ICL | `https://casheva.com/api/v1/dolar` |  |
| DolarAPI | Real-time exchange rates for Latin American currencies | `https://api.argentinadatos.com/static/assets/arq/Desktop_banner_10.png` |  |
| Econdb | Global macroeconomic data | `https://www.econdb.com/api` |  |
| Top 5 Stocks | Daily AI-ranked stock and crypto watchlists | `https://top5stocks.netlify.app/api/v1/openapi.json` | spec-only |
| Zelothorn | Plain-English explanations of US public companies with SEC filings and earnings data | `https://zelothorn.com/api/v1/company/AAPL` |  |

## Food & Drink

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Brewery |  | `https://api.openbrewerydb.org/v1/breweries?per_page=1` |  |
| Cocktail Random |  | `https://www.thecocktaildb.com/api/json/v1/1/random.php` |  |
| Cocktaildb |  | `https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita` |  |
| Coffee |  | `https://coffee.alexflipnote.dev/random.json` |  |
| Meal Random |  | `https://www.themealdb.com/api/json/v1/1/random.php` |  |
| Mealdb |  | `https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata` |  |
| Open Food Facts | Food Products Database | `https://world.openfoodfacts.org/api/v2/product/737628064502.xml` |  |
| Sample Beers |  | `https://api.sampleapis.com/beers/ale` |  |
| Sample Coffee |  | `https://api.sampleapis.com/coffee/hot` |  |
| WhiskyHunter | Past online whisky auctions statistical data | `https://whiskyhunter.net/api` | spec-only |

## Games & Comics

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Astroworld | Free Minecraft data: mobs, biomes, items, enchantments, structures, commands, versions, achievements, trades | `https://api.astroworldmc.com/api/v1/mobs?search=creeper` |  |
| Deckofcards Real |  | `https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1` |  |
| Digimon Information | Provides information about digimon creatures | `https://digimon-api.vercel.app/api/digimon` |  |
| Disney | Information of Disney characters | `https://api.disneyapi.dev/character` |  |
| Dungeons and Dragons | Reference for 5th edition spells, classes, monsters, and more | `https://www.dnd5eapi.co/api` |  |
| Dungeons and Dragons (Alternate) | Includes all monsters and spells from the SRD (System Reference Document) as well as a search API | `https://api.open5e.com` |  |
| Eight Ball | Fortune-telling API with random, sentiment-biased, and multi-language responses | `https://eightballapi.com/api` |  |
| FFXIV Collect | Final Fantasy XIV data on collectables | `https://ffxivcollect.com/api/mounts/186` |  |
| FreeToGame | Free-To-Play Games Database | `https://www.freetogame.com/api/games` |  |
| GamerPower | Game Giveaways Tracker | `https://www.gamerpower.com/api/giveaways` |  |
| Lichess |  | `https://lichess.org/api/user/lichess` |  |
| Lichess Status |  | `https://lichess.org/api/users/status?ids=lichess` |  |
| Minecraft ServerHub | Minecraft server status, player counts, MOTD, and live status badges | `https://minecraft-serverhub.com/api/ping?host=play.hypixel.net&` |  |
| moogleAPI | Final Fantasy franchise data | `https://www.moogleapi.com/api/characters` |  |
| Pokéapi | Pokémon Information | `https://pokeapi.co/api/v2` |  |
| Rblxdb | Verified Roblox music codes and decal IDs with live working status | `https://rblxdb.com/api/og?title=Roblox+API&sub=Free+JSON+data%2C+no+key+required&tag=api` |  |
| Rick and Morty | All the Rick and Morty information, including images | `https://rickandmortyapi.com/api` |  |
| RuneScape | RuneScape and OSRS RPGs information | `https://runescape.wiki/api.php?action=rsd` |  |
| Wynncraft | Wynncraft Information | `https://docs.wynncraft.com/api` |  |
| Wynncraft | Wynncraft Information | `https://docs.wynncraft.com/api/v2` |  |
| xkcd | Retrieve xkcd comics as JSON | `https://xkcd.com/info.0.json` |  |
| Yu-Gi-Oh! | Yu-Gi-Oh! TCG Information | `https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Decode%20Talker` |  |
| Zelda | The Legend of Zelda franchise data | `https://zelda.fanapis.com/api/games?limit=2` |  |

## Geocoding

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| BdAPIs | Get divisions, districts, and upazzilas of Bangladesh | `https://bdapis.com/api/v2` |  |
| BdAPIs | Get divisions, districts, and upazzilas of Bangladesh | `https://bdapis.com/api` |  |
| Cep.la | Brazil RESTful API to find information about streets, zip codes, neighborhoods, cities and states | `https://cep.la/wp-json/wp/v2/pages/21` |  |
| Country | Get your visitor's country from their IP | `https://api.country.is/openapi.json` | spec-only |
| country.is | country.is | `https://api.country.is/` |  |
| Ducks Unlimited | API explorer that gives a query URL with a JSON response of locations and cities | `https://gis.ducks.org/data.json` |  |
| Freeipapi |  | `https://freeipapi.com/api/json` |  |
| geoJS | geoJS | `https://get.geojs.io/v1/ip/geo.json` |  |
| Geojs Ip |  | `https://get.geojs.io/v1/ip.json` |  |
| HackMyIP | IP geolocation, ISP and privacy/VPN scoring, email breach checks, DNS and WHOIS lookups | `https://hackmyip.com/api/ip` |  |
| Ifconfig |  | `https://ifconfig.co/json` |  |
| IP Address Details | Find geolocation with ip address | `https://ipinfo.io` |  |
| ip.app | IP, ASN, geolocation, timezone, security, user-agent in plain text, JSON or HTTP headers | `https://ip.app` |  |
| Ipapi Co |  | `https://ipapi.co/json/` |  |
| IPGEO | Unlimited free IP Address API with useful information | `https://api.techniknews.net/ipgeo` |  |
| Ipguide |  | `https://ip.guide/` |  |
| ipify | ipify | `https://api.ipify.org?format=json` |  |
| Ipify V6 |  | `https://api64.ipify.org?format=json` |  |
| ipwho.is | ipwho.is | `https://ipwho.is/` |  |
| LatLng | Geocoding, reverse geocoding, places, and static maps | `https://api.latlng.work/api?q=Seattle,WA` |  |
| Nominatim |  | `https://nominatim.openstreetmap.org/search?q=London&format=json&limit=1` |  |
| Open Topo Data | Elevation and ocean depth for a latitude and longitude | `https://api.opentopodata.org/v1/test-dataset?locations=56,123` |  |
| Open-Meteo Geocoding | Open-Meteo Geocoding | `https://geocoding-api.open-meteo.com/v1/search?name=Berlin&count=1` |  |
| PostalCodes | Postal code search, country exports, and address validation data | `https://postalcodes.info/openapi.json` | spec-only |
| Postali | Mexico Zip Codes API | `https://postali.app/api/v1/mx/cp/06700` |  |
| REST Countries | Get information about countries via a RESTful API | `https://static-03.restcountries.com/rest-countries/static/images/clients/v1/apple-icon.png` |  |
| Zip Nyc |  | `https://api.zippopotam.us/us/10001` |  |
| Zippopotam | Zippopotam | `https://api.zippopotam.us/us/90210` |  |

## Government

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Api Colombia | Community driven API for Colombia Public Data | `https://api-colombia.com/api/v1/Country/Colombia` |  |
| Bank Negara Malaysia Open Data | Malaysia Central Bank Open Data | `https://api.bnm.gov.my/api/specification/categories` |  |
| Brazil Central Bank Open Data | Brazil Central Bank Open Data | `https://dadosabertos.bcb.gov.br/api` |  |
| Brazil CNPJ | Query Brazilian companies by CNPJ with full Receita Federal registry data, no key required | `https://api.cnpj.wiki/v1/cnpj/00000000000191` |  |
| Brazilian Chamber of Deputies Open Data | Provides legislative information in Apis XML and JSON, as well as files in various formats | `https://dadosabertos.camara.leg.br/api/v2/api-docs` | spec-only |
| City, Gdańsk | Gdańsk (PL) City Open Data | `https://ckan.multimediagdansk.pl/api` |  |
| City, Gdynia | Gdynia (PL) City Open Data | `https://otwartedane.gdynia.pl/api` |  |
| City, New York Open Data | New York (US) City Open Data | `https://opendata.cityofnewyork.us/wp-json/wp/v2/pages/40` |  |
| City, Toronto Open Data | Toronto (CA) City Open Data | `https://open.toronto.ca/wp-json/wp/v2/pages/2` |  |
| Indian Mandi Prices | Free, keyless daily wholesale mandi prices for 5 Indian states, sourced from data.gov.in | `https://mandi-api.onrender.com/v1` |  |
| Istanbul (İBB) Open Data | Data sets from the İstanbul Metropolitan Municipality (İBB) | `https://data.ibb.gov.tr/api` |  |
| Neotimo DGFiP Mirror | French DGFiP registry of certified e-invoicing platforms (Plateformes Agréées), searchable by SIRET | `https://neotimo.com/api/v1/neotimo/annuaire/routing/80438439400016` |  |
| Open Government, Argentina | Argentina Government Open Data | `https://datos.gob.ar/api` |  |
| Open Government, Indonesia | Indonesian Government Open Data | `https://data.go.id/api/minio/news?file=backend/1786336057772-DTI-CX.jpg` |  |
| Open Government, Ireland | Ireland Government Open Data | `https://data.gov.ie/api` |  |
| Open Government, Lithuania | Lithuania Government Open Data | `https://data.gov.lt/partner/api/1/` | spec-only |
| Open Government, Queensland Government | Queensland Government Open Data | `https://www.data.qld.gov.au/api` |  |
| Open Government, Spain | Spain Government Open Data | `https://datos.gob.es/api` |  |
| Open Government, Switzerland | Switzerland Government Open Data | `https://opendata.swiss/api/3/action/package_search?fq=tags:economy` |  |
| OpenMercantil | Spanish company public data and BORME event timelines | `https://openmercantil.es/api/v1/search?q=mercadona&limit=5` |  |
| Tollmint | Advertising, subscription, AI-disclosure and accessibility rules across the US, EU and UK | `https://api.tollmint.com` |  |
| USPTO | USA patent api services | `https://www.uspto.gov/data.json` |  |

## Health

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Covid Tracking Project | Covid-19  data for the US | `https://api.covidtracking.com/v2/us/daily/2021-01-02.json` |  |
| Humanitarian Data Exchange | Humanitarian Data Exchange (HDX) is open platform for sharing data across crises and organisations | `https://data.humdata.org/api` |  |
| Makeup | Makeup Information | `https://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush` |  |
| MedlinePlus Genetics | Genetic conditions, genes, chromosomes and mtDNA data | `https://medlineplus.gov/download/genetics/condition/alzheimer-disease.json` |  |
| NPPES | National Plan & Provider Enumeration System, info on healthcare providers registered in US | `https://npiregistry.cms.hhs.gov/api` |  |
| Open Data NHS Scotland | Medical reference data and statistics by Public Health Scotland | `https://www.opendata.nhs.scot/api` |  |
| Psychologie et Sérénité | French psychology articles metadata and validated psychological tests catalog | `https://psychologieetserenite.com/api/v1/openapi.json` | spec-only |
| Verified Supplement Data | Supplement dosing, form comparisons and drug-nutrient interactions with PubMed citations | `https://verifiedsupplementdata.com/api/v1/recommend/index.json` |  |

## Jobs

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| AI Dev Jobs | AI/ML engineering job aggregator with REST, RSS, and MCP endpoints | `https://aidevboard.com/api/v1` |  |
| Artificial Intelligence Jobs | Live AI/ML job listings from 260+ companies' own career pages, with salary, location, remote and seniority filters | `https://artificialintelligencejobs.co/api/jobs` |  |
| DevITjobs UK | Jobs with GraphQL | `https://devitjobs.uk/job_feed.xml` |  |
| Himalayas | Remote job listings with salary, timezone, and location data | `https://himalayas.app/jobs/api` |  |
| TechRole Index | Russian IT profession, vacancy publication and salary aggregates | `https://techrole.ru/open-data-daily.csv-metadata.json` |  |

## Machine Learning

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| AI Economics Tools | Token cost, LLM energy, agent-hour and Proof-Adjusted Autonomy calculators by Michał Piszczek | `https://piszczek.pl/tools/api` | spec-only |
| DreamThreads | Parse dreams into structured entities, emotions, agency, threat, and outcomes | `https://mydreamthreads.xyz/dream-interpretation-api/openapi.json` | spec-only |
| Not Human Search | AI tool discovery with agentic scoring for 8,600+ tools and MCP servers | `https://nothumansearch.ai/api/v1` |  |
| Statlyte | Live pricing, context windows and model ids for major LLM APIs | `https://statlyte.com/api/v1/models` |  |
| TensorFeed | Real-time AI news, model pricing, service status, and agent activity feeds | `https://tensorfeed.ai/api/agents/news` |  |

## Music

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Genrenator | Music genre generator | `https://binaryjazz.us/wp-json/wp/v2/pages/182` |  |
| Musicbrainz |  | `https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json` |  |

## News

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| DEV.to | DEV.to | `https://dev.to/api/articles?per_page=1` |  |
| HN Algolia | HN Algolia | `https://hn.algolia.com/api/v1/search?query=ai&hitsPerPage=1` |  |
| Lobsters | Lobsters | `https://lobste.rs/hottest.json` |  |
| Lobsters Newest |  | `https://lobste.rs/newest.json` |  |
| Noozra | Free news headlines from 200+ curated RSS sources | `https://noozra.com/api/articles?category=tech&limit=5` |  |
| Spaceflight News | Spaceflight News | `https://api.spaceflightnewsapi.net/v4/articles/?limit=1` |  |

## Open Data

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| API Setu | An Indian Government platform that provides a lot of APIS for KYC, business, education & employment | `https://apisetu.gov.in/apisetu_logo.png` |  |
| ArgentinaDatos | Unofficial Argentinian data API | `https://api.argentinadatos.com/static/logos/bcra.png` |  |
| BotsArchive | JSON formatted details about Telegram Bots available in database | `https://api.botsarchive.com/getBotID.php` |  |
| College ROI | Lifetime ROI of US colleges and majors, static JSON, CC BY 4.0 | `https://le-teen.com/og/api.png` |  |
| CollegeScoreCard.ed.gov | Data on higher education institutions in the United States | `https://collegescorecard.ed.gov/data/_payload.json?d2847bd9-1fde-4288-9b9e-4097fbc6d9e1` |  |
| Dimdom | Polish real estate listings, agency profiles and TERYT geographic data | `https://api.dimdom.pl` |  |
| EOSL | Hardware end-of-sale and end-of-service-life dates by part number, source-linked | `https://eosl.ai/og/api.png` |  |
| i6eal Open AI Data | Open datasets on AI policy, regulation and public-sector adoption in Germany and the EU | `https://i6eal.de/data/catalog/dcat.jsonld` |  |
| InfraNode | Unified German city open data: weather, air quality, EV chargers, transit, demographics | `https://infranode.dev/api/v1/cities/berlin/weather` |  |
| LottoLens PH | Fixed Philippine PCSO historical results and normal draw schedules | `https://remo65588-boop.github.io/lottolens-ph-public-data/api/v1/metadata.json` |  |
| ModelPartFinder Error Codes | Lookup appliance and equipment error codes by brand and code, with recommended replacement parts | `https://modelpartfinder.com/api/v1/error-code/Whirlpool/F01` |  |
| Nobel Prize | Open data about nobel prizes and events | `https://api.nobelprize.org/2.1/laureates` |  |
| Onyx Bazaar | Free public leaderboard of x402 paid HTTP services indexed from Coinbase CDP discovery API | `https://onyx-actions.onrender.com/bazaar` |  |
| Onyx Bazaar | Free public leaderboard of x402 paid HTTP services indexed from Coinbase CDP discovery API | `https://onyx-actions.onrender.com/index.json` |  |
| Open Scholarships | Free, openly-licensed directory of US scholarships and student aid from official sources | `https://scholarships.grudged.io/scholarships.json` |  |
| OpenSanctions | Data on international sanctions, crime and politically exposed persons | `https://api.opensanctions.org/openapi.json` | spec-only |
| Sofiaplan | Access to urban research data for the Bulgarian capital Sofia | `https://sofiaplan.bg/wp-json/wp/v2/pages/7258` |  |
| Statistics of the World | Economic data for 218 countries — GDP, population, inflation, and 440+ indicators from IMF and World Bank | `https://statisticsoftheworld.com/api/v1/countries` |  |
| Tilth | Free daily UK fertiliser price index across nine grades, CC BY 4.0 licensed | `https://www.tilth.uk/api/v1/public/fertiliser/dataset?product=AN_UK` |  |
| Umeå Open Data | Open data of the city Umeå in northen Sweden | `https://opendata.umea.se/api/v2` |  |
| Voidly | Internet censorship measurements, incidents, and ISP-level blocking data across 126 countries | `https://voidly.ai/.well-known/agent-card.json` |  |
| Warnely | Composite travel-safety scores for 180 countries (FCDO + US State + GPI + WGI + live incident wire), OpenAPI 3.1 spec, CC BY 4.0 | `https://www.warnely.com/api/v1/countries` |  |
| Wikipedia | Mediawiki Encyclopedia | `https://www.mediawiki.org/w/rest.php/v1/search` |  |

## Open Source Projects

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Datamuse | Word-finding query engine | `https://api.datamuse.com/metrics` |  |
| Drupal.org | Drupal.org | `https://www.drupal.org/api-d7/node/2773581.json` |  |
| Shields | Concise, consistent, and legible badges in SVG and raster format | `https://shields.io/api` |  |
| Shields | Concise, consistent, and legible badges in SVG and raster format | `https://shields.io/api/v2` |  |

## Personality

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Advice Slip | Generate random advice slips | `https://api.adviceslip.com/advice` |  |
| akshaykumar-rest | Akshay Kumar for every HTTP status code | `https://akshaykumar-rest.vercel.app/api/409` |  |
| Indian Quotes | Curated quotes from India's most successful entrepreneurs | `https://indian-quotes-api.vercel.app/api/quotes/random` |  |
| Joke Father | Ultimate collection of dad jokes | `https://jokefather.com/api/jokes/random` |  |
| kimiquotes | Team radio and interview quotes by Finnish F1 legend Kimi Räikkönen | `https://kimiquotes.pages.dev/api` |  |
| Personality.fyi | Free MBTI personality types and OEJTS test scoring | `https://personality.fyi/api/v1/types` |  |
| Quotes on Design | Inspirational Quotes | `https://quotesondesign.com/wp-json/wp/v2/pages/2333` |  |
| Zen Quotes | Large collection of Zen quotes for inspiration | `https://zenquotes.io/api/v2` |  |
| Zen Quotes | Large collection of Zen quotes for inspiration | `https://zenquotes.io/api/quotes` |  |

## Photography

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Lorem Picsum | Images from Unsplash | `https://picsum.photos/v2/list` |  |
| ReSmush.it | Photo optimization | `https://resmush.it/wp-json/wp/v2/pages/9` |  |

## Programming

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| PHPhub | PHP syntax checker | `https://phphub.net/wp-json/wp/v2/pages/18` |  |
| Pythonium | Validate Python code syntax | `https://pythonium.net/wp-json/wp/v2/pages/13` |  |
| Softwium | Validate SQL queries | `https://softwium.com/wp-json/wp/v2/pages/175` |  |

## Science & Math

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Art Institute of Chicago | Art Institute of Chicago | `https://api.artic.edu/api/v1/artworks/129884?fields=id,title,artist_display` |  |
| Artic List |  | `https://api.artic.edu/api/v1/artworks?limit=1` |  |
| Crossref |  | `https://api.crossref.org/works?query=climate&rows=1` |  |
| Crossref Doi |  | `https://api.crossref.org/works/10.1037/0003-066X.59.1.29` |  |
| CycleCalcs | Interpreted astronomy: sun and moon times, moon phases, planets, eclipses, seasons | `https://www.cyclecalcs.com/v2` |  |
| GBIF Species Match | GBIF Species Match | `https://api.gbif.org/v1/species/match?name=Puma%20concolor` |  |
| Gbif Tiger |  | `https://api.gbif.org/v1/species/match?name=Panthera%20tigris` |  |
| isEven (humor) | Check if a number is even | `https://api.isevenapi.xyz/api/iseven/6/` |  |
| ISRO | ISRO Space Crafts Information | `https://isro.vercel.app/api/spacecrafts` |  |
| Moonlora | Moon phases, illumination, moon signs, full/new moon dates (1900–2100), moonrise/moonset by coordinates | `https://moonlora.com/api/v1/phase?date=1969-07-20` |  |
| Open Library Search | Open Library Search | `https://openlibrary.org/search.json?q=dune&limit=1` |  |
| openFDA Drug Labels | openFDA Drug Labels | `https://api.fda.gov/drug/label.json?limit=1` |  |
| Openfda Food |  | `https://api.fda.gov/food/enforcement.json?limit=1` |  |
| Satellite Passes | Find satellite passes | `https://sat.terrestre.ar/openapi.json` | spec-only |
| SHARE | A free, open, dataset about research and scholarly activities | `https://share.osf.io/api/v2` |  |
| Sunrise and Sunset | Sunset and sunrise times for a given latitude and longitude | `https://api.sunrise-sunset.org/v2?lat=36.7201600&lng=-4.4203400` |  |
| Tallytopia | Calculators for finance, health, math, space and sports with step-by-step results | `https://tallytopia.com/api/v1/calculate/mortgage-payment?principal=300000&annualRate=7&years=30` |  |
| UK Carbon Intensity | UK Carbon Intensity | `https://api.carbonintensity.org.uk/intensity` |  |
| Usgs Day |  | `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson` |  |
| USGS Earthquakes | USGS Earthquakes | `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson` |  |
| Wiki Moon |  | `https://en.wikipedia.org/api/rest_v1/page/summary/Moon` |  |
| Wikipedia REST Summary | Wikipedia REST Summary | `https://en.wikipedia.org/api/rest_v1/page/summary/Earth` |  |

## Security

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| ChronoVerify | Image capture time and provenance verification: C2PA Content Credentials, EXIF, pixel forensics | `https://chronoverify.com/openapi.json` | spec-only |
| dead-drop | Ephemeral zero-knowledge encrypted data sharing | `https://api.dead-drop.xyz/api/v1/docs/openapi.json` | spec-only |
| Defend Network | Free no-auth JSON feed of exploited CVEs with CVSS, EPSS and CISA KEV status | `https://defend.network/api/v1/cves/latest.json` |  |
| PhishStats | Phishing database | `https://api.phishstats.info/api/phishing` |  |
| ScanMalware | Scan URLs in a sandboxed browser and search past scans by domain, IP, ASN, JARM or favicon hash | `https://scanmalware.com/api/v1/rss` |  |

## Shopping

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| CompareFairly | Neutral, sourced comparisons of products and services across any category, localized by language and country; per-criterion values, sub-scores and the source link behind each value | `https://comparefairly.com/llms.txt` |  |
| Marketplace Fee Data | Seller fee schedules for 21 e-commerce marketplaces and payment processors as JSON | `https://www.sellerscalc.com/data/fees.json` |  |

## Sports & Fitness

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| DiscGolf | Structured disc golf course data | `https://io.discgolfapi.com/v1/courses?country=GB&limit=5` |  |
| F1 API | Open F1 API with realtime data | `https://f1api.dev/api/2026/11/race` |  |
| Football (Soccer) Videos | Embed codes for goals and highlights from Premier League, Bundesliga, Serie A and many more | `https://www.scorebat.com/api` |  |
| Football (Soccer) Videos | Embed codes for goals and highlights from Premier League, Bundesliga, Serie A and many more | `https://www.scorebat.com/api/v2` |  |
| OpenF1 | Real-time and historical Formula 1 data including laps, car telemetry and positions | `https://api.openf1.org` |  |
| OpenLigaDB | Crowd sourced sports league results | `https://api.openligadb.de/getmatchdata/bl1/2020/1` |  |
| Racing Alpha | AI win-probability scores, fair prices and draw-bias stats for UK & Irish horse racing | `https://racingalpha.co.uk/api/v1/today` |  |
| SportScore | Live scores, fixtures, standings and stats for football, basketball, cricket and tennis | `https://sportscore.com/api/widget/matches/?sport=football&limit=10` |  |
| Squiggle | Fixtures, results and predictions for Australian Football League matches | `https://api.squiggle.com.au/?q=teams` |  |
| TourneyRadar | Upcoming chess tournaments from 140+ national federations worldwide | `https://tourneyradar-api.vercel.app` |  |

## Test Data

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| AddressMock | Random US, Hong Kong and Cape Verde addresses with matched city, state and ZIP | `https://addressmock.com/api/addresses?count=10&state=CA` |  |
| Bacon Ipsum | A Meatier Lorem Ipsum Generator | `https://baconipsum.com/api/?type=meat-and-filler` |  |
| Dicebear Avatars | Generate random pixel-art avatars | `https://api.dicebear.com/10.x/lorelei/svg?seed=Felix` |  |
| Dog CEO | Dog CEO | `https://dog.ceo/api/breeds/image/random` |  |
| Dogceo Breed |  | `https://dog.ceo/api/breed/hound/images/random` |  |
| DummyJSON | DummyJSON | `https://dummyjson.com/products/1` |  |
| Dummyjson User |  | `https://dummyjson.com/users/1` |  |
| Fake Store | Fake Store | `https://fakestoreapi.com/products/1` |  |
| httpbingo | httpbingo | `https://httpbingo.org/get` |  |
| JSONing | Fake REST API for prototyping | `https://jsoning.com/wp-json/wp/v2/pages/177` |  |
| JSONPlaceholder | JSONPlaceholder | `https://jsonplaceholder.typicode.com/posts/1` |  |
| Jsonplaceholder Users |  | `https://jsonplaceholder.typicode.com/users/1` |  |
| Mockae | Fake REST API powered by Lua | `https://mockae.com/wp-json/wp/v2/pages/10` |  |
| Random User | Random User | `https://randomuser.me/api/?results=1` |  |
| restful-api | Fake REST API for testing and prototyping with CRUD endpoints | `https://api.restful-api.dev/objects/7` |  |
| RoboHash | Generate random robot/alien avatars | `https://robohash.org/api` |  |
| RoboHash | Generate random robot/alien avatars | `https://robohash.org/api/v2` |  |
| TotalShiftLeft Sandbox | Free multi-protocol sandbox: REST, GraphQL & SOAP with OAuth2/JWT auth and OpenAPI 3.0 spec | `https://demo.totalshiftleft.ai/openapi.json` | spec-only |
| UUID Generator | Generate UUIDs | `https://www.uuidtools.com/api/generate/v1` |  |
| Uuidtools |  | `https://www.uuidtools.com/api/generate/v4` |  |
| What The Commit | Random commit message generator | `https://whatthecommit.com/index.json` |  |
| What The Commit | Random commit message generator | `https://whatthecommit.com/index.txt` |  |
| Yes No | Generate yes or no randomly | `https://yesno.wtf/api` |  |

## Transportation

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| ADS-B Exchange | Access real-time and historical data of any and all airborne aircraft | `https://www.adsbexchange.com/wp-json/wp/v2/pages/443` |  |
| BC Ferries | Sailing times and capacities for BC Ferries | `https://www.bcferriesapi.ca/api` |  |
| BC Ferries | Sailing times and capacities for BC Ferries | `https://www.bcferriesapi.ca/v2` |  |
| Can I enter | Visa and entry requirements for 199 passports, cited to official sources, verified daily | `https://canienter.com/openapi.json` | spec-only |
| OpenVan | Fuel prices for 121 countries, food cost index & vanlife weather scores for RV travel | `https://openvan.camp/docs.openapi` |  |
| Strait of Hormuz Ship Monitor | Live AIS vessel traffic, crossings and oil flow through the Strait of Hormuz | `https://hormuz.data-tracking.net/llms.txt` |  |
| Transport for Los Angeles, US | Data about positions of Metro vehicles in real time and travel their routes | `https://developer.metro.net/wp-json/wp/v2/pages/6` |  |
| Transport for Paris, France | RATP Open Data API | `https://data.ratp.fr/api/v2` |  |
| Transport for Switzerland | Swiss public transport API | `https://transport.opendata.ch/v1` |  |
| Transport for Toronto, Canada | TTC | `https://myttc.ca/finch_station.json` |  |

## Vehicle

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Auto Body Shop Directory | Find auto body shops by ZIP code, city, location, or profile | `https://autobodyshopnear.com/api/v1/public/shops/by-city?city=Houston&state=TX&limit=20&offset=0` |  |
| ProblemsByVin | Owner complaints, recalls and failure-mileage statistics by vehicle make, model and year | `https://problemsbyvin.com/data/catalog.json` |  |

## Video

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| An API of Ice And Fire | Game Of Thrones API | `https://anapioficeandfire.com/api` |  |
| Final Space | Final Space API | `https://finalspaceapi.com/api/v0/` |  |
| Iceandfire Book |  | `https://anapioficeandfire.com/api/books/1` |  |
| Shoof Aflam | Arabic streaming guide — search 14,000+ movies/series, platform availability across 18 services | `https://shoofaflam.tv/api/platforms.json` |  |
| SWAPI | All the Star Wars data you've ever wanted | `https://swapi.dev/api/` |  |
| SWAPI | All things Star Wars | `https://www.swapi.tech/api` |  |
| Swapi Py4E |  | `https://swapi.py4e.com/api/people/1/` |  |
| TVMaze | TV Show Data | `https://api.tvmaze.com/search/shows?q=girls` |  |

## Weather

| Name | Purpose | Endpoint | Notes |
| --- | --- | --- | --- |
| Hail History | Radar-detected hail history for any US address from NOAA NEXRAD Level-III hail detections, by year | `https://hail-history-noaa.netlify.app/api` |  |
| MET Norway | MET Norway | `https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.10&lon=9.58` |  |
| Open-Meteo | Open-Meteo | `https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true` |  |
| Open-Meteo Air Quality | Open-Meteo Air Quality | `https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&current=us_aqi` |  |
| Openmeteo Marine |  | `https://marine-api.open-meteo.com/v1/marine?latitude=54.32&longitude=10.15&current=wave_height` |  |
| openSenseMap | Data from Personal Weather Stations called senseBoxes | `https://api.opensensemap.org` |  |
| RainViewer | Radar data collected from different websites across the Internet | `https://www.rainviewer.com/.well-known/api-catalog` |  |
| US Weather | US National Weather Service | `https://api.weather.gov/openapi.json` | spec-only |
| World Time & Weather | Current weather, local time, UTC offset and DST rules for 400 cities as static JSON | `https://worldtimeweather.com/api/v1/cities.json` |  |
| wttr.in | wttr.in | `https://wttr.in/London?format=j1` |  |
| wttr.in | Weather in your terminal, supports JSON output | `https://wttr.in/index.json` |  |

## Sources

Distilled from [public-apis/public-apis](https://github.com/public-apis/public-apis) and [marcelscruz/public-apis](https://github.com/marcelscruz/public-apis), with OpenAPI structure hints from [apis.guru](https://apis.guru). Only entries that pass live verification are included.

## License

MIT
