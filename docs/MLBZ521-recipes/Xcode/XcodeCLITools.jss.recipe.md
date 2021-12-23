# XcodeCLITools.jss.recipe

            _Last updated 2021-12-23 19:58:06Z_

            - **Description**: Download the Xcode Command Line Tools from the Apple dev portal, creates a .pkg, and uploads it to the JPS.  Uses Facebook's "xcode.downloader" recipe.

The Policy will be named %NAME% %Major Version%, e.g. "Xcode Command Line Tools 12"

Important Override Variables:
	* You must override APPLE_ID and ( PASSWORD_FILE or PASSWORD )
	* BETA must either be empty for stable releases or set to "Beta" in order to match Xcode betas

See https://github.com/facebook/Recipes-for-AutoPkg/tree/master/Xcode for more information.

            - **Identifier**: `com.github.mlbz521.jss.XcodeCLITools`

            - **Parent Recipes**: `com.github.mlbz521.pkg.XcodeCLITools`