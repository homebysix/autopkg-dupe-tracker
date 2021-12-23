# SendtoKindle.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads latest Send to Kindle, modifies a postinstall to exit 0 in case of scripting failure, and imports it into Munki.

NOTE:
- This recipe depends on facebook's FileAppender.  Add facebook's repo via:
autopkg repo-add https://github.com/facebook/Recipes-for-AutoPkg
- Requiring a restart rather than troubleshooting the Send to Kindle LaunchAgent trying to find a keychain to store "DeviceSerialNumber"
- STOP_ON_NO_NEW_DOWNLOAD is set to "true" by default.  Amazon's packages seem to be perpetually version 1.0, so this will allow new package version 1.0's to be imported

            - **Identifier**: `com.github.foigus.munki.SendToKindle`

            - **Parent Recipes**: `com.github.foigus.pkg.SendToKindle`