# CameraRAW.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads Adobe Camera RAW.

NOTES:

- THIS RECIPE HAS force_munkiimport TURNED ON SINCE ALL CAMERA RAW PACKAGES ARE VERSION ZERO.  IT IS NOT RECOMMENDED TO RUN THIS RECIPE IN AN AUTOMATED FASHION SINCE THIS WILL RESULT IN MANY IMPORTS INTO THE MUNKI REPO.
- This recipe unfortunately uses an installs array of the md5 of the Camera RAW binary itself.  This is due to poor versioning choices in the plugin.
- The package has uninstallable set to false because it intersects with Creative Cloud application installations that are not recorded in the traditional receipts database, thus a "removepackages" uninstall would end up removing Camera RAW even though there might be Camera RAW-dependent applications still installed.
- This recipe is dependent on Elliot Jordan's VersionSplitter processor.  To add his repo:

autopkg repo-add homebysix-recipes

            - **Identifier**: `com.github.foigus.munki.CameraRAW`

            - **Parent Recipes**: `com.github.foigus.download.CameraRAW`

## Warnings

- These recipes have duplicate URLDownloader URLs:
    - [foigus-recipes/Adobe/CameraRAW.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/Adobe/CameraRAW.munki.recipe)
    - [foigus-recipes/Adobe/CameraRAW.download.recipe](/autopkg-dupe-tracker/foigus-recipes/Adobe/CameraRAW.download.recipe)

- These recipes have duplicate CURLDownloader URLs:
    - [foigus-recipes/Adobe/CameraRAW.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/Adobe/CameraRAW.munki.recipe)
    - [foigus-recipes/Adobe/CameraRAW.download.recipe](/autopkg-dupe-tracker/foigus-recipes/Adobe/CameraRAW.download.recipe)