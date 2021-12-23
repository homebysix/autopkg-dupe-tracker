# OpticalFlaresProPresets1AfterEffectsCC2020.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: "Downloads" Pro Presets, packages it for After Effects CC 2020, and imports it into Munki.

WARNING: The POSIX permissions in this recipe on the "VideoCopilot" folder are 0777 since this is the location where Video Copilot wants to place the license.  This can be changed by overriding the permissions in the "Input".

NOTE:
- This recipe cannot determine the version of Pro Presets and must have it fed in as Input, whether via override or via CLI with -k
- This recipe does not download the Pro Presets zip archive--feed the zip archive into the recipe via -p

The sum of the two notes above would lead to an example run of this recipe as follows:

autopkg run ProPresetsAfterEffectsCC2020.munki -p /path/to/Pro_Presets.zip -k VERSION=2020.11.25

            - **Identifier**: `com.github.foigus.munki.ProPresetsAfterEffectsCC2020`

            - **Parent Recipes**: `com.github.foigus.pkg.ProPresetsAfterEffectsCC2020`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/VideoCopilot/OpticalFlaresProPresets1AfterEffectsCC2019.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/VideoCopilot/OpticalFlaresProPresets1AfterEffectsCC2019.munki.recipe)
    - [foigus-recipes/VideoCopilot/OpticalFlaresProPresets1AfterEffectsCC2020.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/VideoCopilot/OpticalFlaresProPresets1AfterEffectsCC2020.munki.recipe)