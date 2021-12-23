# CaptureOneSubscription.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the current release version of Capture One and imports it into Munki for use with subscription-licensed Capture One.

Notes:

- Due to Phase One's decision to go with different versions for the software itself and marketing (e.g. Capture One version 13 is marketed as version 20), this recipe also has a MARKETING_VERSION variable to account for the discrepancy

This recipe is made for Capture One when licensed with a subscription and has the following unique features/options when compared to the recipe for the perpetual version of Capture One:

- Has a static Munki "name" as opposed to the "CaptureOneXX" "name"-"marketing version" format used in the perpetual recipe (defaults to "CaptureOneSubscription")
- STOP_ON_NO_NEW_DOWNLOAD Option: Skips import if no new file was retrieved in the "download" recipe (defaults to true).  Assuming a stable ETag, this allows the recipe to run (typically in an automated fashion) with force_munkiimport set to true but avoiding duplicate imports.  This allows this recipe for subscription-licensed Capture One to run in tandem with the perpetually-licensed Capture One recipe
- FORCE_MUNKIIMPORT Option: Controls whether force_munkiimport is enabled (defaults to true (the string value is set), switch to an empty set of string tags for false).  This allows the AutoPkg admin to control the force_munkiimport behavior in case it is required

Expected uses of this recipe:

- Capture One perpetual and Capture One subscription are in use: Recipe left in default state (STOP_ON_NO_NEW_DOWNLOAD is true, FORCE_MUNKIIMPORT is set)
- Only Capture One subscription licensing is in use: STOP_ON_NO_NEW_DOWNLOAD is overridden to false, FORCE_MUNKIIMPORT is overridden to a null/empty string (although the behavior _should_ be acceptable even if these variables are not overridden)

            - **Identifier**: `com.github.foigus.munki.CaptureOneSubscription`

            - **Parent Recipes**: `com.github.foigus.download.CaptureOne`
