# EpsonProDrivers.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest version of the Epson product driver from Epson's site
and extracts the package from the dmg.
These will generally be drivers for professional printers and the like not included in
the drivers supplied by Apple.
Make separate overrides for each device driver you may want. An override is required.

See the parent (download) recipe for important recipe instructions.

Note: This recipe suppresses unnecessary copying of the package using the "StopProcessingIf" processor. 
This means that any recipe that uses this as a parent recipe could stop execution before reaching the child. 
You may need to remove the cache for the recipe in question and start again if you manually delete or move 
the package that this recipe creates.


            - **Identifier**: `com.github.jazzace.pkg.EpsonProDrivers`

            - **Parent Recipes**: `com.github.jazzace.download.EpsonProDrivers`