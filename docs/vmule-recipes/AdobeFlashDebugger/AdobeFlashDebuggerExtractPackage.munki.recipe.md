# AdobeFlashDebuggerExtractPackage.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**:  
- Downloads the latest Adobe Flash Player installer, 
- extracts the embedded package inside Install Adobe Flash Player.app, 
- delete PreferencePanes files
- wraps it in a disk image, and imports it into Munki.

This pkg created with this recipe will just install:

-  /Library/Internet\ Plug-Ins/Flash\ Player.plugin
-  /Library/Internet\ Plug-Ins/flashplayer.xpt

            - **Identifier**: `com.github.vmule.munki.FlashDebuggerExtractPackage`

            - **Parent Recipes**: `com.github.vmule.download.AdobeFlashDebugger`