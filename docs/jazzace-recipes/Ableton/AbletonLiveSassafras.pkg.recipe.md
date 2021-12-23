# AbletonLiveSassafras.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the most recent version of Ableton Live and creates an installer package
for use when licenses are managed using Sassafras AllSight/LabSight/KeySight (KeyServer).
The major version and edition is specified through input variables (see the parent download recipe).
In order to avoid pkgbuild errors, the SoundCloud extension is removed from the app bundle and
the version number (from CFBundleShortVersionString) is simplified to eliminate parenthetical 
build info (the homebysix-recipes repo is required).
An Options.txt file is added (via postinstall script) in /Library/Preferences/Ableton/Live %version%/ as per 
https://help.ableton.com/hc/en-us/articles/360020530999-Authorizing-Live-for-all-users-on-macOS-with-Sassafras


            - **Identifier**: `com.github.jazzace.pkg.AbletonLiveSassafras`

            - **Parent Recipes**: `com.github.jazzace.download.AbletonLive`
