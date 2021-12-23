# WoodwingSmartConnectionInDesignCC2018.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Packages InDesign Smart Connection for installation for InDesign CC 2018 and imports it into Munki

NOTES:
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add this repos via:

autopkg repo-add hjuutilainen-recipes

- Specific pkgs are disabled via InstallerChoices depending on the product that's being installed.  Due to this, the packages are identical--thus force_munkiimport is set to true
- This recipe does not download the Smart Connection disk image--feed the disk image into the recipe via the following format:

autopkg run WoodwingSmartConnectionInDesignCC2018.munki -p /path/to/Smart_Connection_for_Adobe_CC_2018_v13.0.0_Build4.dmg

            - **Identifier**: `com.github.foigus.munki.WoodwingSmartConnectionInDesignCC2018`

            - **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignCC2014.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignCC2014.munki.recipe)
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignCC2015.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignCC2015.munki.recipe)
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignCC2018.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignCC2018.munki.recipe)
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignCC2019.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignCC2019.munki.recipe)