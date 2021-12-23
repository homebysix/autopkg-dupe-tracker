# TeradiciClientBeta.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads latest Teradici client beta disk image.

NOTES:
- DOWNLOAD_URL and _must_ be overridden in order for this recipe to work.

Log into your organization's Teradici account, visit the download URL for the Teradici (Mac) client beta, and paste in the URL referenced under "Download using a script" in the "To download the latest beta version" command:

Example:
https://dl.teradici.com/XXXXXXXXXXXXXXXX/pcoip-client-beta/raw/names/pcoip-client-dmg/versions/latest/pcoip-client_latest.dmg

- This recipe depends on homebysix's FindAndReplace.  Add homebysix's repo via:

autopkg repo-add homebysix-recipes

            - **Identifier**: `com.github.foigus.download.teradiciclientbeta`

            - **Parent Recipes**: `None`

## Warnings

- These recipes have duplicate URLDownloader URLs:
    - [foigus-recipes/Teradici/TeradiciCASGraphicsAgentBeta.download.recipe](/autopkg-dupe-tracker/foigus-recipes/Teradici/TeradiciCASGraphicsAgentBeta.download.recipe)
    - [foigus-recipes/Teradici/TeradiciCASGraphicsAgent.download.recipe](/autopkg-dupe-tracker/foigus-recipes/Teradici/TeradiciCASGraphicsAgent.download.recipe)
    - [foigus-recipes/Teradici/TeradiciClientBeta.download.recipe](/autopkg-dupe-tracker/foigus-recipes/Teradici/TeradiciClientBeta.download.recipe)

- These recipes have duplicate CURLDownloader URLs:
    - [foigus-recipes/Teradici/TeradiciCASGraphicsAgentBeta.download.recipe](/autopkg-dupe-tracker/foigus-recipes/Teradici/TeradiciCASGraphicsAgentBeta.download.recipe)
    - [foigus-recipes/Teradici/TeradiciCASGraphicsAgent.download.recipe](/autopkg-dupe-tracker/foigus-recipes/Teradici/TeradiciCASGraphicsAgent.download.recipe)
    - [foigus-recipes/Teradici/TeradiciClientBeta.download.recipe](/autopkg-dupe-tracker/foigus-recipes/Teradici/TeradiciClientBeta.download.recipe)