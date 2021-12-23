# Vectorworks.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: This recipe downloads the latest Vectorworks installer app and creates a package that leverages the silent install 
CLI method to automate installation. Input variables are used to specify which major version of Vectorworks you are 
packaging (e.g., 2021) and to customize the installation package with the recipe user's license information. 
The pkg is named with the name and the version number (e.g., the installer for Vectorworks 2021 SP2 would be named 
"Vectorworks-26.0.2"); if you want to include the year/major version in the pkg name, change the NAME variable accordingly.
Should the download not have changed, no processing is done; this is done to save redundant copying of the 2+ GB installer.
If you need Vectorworks 2020, use the Vectorworks2020.pkg recipe.


            - **Identifier**: `com.github.jazzace.pkg.vectorworks`

            - **Parent Recipes**: `com.github.jazzace.download.vectorworks`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [jazzace-recipes/Nemetschek/Vectorworks.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/Nemetschek/Vectorworks.pkg.recipe)
    - [jazzace-recipes/Nemetschek/Vectorworks2020.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/Nemetschek/Vectorworks2020.pkg.recipe)

- These recipes have duplicate NAMEs:
    - [jazzace-recipes/Nemetschek/Vectorworks.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/Nemetschek/Vectorworks.pkg.recipe)
    - [jazzace-recipes/Nemetschek/Vectorworks2020.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/Nemetschek/Vectorworks2020.pkg.recipe)