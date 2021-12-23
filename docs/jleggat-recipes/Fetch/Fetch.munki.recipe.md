# Fetch.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest Fetch from Fetch Softworks website, creates a Apple installer pkg and imports into Munki.

Optional Values SERIALNUMBER and REGISTRANTNAME when both provided will 
add a fetch license agreement to 
/Library/Preferences/com.fetchsoftworks.Fetch.License.plist.

Set SERIALNUMBER to serial number provided in a Fetch license agreement.
Set REGISTRANTNAME to name used to register a Fetch license agreement.

            - **Identifier**: `com.github.jleggat.Fetch.munki`

            - **Parent Recipes**: `com.github.jleggat.pkg.Fetch`