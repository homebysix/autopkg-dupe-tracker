# ProToolsImport.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Copies the Pro Tools PKG out from a Pro Tools .dmg download, collects the version from the filename, and imports it into a munki_repo. Adds the specific Pro Tools Codecs and HD Driver versions to the `requires` array.

Refer to this article on the supported minimum & maximum supported macOS versions: http://avid.force.com/pkb/articles/en_US/Compatibility/Pro-Tools-System-Requirements

To use this recipe:

1) Create a recipe override of this recipe.
2) Go to the Avid website and download the Pro Tools for Mac DMG.
3) Copy the downloaded DMG onto your Mac running autopkg in the folder specified in the PATH variable. Don't include a trailing '/'.
4) Specify the desired Pro Tools display name in the DISPLAY_NAME variable. The collected version will be appended to the name.
5) Specify the munki item name for the HD Driver as listed in your munki repo in the PROTOOLS_DRIVER_NAME. This name and the detected PKG version of the HD Driver in the .dmg will be added to the `requires` array for Pro Tools.
6) Specify the munki item name for the Codecs as listed in your munki repo in the PROTOOLS_CODECS_NAME input variable. This name and the detected PKG version of the Codecs in the .dmg will be added to the `requires` array for Pro Tools.
7) Refer to Avid's KB article on supported macOS versions (https://avid.secure.force.com/pkb/articles/en_US/Compatibility/Pro-Tools-System-Requirements) and update the PROTOOLS_MACOS_SUPPORTED_LIST accordingly. This will use the defined supported versions to compare with the installed version via a preinstall_script. If a supported version is not found, an exit status of 1 is produced and the item is not installed.
8) Run the recipe.
9) Profit.

            - **Identifier**: `com.github.apizz.munki.ProToolsImport`

            - **Parent Recipes**: `com.github.apizz.pkg.ProToolsImport`