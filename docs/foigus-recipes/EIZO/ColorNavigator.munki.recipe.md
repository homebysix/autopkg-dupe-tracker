# ColorNavigator.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest ColorNavigator installer and imports it into Munki.

Relying on a package recipe to extract the ColorNavigator package since it currently ships on a read-write disk image.

Note this recipe adds the version number to the "name" of the recipe since EIZO has dropped support for monitors when  releasing new major versions of ColorNavigator

Reference: http://www.eizoglobal.com/support/db/products/software/search?k=colornavigators

Requiring a logout since the GUI installer reopens ColorNavigator, but not from the CLI.  Also, updating calibration software while a user is using the monitor wouldn't be good.

            - **Identifier**: `com.github.foigus.munki.ColorNavigator`

            - **Parent Recipes**: `com.github.foigus.pkg.ColorNavigator`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/EIZO/ColorNavigator.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/EIZO/ColorNavigator.munki.recipe)
    - [foigus-recipes/EIZO/ColorNavigator7.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/EIZO/ColorNavigator7.munki.recipe)