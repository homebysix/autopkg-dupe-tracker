# PantoneConnect.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Repackage Pantone Connect and import it into Munki.

NOTE:

- This recipe does not download the Pantone Connect package--feed the package into the recipe via the following format:
autopkg run PantoneConnect.munki -p /path/to/PantoneConnect.zxp

            - **Identifier**: `com.github.foigus.munki.PantoneConnect`

            - **Parent Recipes**: `com.github.foigus.pkg.PantoneConnect`