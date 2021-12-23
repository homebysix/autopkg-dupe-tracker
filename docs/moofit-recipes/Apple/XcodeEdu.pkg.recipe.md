# XcodeEdu.pkg.recipe

    _Last updated 2021-12-23 20:01:50Z_

    - **Description**: Creates an installer package from a supplied .xip file downloaded using Facebook's "xcode.downloader" 
recipe, and extracted using their "xcode.extract" recipe from their AutoPkg repo 
"com.github.facebook.Recipes-for-AutoPkg".

This recipe also adds a postflight script to the package, to install the command-line tools and configure these 
for lab Mac use.

Due to Apple signed packages not being able to install to SIP protected areas when called via a postflight, the
additional packages are installed by a self-destrictible LaunchDaemon which is called immediately after the 
"parent" Xcode installer is complete. This LaunchDaemon runs a script (both stored in /tmp) which installs all 3
additional component packages, and then unloads and deletes the launchdaemon, and itself.

This kind of installation package would typically be used in lab enviroments, where users don't have admin 
rights.

Please see https://github.com/facebook/Recipes-for-AutoPkg for usage

    - **Identifier**: `com.github.moofit-recipes.pkg.XcodeEdu`

    - **Parent Recipes**: `com.facebook.autopkg.xcode.extract`
