# Mira.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the current release version of Mira and imports it into Munki.

Munki recipe specifies `RequireRestart` pkginfo key because of multiple launchd items (un)loaded by package scripts in user context.
Package preinstall and postinstall scripts do a lot of neat things in user's Library. For example thex disable Plex helper. Installing by Munki or AutoPkg prevents them from doing so. Inspect both scripts before deploying.


            - **Identifier**: `com.github.michalmmac.munki.Mira`

            - **Parent Recipes**: `com.github.michalmmac.download.Mira`