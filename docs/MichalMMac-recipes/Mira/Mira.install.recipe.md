# Mira.install.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the current release version of Mira and installs it.

Package preinstall and postinstall scripts do a lot of neat things in user's Library. For example thex disable Plex helper. Installing by Munki or AutoPkg prevents them from doing so. Inspect both scripts before deploying.    


            - **Identifier**: `com.github.michalmmac.install.Mira`

            - **Parent Recipes**: `com.github.michalmmac.download.Mira`
