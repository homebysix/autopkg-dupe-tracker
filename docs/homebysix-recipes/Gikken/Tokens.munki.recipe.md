# Tokens.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest version of Tokens and imports it into Munki.

Note: Tokens was taken over by a new developer, Gikken, and Tokens 2 was released in September 2020.
Despite the name and path (/Applications/Tokens 2.app), the first version of this new app is 1.0.0.
This may require you to manually adjust your distribution method (e.g. Munki pkginfo) if you wish to
upgrade from the old app from developer Peer Assembly.

            - **Identifier**: `com.github.homebysix.munki.Tokens`

            - **Parent Recipes**: `com.github.homebysix.download.Tokens`