# Jobs

## AI Dev Jobs
`GET https://aidevboard.com/api/v1`
Fields: $schema, ai_plugin_manifest, auth, base_url, description, docs, endpoints, mcp_endpoint. Limit: unknown. Fallback: `artificial-intelligence-jobs`.

## Artificial Intelligence Jobs
`GET https://artificialintelligencejobs.co/api/jobs`
Fields: source, generated, total_live, matched, returned, offset, jobs, docs. Limit: unknown. Fallback: `devitjobs-uk`.

## DevITjobs UK
`GET https://devitjobs.uk/job_feed.xml`
Fields: xml. Limit: unknown. Fallback: `ai-dev-jobs`.

## Himalayas
`GET https://himalayas.app/jobs/api`
Fields: comments, updatedAt, offset, limit, totalCount, jobs. Limit: unknown. Fallback: `devitjobs-uk`.

## TechRole Index
`GET https://techrole.ru/open-data-daily.csv-metadata.json`
Fields: @context, url, dc:title, dc:description, dc:publisher, dc:license, dc:source, dc:conformsTo. Limit: unknown. Fallback: `himalayas`.
