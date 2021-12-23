# Steam.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of Steam and imports it into Munki.

NOTE: This simply installs Steam.app to /Applications, upon first launch the Steam update process will download about 180 MB of assets to complete the installation. 
These support files are downloaded to ~/Library/Application Support/Steam for the current user opening the app. These assets must be downloaded for each user on the system.

            - **Identifier**: `com.github.dataJAR-recipes.munki.Steam`

            - **Parent Recipes**: `com.github.haircut.download.Steam`
