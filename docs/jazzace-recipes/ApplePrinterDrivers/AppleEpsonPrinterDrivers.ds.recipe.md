# AppleEpsonPrinterDrivers.ds.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads latest version of the Epson Printer Drivers from Apple, extracts 
the package from the dmg, and copies it to a local path of your choosing.

Note: Because this package is large (over 1 GB), the recipe suppresses unnecessary copying 
of the package using the "StopProcessingIf" processor. This means that any recipe that uses 
this as a parent recipe could stop execution before reaching the child. You may need to 
remove the cache for the recipe in question and start again if you manually delete or move 
the package that this recipe copies by extraction.

Note 2: Normally, we would use the related .pkg recipe as a parent and copy the file to our 
local repo, but the way in which AutoPkg evaluates variables means that we cannot have a .pkg 
recipe that copies the package to the AutoPkg cache or to a desired path using an input 
variable. So this recipe is identical to the .pkg version except that a destination 
path is included in the Input keys.

            - **Identifier**: `com.github.jazzace.ds.AppleEpsonPrinterDrivers`

            - **Parent Recipes**: `com.github.n8felton.download.AppleEpsonPrinterDrivers`
