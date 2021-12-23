# AdobeFlashPlayerExtractPackage.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: 
- Downloads the latest Adobe Flash Player installer, 
- extracts the embedded package inside Install Adobe Flash Player.app, 
- delete PreferencePanes,Application Support, LaunchDaemons and PreferencePanes files from the pkg
- wraps it in a disk image, and imports it into Munki.

This pkg created with this recipe will just install:

-  /Library/Internet\ Plug-Ins/Flash\ Player.plugin
-  /Library/Internet\ Plug-Ins/flashplayer.xpt

            - **Identifier**: `com.github.vmule.munki.FlashPlayerExtractPackage`

            - **Parent Recipes**: `com.github.autopkg.download.FlashPlayer`

## Warnings

- These recipes have duplicate filenames:
    - [vmule-recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe](/autopkg-dupe-tracker/vmule-recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe)
    - [recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe](/autopkg-dupe-tracker/recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [vmule-recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe](/autopkg-dupe-tracker/vmule-recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe)
    - [recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe](/autopkg-dupe-tracker/recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe)

- These recipes have duplicate NAMEs:
    - [vmule-recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe](/autopkg-dupe-tracker/vmule-recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe)
    - [recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe](/autopkg-dupe-tracker/recipes/AdobeFlashPlayer/AdobeFlashPlayerExtractPackage.munki.recipe)
    - [recipes/AdobeFlashPlayer/AdobeFlashPlayer.munki.recipe](/autopkg-dupe-tracker/recipes/AdobeFlashPlayer/AdobeFlashPlayer.munki.recipe)