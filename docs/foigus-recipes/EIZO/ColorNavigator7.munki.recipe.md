# ColorNavigator7.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest ColorNavigator installer and imports it into Munki.

NOTES:
- Requiring a logout since the GUI installer reopens ColorNavigator, but not from the CLI.  Also, updating calibration software while a user is using the monitor wouldn't be good.
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add this repo via:

autopkg repo-add hjuutilainen-recipes

            - **Identifier**: `com.github.foigus.munki.ColorNavigator7`

            - **Parent Recipes**: `com.github.foigus.pkg.ColorNavigator7`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/EIZO/ColorNavigator.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/EIZO/ColorNavigator.munki.recipe)
    - [foigus-recipes/EIZO/ColorNavigator7.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/EIZO/ColorNavigator7.munki.recipe)