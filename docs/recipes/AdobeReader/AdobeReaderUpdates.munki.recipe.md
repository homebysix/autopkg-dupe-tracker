# AdobeReaderUpdates.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest update for Adobe Reader and imports into Munki. This is not a complete
installer for Adobe Reader as is provided by AdobeReader.munki, but recent versions (11.0.11 and 11.0.12)
have not been made available as integrated installers. These updates are also multilingual, and provide
updates for languages that aren't available in full installers.

See AdobeReaderUpdates.download for MAJOR_VERSION and OS_VERSION input variables.

This recipe does not currently support "patch" updaters for Reader DC.

Based on AdobeReaderUpdates recipes by Matthias Choules,
https://github.com/autopkg/recipes/pull/61.


            - **Identifier**: `com.github.autopkg.munki.AdobeReaderUpdates`

            - **Parent Recipes**: `com.github.autopkg.download.AdobeReaderUpdates`