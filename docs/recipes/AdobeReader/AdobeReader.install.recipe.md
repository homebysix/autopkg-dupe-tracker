# AdobeReader.install.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the current Adobe Reader pkg and repackages, replacing a problematic preinstall script,
and enabling installation on non-boot volumes. Finally, it is installed. Setting MAJOR_VERSION to "10" will cause a download of the
latest/last version of Adobe Reader 10, but the repackager is unlikely to operate properly with that version.


            - **Identifier**: `com.github.autopkg.install.AdobeReader`

            - **Parent Recipes**: `com.github.autopkg.pkg.AdobeReader`


## Warnings

- These recipes have duplicate NAMEs:
    - [recipes/AdobeReader/AdobeReaderDC.install.recipe](/autopkg-dupe-tracker/recipes/AdobeReader/AdobeReaderDC.install.recipe)
    - [recipes/AdobeReader/AdobeReader.install.recipe](/autopkg-dupe-tracker/recipes/AdobeReader/AdobeReader.install.recipe)