# Email

## AGPC Domain Check
`GET https://guild.tradeuniquecapital.com/api/check?domain=example.com`
Fields: domain, grade, checks_completed, checks_total, complete, findings, seconds, honesty_note. Limit: unknown. Fallback: `mail-gw`.

## mail.gw
`GET https://docs.mail.gw/_nuxt/manifest.c0c86816.json`
Fields: icons, start_url, display, background_color, theme_color, lang. Limit: unknown. Fallback: `mail-tm`.

## mail.tm
`GET https://api.mail.tm`
Fields: @context, @id, @type, domain, message. Limit: unknown. Fallback: `mailcheck-ai`.

## MailCheck.ai
`GET https://api.webshot.co/EVWMY5`
Fields: binary. Limit: unknown. Fallback: `agpc-domain-check`.
