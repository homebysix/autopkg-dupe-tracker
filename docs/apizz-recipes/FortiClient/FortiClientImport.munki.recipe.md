# FortiClientImport.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Copies the FortiClient mpkg out from a FortiClient .dmg download and imports it into a munki_repo.

To use this recipe:

1) Create a recipe override of this recipe.
2) Acquire your instance's FortiClient DMG with contained installer.
3) Copy the downloaded DMG onto your Mac running autopkg in the folder specified in the PATH variable. Don't include a trailing '/'.
4) Run the recipe.

            - **Identifier**: `com.github.apizz.munki.FortiClientImport`

            - **Parent Recipes**: `com.github.apizz.pkg.FortiClientImport`