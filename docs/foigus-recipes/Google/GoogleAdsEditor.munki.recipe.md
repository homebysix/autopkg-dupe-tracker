# GoogleAdsEditor.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads latest Google Ads Editor disk image, builds an installation package, and imports it into Munki.

NOTES:
- When "Google Ads Editor" version 1.0 was released, the versioning for Ads Editor was reset to 1.0 even though the actual software went to version 13.  Subtract 12 from the major version to get the marketing version of Google Ads Editor (e.g. 13-12=1)
- This package carries the Google Keystone updater.  To get rid of the Keystone updater, set the following postuninstall_script in your override

###
#!/bin/bash

rm "/Applications/Google Ads Editor.app/Contents/Frameworks/KeystoneRegistration.framework/Versions/A/Resources/Keystone.tbz" \
"/Applications/Google Ads Editor.app/Contents/Frameworks/KeystoneRegistration.framework/Versions/A/Resources/ksinstall"
###

            - **Identifier**: `com.github.foigus.munki.googleadseditor`

            - **Parent Recipes**: `com.github.foigus.pkg.googleadseditor`
