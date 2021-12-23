# EMCSyncplicitySSO.munki.recipe

_Last updated 2021-12-23 19:58:07Z_

- **Description**: Downloads the current release version of EMC Syncplicity SSO and imports into Munki. Includes a preinstall script that will check for an existing "Syncplicity.app" in /Applications and remove it if found. Also includes a postinstall script that copies first run files into place to prevent Admin prompting, and disables automatic updates and checks.

- **Identifier**: `com.github.autopkg.kernsb.munki.EMCSyncplicitySSO`

- **Parent Recipes**: `com.github.autopkg.kernsb.download.EMCSyncplicitySSO`