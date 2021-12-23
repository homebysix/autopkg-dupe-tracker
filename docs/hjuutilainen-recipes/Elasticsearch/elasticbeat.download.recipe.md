# elasticbeat.download.recipe

_Last updated 2021-12-23 20:01:51Z_

- **Description**: Downloads the latest defined Elastic Beat product. Use an override to set OPTIONAL_VERSION to -oss to download the Apache 2.0 licensed version of the Beat. Set BEAT_NAME to one of the following: filebeat, packetbeat, metricbeat, heartbeat, auditbeat, functionbeat. Note: winlogbeat and journalbeat do not have macOS binaries and functionbeat does not have an Apache 2.0 licensed version.

- **Identifier**: `io.github.hjuutilainen.download.elasticbeat`

- **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate NAMEs:
    - [hjuutilainen-recipes/Elasticsearch/elasticbeat.download.recipe](/autopkg-dupe-tracker/hjuutilainen-recipes/Elasticsearch/elasticbeat.download.recipe)
    - [hjuutilainen-recipes/Elasticsearch/filebeat.download.recipe](/autopkg-dupe-tracker/hjuutilainen-recipes/Elasticsearch/filebeat.download.recipe)