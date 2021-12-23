# AdobeAcrobatProBaseCustomized.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads latest Adobe Acrobat Pro DC (Continuous) Enterprise installer
as provided at https://helpx.adobe.com/acrobat/kb/acrobat-dc-downloads.html,
uses the Customization Wizard for DC to output a customized installer package,
and imports the result into Munki.


ENABLE_BROWSER_PLUGIN can be set to any value to enable the Adobe Acrobat Pro
NPAPI browser plugin


            - **Identifier**: `com.github.timsutton.munki.adobe-acrobat-pro-base-customized`

            - **Parent Recipes**: `com.github.timsutton.pkg.adobe-acrobat-pro-base-customized`
