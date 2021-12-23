# Fetch.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest Fetch from Fetch Softworks website and creates a Apple installer pkg.

Optional Values SERIALNUMBER and REGISTRANTNAME when both provided will 
add a fetch license agreement to 
/Library/Preferences/com.fetchsoftworks.Fetch.License.plist.

Set SERIALNUMBER to serial number provided in a Fetch license agreement.
Set REGISTRANTNAME to name used to register a Fetch license agreement.

            - **Identifier**: `com.github.jleggat.pkg.Fetch`

            - **Parent Recipes**: `com.github.jleggat.download.Fetch`
