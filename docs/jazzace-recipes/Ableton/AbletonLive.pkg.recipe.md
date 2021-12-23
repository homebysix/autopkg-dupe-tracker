# AbletonLive.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the most recent version of Ableton Live and creates an installer package.
The major version and edition is specified through input variables (see the parent download recipe).
In order to avoid pkgbuild errors, the SoundCloud extension is removed from the app bundle and
the version number (from CFBundleShortVersionString) is simplified to eliminate parenthetical 
build info (the homebysix-recipes repo is required).
If a new package is created, the temporary files needed during packaging are deleted.



            - **Identifier**: `com.github.jazzace.pkg.AbletonLive`

            - **Parent Recipes**: `com.github.jazzace.download.AbletonLive`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [jazzace-recipes/Ableton/AbletonLive.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/Ableton/AbletonLive.pkg.recipe)
    - [moofit-recipes/Ableton/AbletonLive9.pkg.recipe](/autopkg-dupe-tracker/moofit-recipes/Ableton/AbletonLive9.pkg.recipe)