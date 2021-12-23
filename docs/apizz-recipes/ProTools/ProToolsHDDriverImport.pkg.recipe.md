# ProToolsHDDriverImport.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Copies the Pro Tools HD Driver PKG out from a Pro Tools .dmg download.

To use this recipe:

1) Create a recipe override of this recipe.
2) Go to the Avid website and download the Pro Tools for Mac DMG.
3) Copy the downloaded DMG onto your Mac running autopkg in the folder specified in the PATH variable. Don't include a trailing '/'.
4) Run the recipe.

More valuable when used as a parent recipe to bring into munki, Jamf, etc.

            - **Identifier**: `com.github.apizz.pkg.ProToolsHDDriverImport`

            - **Parent Recipes**: `None`
