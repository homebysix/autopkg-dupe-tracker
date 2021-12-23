# EMCSyncplicitySSO.pkg.recipe

_Last updated 2021-12-23 19:58:07Z_

- **Description**: Downloads EMC Syncplicity SSO disk image and builds a package. The installer package includes a preinstall script that will check for an existing "Syncplicity.app" in /Applications and remove it if found. The install package also includes a postinstall script that copies first run files into place to prevent Admin prompting, and disables automatic updates and checks. Adapted from rtrouton's Firefox pkg recipe.

- **Identifier**: `com.github.autopkg.kernsb.pkg.EMCSyncplicitySSO`

- **Parent Recipes**: `com.github.autopkg.kernsb.download.EMCSyncplicitySSO`