# ProVideoFormats.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads latest version of the Pro Video Formats (previously known as ProApps QuickTime Codecs)
    provided by Apple for their pro apps and extracts the package from the dmg.

This recipe suppresses unnecessary copying of the package using the "StopProcessingIf" 
processor. This means that any recipe that uses this as a parent recipe could stop execution 
before reaching the child. You may need to remove the cache for the recipe in question and 
start again if you manually delete or move the package that this recipe creates.

*** Note 1: This Recipe requires an external processor. You must have Nate Felton's recipe repo
    available in your cache: com.github.autopkg.n8felton-recipes ***
*** Note 2: The pkg installer is an updater that requires that you have one of the following installed:
    * Final Cut Pro 7 or later (including X)
    * Compressor 3.5 or later
    * Motion 4.0 or later
    Having that software installed means you also agreed to the appropriate Software License Agreement(s). ***    

The NAME input key is specified in the parent recipe. Use an override if you want something
other than the default.


            - **Identifier**: `com.github.jazzace.pkg.ProVideoFormats`

            - **Parent Recipes**: `com.github.jazzace.download.ProVideoFormats`