# MediaBankGoldIllustratorCC2018.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Repackage the MediaBank Gold plugin for Illustrator CC 2018 and import it into Munki.  This recipe does not download the MediaBank Gold tar archive--feed the tar archive into the recipe via the following format:

autopkg run MediaBankGoldIllustratorCC2018.munki -p /path/to/MediaBankGold_Installer_osx_CC_2018_20190127.tar

            - **Identifier**: `com.github.foigus.munki.MediaBankGoldIllustratorCC2018`

            - **Parent Recipes**: `com.github.foigus.pkg.MediaBankGoldIllustratorCC2018`
