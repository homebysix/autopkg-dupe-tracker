# OpticalFlaresAfterEffectsCC2019.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: "Downloads" Optical Flares and packages it for installation under After Effects CC 2019.

WARNING: The POSIX permissions in this recipe on the "VideoCopilot" folder are 0777 since this is the location where Video Copilot wants to place the license--0777 rights allows a non-admin to license Video Copilot without admin assistance.  This can be changed by overriding the VIDEOCOPILOT_FOLDER_PERMISSIONS permissions in the "Input".

NOTE:

- This recipe does not download the Optical Flares zip archive--feed the zip archive into the recipe via the following format:

autopkg run OpticalFlaresAfterEffectsCC2019.pkg -p /path/to/OpticalFlaresInstaller_1.3.5_Mac_2020.zip

- This recipe depends on jessepeterson's ModeChanger.  Add jessepeterson's repo via:

autopkg repo-add jessepeterson-recipes

            - **Identifier**: `com.github.foigus.pkg.OpticalFlaresAfterEffectsCC2019`

            - **Parent Recipes**: `com.github.foigus.download.OpticalFlares`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/VideoCopilot/OpticalFlaresAfterEffectsCC2019.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/VideoCopilot/OpticalFlaresAfterEffectsCC2019.pkg.recipe)
    - [foigus-recipes/VideoCopilot/OpticalFlaresAfterEffectsCC2020.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/VideoCopilot/OpticalFlaresAfterEffectsCC2020.pkg.recipe)