# SplashtopStreamer.munki.recipe

_Last updated 2021-12-23 20:01:50Z_

- **Description**: Downloads the current version of Splashtop streamer. Set DEPLOY_CODE with your deploy code. Set PLIST_PERM to your desired chmod permissions for the plashtop-Streamer.plist. Permissions on the Splashtop-Streamer.plist are installed as 666, any user can change and delete settings. Set HIDE_FOLDER "hidden" to hide the /Users/Shared/Splashtop folder and "nohidden" to keep the default visibility.

- **Identifier**: `com.github.peetinc.munki.SplashtopStreamer`

- **Parent Recipes**: `com.github.peetinc.download.SplashtopStreamer`
