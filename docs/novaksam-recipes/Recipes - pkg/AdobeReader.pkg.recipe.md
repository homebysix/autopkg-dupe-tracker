# AdobeReader.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the current Adobe Reader pkg and repackages, replacing a problematic preinstall script, 
and enabling installation on non-boot volumes. Setting MAJOR_VERSION to "10" will cause a download of the 
latest/last version of Adobe Reader 10, but the repackager is unlikely to operate properly with that version.
This recipe is a retooling of the AdobeReader recipe provided by autopkg. All of the base work goes to them,
I just wanted to tweak it a little and get the version number on the installer.


            - **Identifier**: `com.github.novaksam.pkg.AdobeReader`

            - **Parent Recipes**: `com.github.autopkg.download.AdobeReader`


## Warnings

- These recipes have duplicate filenames:
    - [novaksam-recipes/Recipes - pkg/AdobeReader.pkg.recipe](/autopkg-dupe-tracker/novaksam-recipes/Recipes - pkg/AdobeReader.pkg.recipe)
    - [recipes/AdobeReader/AdobeReader.pkg.recipe](/autopkg-dupe-tracker/recipes/AdobeReader/AdobeReader.pkg.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [novaksam-recipes/Recipes - pkg/AdobeReader.pkg.recipe](/autopkg-dupe-tracker/novaksam-recipes/Recipes - pkg/AdobeReader.pkg.recipe)
    - [recipes/AdobeReader/AdobeReader.pkg.recipe](/autopkg-dupe-tracker/recipes/AdobeReader/AdobeReader.pkg.recipe)

- These recipes have duplicate NAMEs:
    - [novaksam-recipes/Recipes - pkg/AdobeReader.pkg.recipe](/autopkg-dupe-tracker/novaksam-recipes/Recipes - pkg/AdobeReader.pkg.recipe)
    - [recipes/AdobeReader/AdobeReader.pkg.recipe](/autopkg-dupe-tracker/recipes/AdobeReader/AdobeReader.pkg.recipe)