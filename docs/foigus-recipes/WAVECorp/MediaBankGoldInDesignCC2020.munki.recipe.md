# MediaBankGoldInDesignCC2020.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Repackage the MediaBank Gold plugin for InDesign CC 2020 and import it into Munki.  This recipe does not download the MediaBank Gold tar archive--feed the tar archive into the recipe via the following format:

autopkg run MediaBankGoldInDesignCC2020.munki -p /path/to/mediabankgold_installer_osx_2020_20200111.tar.gz

            - **Identifier**: `com.github.foigus.munki.MediaBankGoldInDesignCC2020`

            - **Parent Recipes**: `com.github.foigus.pkg.MediaBankGoldInDesignCC2020`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/WAVECorp/MediaBankGoldInDesignCC2018.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WAVECorp/MediaBankGoldInDesignCC2018.munki.recipe)
    - [foigus-recipes/WAVECorp/MediaBankGoldInDesignCC2020.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WAVECorp/MediaBankGoldInDesignCC2020.munki.recipe)