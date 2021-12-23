# CaptureOne.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the current release version of Capture One.

NOTES:

- Due to Phase One's decision to go with different versions for the software itself and marketing (e.g. Capture One version 13 is marketed as version 20), this recipe also has a MARKETING_VERSION variable to account for the discrepancy.
- Major version upgrades of Capture One perpetual licenses are generally paid upgrades, however Phase One's update URL doesn't stop at major version boundaries (e.g. the update URL for Capture One 7 offers a download of Capture One 9) and new major versions of Capture One are paid updates.  In an attempt to avoid accidentally downloading (and subsequently importing) Capture One updates that require a paid update, we restrict to an ACTUAL_VERSION and a corresponding MARKETING_VERSION.  When Phase One releases a new major version, this recipe will break until ACTUAL_VERSION and MARKETING_VERSION are updated (either via override or by updating this recipe).

            - **Identifier**: `com.github.foigus.download.CaptureOne`

            - **Parent Recipes**: `None`