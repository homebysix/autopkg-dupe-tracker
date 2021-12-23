# MSOffice2011Updates.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Finds latest Office 2011 update, downloads the disk image and extracts the pkg.
Set VERSION to a specific version number to download that version instead.
Set CULTURE_CODE to a different value to get a different localization. See http://msdn.microsoft.com/en-us/library/ee825488(v=cs.20).aspx for a table of Culture Codes.

If you would like to use an undocumented HTTPS download, set DOWNLOAD_URL_SCHEME to https.

`autopkg run MSOffice2011Updates.munki -k VERSION=14.1.0 -k DISABLE_CODE_SIGNATURE_VERIFICATION=true`
will download and import the 14.1.0 update; most of the later Office updates declare they require
this update, so save yourself some headaches by adding this update to your repo even if you don't
technically require it because your base installer is 14.1.0 or higher. The
DISABLE_CODE_SIGNATURE_VERIFICATION flag is required for 14.1.0 because the installer certificate name
in the download recipe (for current versions) doesn't match that of the 14.1.0 update. The installer
certificate for the downloaded update can still be manually verified, however.


            - **Identifier**: `com.github.autopkg.munki.Office2011Updates`

            - **Parent Recipes**: `com.github.autopkg.download.Office2011Updates`

## Warnings

- These recipes have duplicate NAMEs:
    - [recipes/MSOffice2011Updates/MSOffice2011Updates.munki.recipe](/autopkg-dupe-tracker/recipes/MSOffice2011Updates/MSOffice2011Updates.munki.recipe)
    - [ygini-recipes/MSOfficeUpdates/Office2011Updates-fr_FR.munki.recipe](/autopkg-dupe-tracker/ygini-recipes/MSOfficeUpdates/Office2011Updates-fr_FR.munki.recipe)