# EpsonSureColorDrivers.ds.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads latest version of the Epson SureColor P-series product driver from Epson's site, 
extracts the package from the dmg, and copies it to a local path of your choosing.
These will generally be drivers and ICC profiles not included in the OS by Apple.
Make separate overrides for each printer you may want. An override is required.

When Epson was using separate code signing authorities for older and new products, it was
necessary to have separate recipes (EpsonProDrivers and EpsonSureColorDrivers). Now that 
Epson is using the same authority for all new releases, this recipe has been turned into a stub
recipe that points to EpsonProDrivers.download.

If you are creating a new override, use the EpsonProDrivers series of recipes.


            - **Identifier**: `com.github.jazzace.ds.EpsonSureColorDrivers`

            - **Parent Recipes**: `com.github.jazzace.ds.EpsonProDrivers`
