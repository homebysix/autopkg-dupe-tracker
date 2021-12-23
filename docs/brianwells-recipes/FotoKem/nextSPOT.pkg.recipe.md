# nextSPOT.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Creates a flat package from a manually-download copy of nextSPOT Download Manager.

This recipe originally provided an automated download of nextSPOT Download Manager,
using a download parent recipe. However, the URL was temporary in nature and so now
this recipe requires a manual download of the .dmg and for it to be passed via the
`--pkg` argument to `autopkg run`.

NOTE: The app from the vendor is NOT code signed.

NOTE: The app installs a Launch Agent for the user when first launched.

            - **Identifier**: `com.github.brianwells.pkg.nextSPOT`

            - **Parent Recipes**: `None`
