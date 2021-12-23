# Jamf Pro Tools.jss.recipe

            _Last updated 2021-12-23 19:58:06Z_

            - **Description**: Downloads and packages the latest verison of Jamf Pro Tools from a local file share and then uploads it to a JPS.

Only the Composer, Jamf Remote, and Recon applications are packaged in the parent recipe.  These are the only apps that our Site Admins use, which is what this recipe is written for.

The name of the folder name in /Applications and the package will be named based on the NAME substituion variable.

            - **Identifier**: `com.github.mlbz521.jss.JamfProTools`

            - **Parent Recipes**: `com.github.mlbz521.pkg.JamfProTools`