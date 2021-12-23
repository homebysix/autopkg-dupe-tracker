# Geogebra.jss.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads latest Geogebra disk image, builds a package, and uploads to the JSS.

Note: Geogebra 5 changes the package ID. The installer app ignores a previously installed Geogebra 4 and makes a subfolder to install into. This is not what is desired, thus, a preinstall script will remove old versions.

            - **Identifier**: `com.github.jss-recipes.jss.Geogebra`

            - **Parent Recipes**: `com.github.sheagcraig.pkg.Geogebra`