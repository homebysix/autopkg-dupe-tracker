# AppleEpsonPrinterDrivers.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads latest version of the Epson Printer Drivers from Apple and extracts 
the package from the dmg.

Note: Because this package is large (over 1 GB), the recipe suppresses unnecessary copying 
of the package using the "StopProcessingIf" processor. This means that any recipe that uses 
this as a parent recipe could stop execution before reaching the child. You may need to 
remove the cache for the recipe in question and start again if you manually delete or move 
the package that this recipe creates.

            - **Identifier**: `com.github.jazzace.pkg.AppleEpsonPrinterDrivers`

            - **Parent Recipes**: `com.github.n8felton.download.AppleEpsonPrinterDrivers`


## Warnings

- These recipes have duplicate filenames:
    - [jazzace-recipes/ApplePrinterDrivers/AppleEpsonPrinterDrivers.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/ApplePrinterDrivers/AppleEpsonPrinterDrivers.pkg.recipe)
    - [novaksam-recipes/Recipes - pkg/AppleEpsonPrinterDrivers.pkg.recipe](/autopkg-dupe-tracker/novaksam-recipes/Recipes - pkg/AppleEpsonPrinterDrivers.pkg.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [jazzace-recipes/ApplePrinterDrivers/AppleEpsonPrinterDrivers.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/ApplePrinterDrivers/AppleEpsonPrinterDrivers.pkg.recipe)
    - [novaksam-recipes/Recipes - pkg/AppleEpsonPrinterDrivers.pkg.recipe](/autopkg-dupe-tracker/novaksam-recipes/Recipes - pkg/AppleEpsonPrinterDrivers.pkg.recipe)