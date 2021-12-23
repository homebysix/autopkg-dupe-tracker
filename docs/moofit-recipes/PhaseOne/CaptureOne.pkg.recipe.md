# CaptureOne.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the current release version of Capture One and packages.

Note major version upgrades of Capture One are generally paid upgrades, however Phase One's update URL doesn't stop at major version boundaries (e.g. the update URL for Capture One 7 offers a download of Capture One 9) and new major versions of Capture One are paid updates.

In an attempt to avoid accidentally downloading (and subsequently importing) Capture One updates that require a paid update, we restrict to a MAJOR_VERSION.  When Phase One releases a new major version, this recipe will break until MAJOR_VERSION is updated (either via override or by updating this recipe).

            - **Identifier**: `com.github.moofit-recipes.pkg.CaptureOne`

            - **Parent Recipes**: `com.github.foigus.download.CaptureOne`