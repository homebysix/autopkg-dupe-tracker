# PackageApp.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: This is a generic recipe to turn an app into a .pkg installer for it.
The user must specify the path to the app at runtime via the --pkg option.
The package will be saved in the AutoPkg cache for this recipe.
A new package will be built each time.
Note that many Apple-authored apps do not work with this recipe—consider using
AppStoreApp.pkg from the nmcspadden-recipes repo instead.

            - **Identifier**: `com.github.jazzace.pkg.packageapp`

            - **Parent Recipes**: `None`
