# Spotify.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest Spotify and imports into Munki.

Note: 1.0.50 and 1.0.51 versions of Spotify has mode 744 for its executables,
causing the app to not launch for any user except the user who installed
it, root in the case of Munki. Currently a postinstall_script fixes this issue
by adding group and owner +x to these files.

Related GitHub issue:
https://github.com/autopkg/recipes/issues/196


            - **Identifier**: `com.github.autopkg.munki.Spotify`

            - **Parent Recipes**: `com.github.autopkg.download.Spotify`
