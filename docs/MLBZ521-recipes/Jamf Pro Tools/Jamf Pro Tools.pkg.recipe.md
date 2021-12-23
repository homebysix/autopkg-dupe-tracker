# Jamf Pro Tools.pkg.recipe

            _Last updated 2021-12-23 19:58:06Z_

            - **Description**: Downloads and packages the latest verison of the Jamf Pro Tools from a local file share for use by Site Admins.

Only the Composer, Jamf Remote, and Recon applications are checked for code sign verified and packaged.  These are the only apps that our Site Admins use, which is what this recipe is written for.

The name of the folder name in /Applications and the package will be named based on the NAME substituion variable.

            - **Identifier**: `com.github.mlbz521.pkg.JamfProTools`

            - **Parent Recipes**: `com.github.mlbz521.download.JamfProTools`