# macOSEraseInstallHighSierraImport.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Imports a DMG with a macOS High Sierra installer inside into a munki repo. This would be built with a tool like installinstallmacos.py. Meant to be imported as an erase & install, but these options can be removed if desired.

To use this recipe:

1) Create a recipe override of this recipe.
2) Use installinstallmacos.py to create a compressed DMG of the desired macOS installer.
3) Copy the downloaded DMG onto your Mac running autopkg in the folder specified in the PATH variable. Don't include a trailing '/'.
4) Run the recipe.
5) Profit.

            - **Identifier**: `com.github.apizz.munki.macOSEraseInstallHighSierraImport`

            - **Parent Recipes**: `None`