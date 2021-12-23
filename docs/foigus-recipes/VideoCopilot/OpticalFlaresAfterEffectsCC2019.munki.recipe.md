# OpticalFlaresAfterEffectsCC2019.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: "Downloads" Optical Flares, packages it for installation under After Effects CC 2019, and imports the package into Munki.

WARNING: The POSIX permissions in this recipe on the "VideoCopilot" folder are 0777 since this is the location where Video Copilot wants to place the license.  This can be changed by overriding the permissions in the "Input".

NOTE: This recipe does not download the Optical Flares zip archive--feed the zip archive into the recipe via the following format:

autopkg run OpticalFlaresAfterEffectsCC2019.munki -p /path/to/OpticalFlaresInstaller_1.3.5_Mac_2020.zip

            - **Identifier**: `com.github.foigus.munki.OpticalFlaresAfterEffectsCC2019`

            - **Parent Recipes**: `com.github.foigus.pkg.OpticalFlaresAfterEffectsCC2019`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/VideoCopilot/OpticalFlaresAfterEffectsCC2020.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/VideoCopilot/OpticalFlaresAfterEffectsCC2020.munki.recipe)
    - [foigus-recipes/VideoCopilot/OpticalFlaresAfterEffectsCC2019.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/VideoCopilot/OpticalFlaresAfterEffectsCC2019.munki.recipe)