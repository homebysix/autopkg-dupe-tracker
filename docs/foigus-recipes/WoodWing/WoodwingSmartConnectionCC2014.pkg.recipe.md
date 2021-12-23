# WoodwingSmartConnectionCC2014.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Packages Smart Connection CC 2014 for installation.

NOTES:
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add hjuutilainen's repo via:

autopkg repo-add hjuutilainen-recipes

- This recipe does not fix the InDesign Server packages, since these are very likely to be installed by hand
- This recipe does not download the Smart Connection disk image--feed the disk image into the recipe via the following format:

autopkg run WoodwingSmartConnectionCC2015.pkg -p /path/to/Smart_Connection_for_Adobe_CC_2014_v10.2.2_Build75.dmg

            - **Identifier**: `com.github.foigus.pkg.WoodwingSmartConnectionCC2014`

            - **Parent Recipes**: `None`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionCC2014.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionCC2014.pkg.recipe)
    - [foigus-recipes/WoodWing/WoodwingSmartConnectionCC2015.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/WoodwingSmartConnectionCC2015.pkg.recipe)