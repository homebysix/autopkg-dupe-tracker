# Fetch.install.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest Fetch from Fetch Softworks website, creates a Apple installer pkg and then installs it.

Optional Values SERIALNUMBER and REGISTRANTNAME when both provided will 
add a fetch license agreement to 
/Library/Preferences/com.fetchsoftworks.Fetch.License.plist.

Set SERIALNUMBER to serial number provided in a Fetch license agreement.
Set REGISTRANTNAME to name used to register a Fetch license agreement.

            - **Identifier**: `com.github.jleggat.Fetch.install`

            - **Parent Recipes**: `com.github.jleggat.pkg.Fetch`
