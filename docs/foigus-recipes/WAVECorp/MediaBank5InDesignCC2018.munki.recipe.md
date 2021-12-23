# MediaBank5InDesignCC2018.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Repackage the MediaBank 5 plugin for InDesign CC 2018 and import it into Munki.  This recipe does not download the MediaBank 5 tar.gz archive--feed the tar.gz archive into the recipe via the following format:

autopkg run MediaBank5InDesignCC2018.munki -p /path/to/MediaBank_Installer_osx_CC_2018_20201009.tar.gz

            - **Identifier**: `com.github.foigus.munki.MediaBank5InDesignCC2018`

            - **Parent Recipes**: `com.github.foigus.pkg.MediaBank5InDesignCC2018`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/WAVECorp/MediaBank5InDesignCC2018.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WAVECorp/MediaBank5InDesignCC2018.munki.recipe)
    - [foigus-recipes/WAVECorp/MediaBank5InDesignCC2020.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WAVECorp/MediaBank5InDesignCC2020.munki.recipe)