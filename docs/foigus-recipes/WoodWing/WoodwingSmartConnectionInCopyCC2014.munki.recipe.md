# WoodwingSmartConnectionInCopyCC2014.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Packages InCopy Smart Connection for installation for InCopy CC 2014 and imports it into Munki

NOTES:
- This recipe depends on keeleysam's MunkiPkginfoReceiptsEditor and hjuutilainen's ChecksumVerifier.  Add these repos via:

autopkg repo-add keeleysam-recipes
autopkg repo-add hjuutilainen-recipes

- Specific pkgs are disabled via InstallerChoices depending on the product that's being installed.  Due to this, the packages are identical--thus force_munkiimport is set to true
- This recipe does not download the Smart Connection disk image--feed the disk image into the recipe via the following format:

autopkg run WoodwingSmartConnectionInCopyCC2014.munki -p /path/to/Smart_Connection_for_Adobe_CC_2014_v10.2.2_Build75.dmg

            - **Identifier**: `com.github.foigus.munki.WoodwingSmartConnectionInCopyCC2014`

            - **Parent Recipes**: `com.github.foigus.pkg.WoodwingSmartConnectionCC2014`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionInCopyCC2018.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionInCopyCC2018.munki.recipe)
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionInCopyCC2014.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionInCopyCC2014.munki.recipe)
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionInCopyCC2015.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionInCopyCC2015.munki.recipe)