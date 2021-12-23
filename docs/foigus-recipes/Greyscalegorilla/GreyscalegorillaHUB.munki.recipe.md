# GreyscalegorillaHUB.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Packages Greyscalegorilla HUB plugin for Cinema 4D and imports it into Munki.

NOTES:
- This recipe needs the version of Cinema 4D to be defined in the Input, since the installation is path-specific and hopefully _should_ work for many versions of Cinema 4D
- This recipe needs the version of Greyscalegorilla HUB to be defined in the Input.  Right _now_ the "version.txt" file inside the download says version "1206", while the plugin itself says both "1.206" and "OSX_23_Build_117" so I leave this choice to the AutoPkg admin
- This recipe does not download the Greyscalegorilla HUB installation media--feed the compressed file into the recipe via the following format:

autopkg run GreyscalegorillaHUB.munki -p /path/to/the/appropriate/osx_rVERSION_greyscalegorillahub.zip

            - **Identifier**: `com.github.foigus.munki.GreyscalegorillaHUB`

            - **Parent Recipes**: `com.github.foigus.pkg.GreyscalegorillaHUB`
