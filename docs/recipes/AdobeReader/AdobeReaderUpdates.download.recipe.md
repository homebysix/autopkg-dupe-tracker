# AdobeReaderUpdates.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest multi-lingual Adobe Reader "patch" updater pkg. This is not a complete
installer for Adobe Reader as is provided by AdobeReader.download, but recent versions (11.0.11 and 11.0.12)
have not been made available as integrated installers. These updates are also multilingual, and provide
updates for languages that aren't available in full installers.

Set MAJOR_VERSION to either '10' or '11'. OS_VERSION defaults to 10.9 because the most recent
updates, (10.1.14, 11.0.12) are offered only to OS X 10.9 and up, but this can be set to try requesting the
update for different client OS X versions if newer versions are offered exclusively to higher OS X versions
in the future.

This recipe does not currently support "patch" updaters for Reader DC.

Based on AdobeReaderUpdates recipes by Matthias Choules,
https://github.com/autopkg/recipes/pull/61.


            - **Identifier**: `com.github.autopkg.download.AdobeReaderUpdates`

            - **Parent Recipes**: `None`

## Warnings

- These recipes have duplicate NAMEs:
    - [recipes/AdobeReader/AdobeReader.download.recipe](/autopkg-dupe-tracker/recipes/AdobeReader/AdobeReader.download.recipe)
    - [recipes/AdobeReader/AdobeReaderUpdates.download.recipe](/autopkg-dupe-tracker/recipes/AdobeReader/AdobeReaderUpdates.download.recipe)
    - [hansen-m-recipes/Adobe/AdobeReader-Win.download.recipe](/autopkg-dupe-tracker/hansen-m-recipes/Adobe/AdobeReader-Win.download.recipe)