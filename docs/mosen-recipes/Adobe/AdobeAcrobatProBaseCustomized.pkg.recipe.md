# AdobeAcrobatProBaseCustomized.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads latest Adobe Acrobat Pro DC (Continuous) Enterprise installer
as provided at https://helpx.adobe.com/acrobat/kb/acrobat-dc-downloads.html,
and uses the Customization Wizard for DC to output a customized installer package.

MAJOR_VERSION can be updated if Adobe updates this to 2017, 2018, etc.

FEATURE_LOCKDOWN_PLIST can be provided to add additional parameters as documented on
Adobe's Acrobat Enterprise website. The default provided by this recipe is to
disable the built-in auto-updater for both the "DC" and "2015" (Classic) releases
of Acrobat Pro DC. Other parameters may be added by the admin as desired.

SERIAL_NUMBER can contain a serial number for the license. If omitted, either
Named Licensing or a license file provided by a serialization/device license
from CCP can be used.


            - **Identifier**: `com.github.timsutton.pkg.adobe-acrobat-pro-base-customized`

            - **Parent Recipes**: `com.github.timsutton.download.adobe-acrobat-pro-base`
