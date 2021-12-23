# ColorNavigatorNX.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest ColorNavigator NX installer and imports it into Munki.

Relying on a package recipe to extract the ColorNavigator NX package since it currently ships on a read-write disk image.

Requiring a logout since updating monitor calibration software while a user is using the monitor wouldn't be good.

            - **Identifier**: `com.github.foigus.munki.ColorNavigatorNX`

            - **Parent Recipes**: `com.github.foigus.download.ColorNavigatorNX`