# EpsonScannerDriverAndScanUtility.ds.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of the Epson Scanner Driver and Epson Scan Utility
from Epson's site, extracts the package from the dmg, and copies it to a local path of your choosing.

Make separate overrides for each scanner driver you may want (make sure to change the
value of the NAME or DS_NAME input key). An override is required.

See the parent (download) recipe for important recipe instructions. Requires the apizz-recipes repo.

Note: This recipe suppresses unnecessary copying of the package using the "StopProcessingIf" processor. 
This means that any recipe that uses this as a parent recipe could stop execution before reaching the child. 
You may need to remove the cache for the recipe in question and start again if you manually delete or move 
the package that this recipe creates.

Note 2: This recipe is identical to the .pkg version except that the pkg is copied directly to the 
destination path DS_PKGS_PATH.

            - **Identifier**: `com.github.jazzace.ds.EpsonScannerDriver`

            - **Parent Recipes**: `com.github.apizz.download.EpsonScannerDriverandScanUtility-NewCert`
