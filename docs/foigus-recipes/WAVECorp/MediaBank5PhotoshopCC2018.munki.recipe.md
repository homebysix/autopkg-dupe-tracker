# MediaBank5PhotoshopCC2018.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Repackage the MediaBank 5 plugin for Photoshop CC 2018 and import it into Munki.  This recipe does not download the MediaBank 5 tar.gz archive--feed the tar.gz archive into the recipe via the following format:

autopkg run MediaBank5PhotoshopCC2018.munki -p /path/to/MediaBank_Installer_osx_CC_2018_20201009.tar.gz

            - **Identifier**: `com.github.foigus.munki.MediaBank5PhotoshopCC2018`

            - **Parent Recipes**: `com.github.foigus.pkg.MediaBank5PhotoshopCC2018`
