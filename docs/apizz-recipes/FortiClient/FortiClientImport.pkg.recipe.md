# FortiClientImport.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Copies the FortiClient PKG out from a FortiClient .dmg download and collects the version from the PKG.

To use this recipe:

1) Create a recipe override of this recipe.
2) Acquire your instance's FortiClient DMG with contained installer.
3) Copy the downloaded DMG onto your Mac running autopkg in the folder specified in the PATH variable. Don't include a trailing '/'.
4) Run the recipe.

More valuable when used as a parent recipe to bring FortiClient into munki, Jamf, etc.

            - **Identifier**: `com.github.apizz.pkg.FortiClientImport`

            - **Parent Recipes**: `None`
