# ProToolsCodecsImport.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Copies the Pro Tools Codecs out from a Pro Tools .dmg download and imports it into a munki_repo.

To use this recipe:

1) Create a recipe override of this recipe.
2) Go to the Avid website and download the Pro Tools for Mac DMG.
3) Copy the downloaded DMG onto your Mac running autopkg in the folder specified in the PATH variable. Don't include a trailing '/'.
4) Run the recipe.
5) Profit.

            - **Identifier**: `com.github.apizz.munki.ProToolsCodecsImport`

            - **Parent Recipes**: `com.github.apizz.pkg.ProToolsCodecsImport`