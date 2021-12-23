# ColorNavigator7.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest ColorNavigator 7 installer and modifies a postinstall to no longer open the ColorNavigator 7 window following installation. 

NOTES:
- POSTINSTALL_SCRIPT_PATH must be set to reflect the location of the "postinstall" script--it can point back to the postinstall in the directory of the original recipe, but due to overrides it must be a piece of override-able INPUT
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add hjuutilainen's repo via:
autopkg repo-add hjuutilainen-recipes

- This recipe depends on jessepeterson's ModeChanger.  Add jessepeterson's repo via:
autopkg repo-add jessepeterson-recipes

            - **Identifier**: `com.github.foigus.pkg.ColorNavigator7`

            - **Parent Recipes**: `com.github.foigus.download.ColorNavigator7`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/EIZO/ColorNavigator7.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/EIZO/ColorNavigator7.pkg.recipe)
    - [foigus-recipes/EIZO/ColorNavigator.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/EIZO/ColorNavigator.pkg.recipe)