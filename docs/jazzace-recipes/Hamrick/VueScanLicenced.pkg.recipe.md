# VueScanLicenced.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads VueScan and then creates an installer package with the app and the needed authorization file.
This recipe requires the hansen-m-recipes (Matt Hansen) repo.

The recipe requires the authorization file created by VueScan for your licence.
The suggested way to do this is to install VueScan on the Mac/VM running AutoPkg and use the recipe's
default value for RC_FILE. Alternately, you can create a text file made up of the following four lines
(where you replace # with the values for your license):

[VueScan]
SerialNumber=#
CustomerNumber=#
EmailAddress=#@#.#

Then, save that file in a locally-accessible location and set the RC_FILE input variable to
the path to that file (including the file name with extension). AutoPkg will do the rest.

            - **Identifier**: `com.github.jazzace.pkg.VueScanLicenced`

            - **Parent Recipes**: `com.github.hansen-m.download.VueScan`