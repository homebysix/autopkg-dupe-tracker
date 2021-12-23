# AutodeskMaya2020Import.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Imports a DMG with an Autodesk Maya installer app inside. Install requires copying the install app to a desired location on the endpoint and using a postinstall script to trigger the install.

To use this recipe:

1) Download a copy of Autodesk Maya 2020.
2) Create a recipe override of this recipe.
3) Specify a PATH where the recipe will look for a Maya 2020 DMG. If applicable, move your downloaded Maya 2020 to this location.
4) Specify a DESTINATION_PATH which munki will copy the install app to on endpoints. This will also be inserted in the required places in the postinstall script for installation.
5) Enter your license type in MAYA_LICENSE_TYPE. Valid options are USER, STANDALONE, and NETWORK.
6) If applicable, update the MAYA_LOCALE. Default is 'US'.
7) Enter your Maya's SERIAL to be used in the postinstall script to activate the software.
8) Run the recipe.
9) Profit.

            - **Identifier**: `com.github.apizz.munki.AutdoeskMayaImport`

            - **Parent Recipes**: `None`
