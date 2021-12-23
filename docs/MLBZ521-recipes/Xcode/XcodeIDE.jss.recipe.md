# XcodeIDE.jss.recipe

            _Last updated 2021-12-23 20:01:49Z_

            - **Description**: Download the Xcode IDE from the Apple dev portal, creates a .pkg, and uploads it to the JPS.  Uses Facebook's "xcode.downloader" recipe.

The Policy will be named %NAME% %Major Version%, e.g. "Xcode 12"

Important Override Variables:
	* You must override APPLE_ID and ( PASSWORD_FILE or PASSWORD )
	* BETA must either be empty for stable releases or set to "Beta" in order to match Xcode betas

See https://github.com/facebook/Recipes-for-AutoPkg/tree/master/Xcode for more information.

            - **Identifier**: `com.github.mlbz521.jss.XcodeIDE`

            - **Parent Recipes**: `com.github.moofit-recipes.pkg.Xcode`


## Warnings

- These recipes have duplicate NAMEs:
    - [MLBZ521-recipes/Xcode/XcodeIDE.jss.recipe](/autopkg-dupe-tracker/MLBZ521-recipes/Xcode/XcodeIDE.jss.recipe)
    - [jss-recipes/Xcode/Xcode.jss.recipe](/autopkg-dupe-tracker/jss-recipes/Xcode/Xcode.jss.recipe)
    - [novaksam-recipes/XCode/XCode.jss.recipe](/autopkg-dupe-tracker/novaksam-recipes/XCode/XCode.jss.recipe)
    - [smithjw-recipes/Xcode/Xcode.jss.recipe.yaml](/autopkg-dupe-tracker/smithjw-recipes/Xcode/Xcode.jss.recipe.yaml)