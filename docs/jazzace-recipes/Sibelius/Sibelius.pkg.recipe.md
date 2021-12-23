# Sibelius.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of Sibelius and extracts the package from the dmg.

Note: This recipe suppresses unnecessary copying of the package using the "StopProcessingIf" processor. 
This means that any recipe that uses this as a parent recipe could stop execution before reaching the child. 
You may need to remove the cache for the recipe in question and start again if you manually delete or move 
the package that this recipe creates.


            - **Identifier**: `com.github.jazzace.pkg.Sibelius`

            - **Parent Recipes**: `com.github.hansen-m.download.Sibelius`


## Warnings

- These recipes have duplicate filenames:
    - [jazzace-recipes/Sibelius/Sibelius.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/Sibelius/Sibelius.pkg.recipe)
    - [andrewzirkel-recipes/Sibelius/Sibelius.pkg.recipe](/autopkg-dupe-tracker/andrewzirkel-recipes/Sibelius/Sibelius.pkg.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [jazzace-recipes/Sibelius/Sibelius.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/Sibelius/Sibelius.pkg.recipe)
    - [andrewzirkel-recipes/Sibelius/Sibelius.pkg.recipe](/autopkg-dupe-tracker/andrewzirkel-recipes/Sibelius/Sibelius.pkg.recipe)