# FinalCutProXContent.ds.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads latest version of the Final Cut Pro X Supplemental Content, extracts the package from the dmg,
and then copies it to a local path of your choosing.

This recipe suppresses unnecessary copying of the package using the "StopProcessingIf" 
processor. This means that any recipe that uses this as a parent recipe could stop execution 
before reaching the child. You may need to remove the cache for the recipe in question and 
start again if you manually delete or move the package that this recipe copies by extraction.

*** Note: The parent recipe requires an external processor. You must have Nate Felton's recipe repo
    available in your cache: com.github.autopkg.n8felton-recipes ***

DS_PKGS_PATH is the destination path for the copy. A trailing slash is not required/desired.
NAME will be used to name the copied pkg.


            - **Identifier**: `com.github.jazzace.ds.FCPContent`

            - **Parent Recipes**: `com.github.jazzace.download.FCPContent`