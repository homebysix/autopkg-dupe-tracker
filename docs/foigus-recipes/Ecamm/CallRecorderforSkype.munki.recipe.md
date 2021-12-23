# CallRecorderforSkype.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads latest Call Recorder for Skype installer, packages it, and imports it into Munki.

Note: CUSTOMER_EMAIL and REG_CODE _must_ be overridden in order for this recipe to work.

Log in to your Ecamm customer center and inspect the URL for these values:
- The CUSTOMER_EMAIL is the "u" parameter. It's your customer email address, URL-encoded.
- The REG_CODE is the "c" parameter, a six-character string.

Example (spaces added for clarity):
https://www.ecamm.com/cgi-bin/customercenter ? u=john%2Edoe%40example%2Ecom & c=XYZ123

- Call Recorder for Skype removes the code signature from a Skype component.  This is set in the
postinstall script, but defaults to _not_ performing the code signature removal.  Please change
this in the override to indicate understanding of the change to Skype.

            - **Identifier**: `com.github.foigus.munki.CallRecorderforSkype`

            - **Parent Recipes**: `com.github.foigus.pkg.CallRecorderforSkype`