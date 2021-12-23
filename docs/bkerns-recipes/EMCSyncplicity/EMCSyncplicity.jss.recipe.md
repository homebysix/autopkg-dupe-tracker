# EMCSyncplicity.jss.recipe

_Last updated 2021-12-23 20:01:50Z_

- **Description**: Downloads EMC Syncplicity disk image, builds a package, and imports into JSS. The installer package includes a preinstall script that will check for an existing "Syncplicity.app" in /Applications and remove it if found. The install package also includes a postinstall script that copies first run files into place to prevent Admin prompting, and disables automatic updates and checks.

- **Identifier**: `com.github.autopkg.kernsb.jss.EMCSyncplicity`

- **Parent Recipes**: `com.github.autopkg.kernsb.pkg.EMCSyncplicity`


## Warnings

- These recipes have duplicate NAMEs:
    - [bkerns-recipes/EMCSyncplicity/EMCSyncplicity.jss.recipe](/autopkg-dupe-tracker/bkerns-recipes/EMCSyncplicity/EMCSyncplicity.jss.recipe)
    - [bkerns-recipes/EMCSyncplicitySSO/EMCSyncplicitySSO.jss.recipe](/autopkg-dupe-tracker/bkerns-recipes/EMCSyncplicitySSO/EMCSyncplicitySSO.jss.recipe)