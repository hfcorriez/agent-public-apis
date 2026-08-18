# Dictionaries

## Datamuse
`GET https://api.datamuse.com/words?rel_syn=happy&max=5`
Fields: word, score. Limit: unknown. Fallback: `mymemory`.

## Free Dictionary API
`GET https://api.dictionaryapi.dev/api/v2/entries/en/hello`
Fields: word, phonetics, meanings, license, sourceUrls. Limit: x-ratelimit-limit 450. Fallback: `datamuse`.

## LanguageTool languages
`GET https://api.languagetool.org/v2/languages`
Fields: name, code, longCode. Limit: unknown. Fallback: `dictionaryapi`.

## MyMemory Translate
`GET https://api.mymemory.translated.net/get?q=Hello&langpair=en|es`
Fields: responseData, quotaFinished, mtLangSupported, responseDetails, responseStatus, responderId, exception_code, matches. Limit: unknown. Fallback: `languagetool`.

## Dict World
`GET https://api.dictionaryapi.dev/api/v2/entries/en/world`
Fields: word, phonetic, phonetics, meanings, license, sourceUrls. Limit: x-ratelimit-limit 450. Fallback: `urban-hello`.

## Free Dictionary
`GET https://api.dictionaryapi.dev/api/v2/entries/en/hello`
Fields: word, phonetics, meanings, license, sourceUrls. Limit: x-ratelimit-limit 450. Fallback: `wiktionary`.

## Urban
`GET https://api.urbandictionary.com/v0/define?term=api`
Fields: list. Limit: unknown. Fallback: `wiktionary-2`.

## Urban Hello
`GET https://api.urbandictionary.com/v0/define?term=hello`
Fields: list. Limit: unknown. Fallback: `datamuse`.

## Wiktionary
`GET https://en.wiktionary.org/w/rest.php/v1/search`
Fields: xml. Limit: unknown. Fallback: `wiktionary-2`.

## Wiktionary
`GET https://en.wiktionary.org/api/rest_v1/page/definition/hello`
Fields: en, fr, ff. Limit: unknown. Fallback: `datamuse`.
