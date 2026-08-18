# Games & Comics

## Astroworld
`GET https://api.astroworldmc.com/api/v1/mobs?search=creeper`
Fields: success, count, data. Limit: x-ratelimit-limit 100. Fallback: `yu-gi-oh`.

## Deckofcards Real
`GET https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1`
Fields: success, deck_id, remaining, shuffled. Limit: unknown. Fallback: `lichess-status`.

## Digimon Information
`GET https://digimon-api.vercel.app/api/digimon`
Fields: name, img, level. Limit: unknown. Fallback: `dungeons-and-dragons-alternate`.

## Disney
`GET https://api.disneyapi.dev/character`
Fields: info, data. Limit: unknown. Fallback: `ffxiv-collect`.

## Dungeons and Dragons
`GET https://www.dnd5eapi.co/api`
Fields: ability-scores, alignments, backgrounds, classes, conditions, damage-types, equipment, equipment-categories. Limit: x-ratelimit-limit 100. Fallback: `eight-ball`.

## Dungeons and Dragons (Alternate)
`GET https://api.open5e.com`
Fields: spells, spelllist, monsters, documents, backgrounds, planes, sections, feats. Limit: unknown. Fallback: `disney`.

## Eight Ball
`GET https://eightballapi.com/api`
Fields: reading, locale. Limit: unknown. Fallback: `rick-and-morty`.

## FFXIV Collect
`GET https://ffxivcollect.com/api/mounts/186`
Fields: id, name, description, enhanced_description, tooltip, movement, seats, custom_music. Limit: unknown. Fallback: `pok-api`.

## FreeToGame
`GET https://www.freetogame.com/api/games`
Fields: id, title, thumbnail, short_description, game_url, genre, platform, publisher. Limit: unknown. Fallback: `gamerpower`.

## GamerPower
`GET https://www.gamerpower.com/api/giveaways`
Fields: id, title, worth, thumbnail, image, description, instructions, open_giveaway_url. Limit: unknown. Fallback: `xkcd`.

## Lichess
`GET https://lichess.org/api/user/lichess`
Fields: id, username, perfs, flair, patron, patronColor, verified, createdAt. Limit: unknown. Fallback: `astroworld`.

## Lichess Status
`GET https://lichess.org/api/users/status?ids=lichess`
Fields: name, flair, patron, patronColor, id, online. Limit: unknown. Fallback: `astroworld`.

## Minecraft ServerHub
`GET https://minecraft-serverhub.com/api/ping?host=play.hypixel.net&`
Fields: online, players, version, motd, favicon, ping. Limit: unknown. Fallback: `zelda`.

## moogleAPI
`GET https://www.moogleapi.com/api/characters`
Fields: items, totalCount, page, pageSize. Limit: unknown. Fallback: `dungeons-and-dragons`.

## Pokéapi
`GET https://pokeapi.co/api/v2`
Fields: ability, berry, berry-firmness, berry-flavor, characteristic, contest-effect, contest-type, currency. Limit: unknown. Fallback: `wynncraft-2`.

## Rblxdb
`GET https://rblxdb.com/api/og?title=Roblox+API&sub=Free+JSON+data%2C+no+key+required&tag=api`
Fields: binary. Limit: unknown. Fallback: `astroworld`.

## Rick and Morty
`GET https://rickandmortyapi.com/api`
Fields: characters, locations, episodes. Limit: unknown. Fallback: `dungeons-and-dragons`.

## RuneScape
`GET https://runescape.wiki/api.php?action=rsd`
Fields: xml. Limit: unknown. Fallback: `gamerpower`.

## Wynncraft
`GET https://docs.wynncraft.com/api`
Fields: text. Limit: unknown. Fallback: `minecraft-serverhub`.

## Wynncraft
`GET https://docs.wynncraft.com/api/v2`
Fields: text. Limit: unknown. Fallback: `astroworld`.

## xkcd
`GET https://xkcd.com/info.0.json`
Fields: month, num, link, year, news, safe_title, transcript, alt. Limit: unknown. Fallback: `rblxdb`.

## Yu-Gi-Oh!
`GET https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Decode%20Talker`
Fields: data. Limit: unknown. Fallback: `freetogame`.

## Zelda
`GET https://zelda.fanapis.com/api/games?limit=2`
Fields: success, count, data. Limit: unknown. Fallback: `moogleapi`.
