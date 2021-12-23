# WoodwingSmartConnectionInDesignDigitalMagazineCC2015.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Packages InDesign Digital Magazine plugins for installation for InDesign CC 2015 and imports it into Munki

NOTES:
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add this repos via:

autopkg repo-add hjuutilainen-recipes

- Specific pkgs are disabled via InstallerChoices depending on the product that's being installed.  Due to this, the packages are identical--thus force_munkiimport is set to true
- This recipe does not download the Smart Connection disk image--feed the disk image into the recipe via the following format:

autopkg run WoodwingSmartConnectionInDesignDigitalMagazineCC2015.munki -p /path/to/Smart_Connection_for_Adobe_CC_2015_v11.2.0_Build42.dmg

            - **Identifier**: `com.github.foigus.munki.WoodwingSmartConnectionInDesignDigitalMagazineCC2015`

            - **Parent Recipes**: `com.github.foigus.pkg.WoodwingSmartConnectionCC2015`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignDigitalMagazineCC2014.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignDigitalMagazineCC2014.munki.recipe)
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignDigitalMagazineCC2015.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionInDesignDigitalMagazineCC2015.munki.recipe)