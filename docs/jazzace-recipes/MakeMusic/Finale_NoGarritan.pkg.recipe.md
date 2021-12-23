# Finale_NoGarritan.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Creates an installer pkg for Finale (v.25 and later) that installs properly using a management system.
This recipe uses the PackageRequired option and assumes you are specifying the Disk Image that contains 
the Finale Installer(s). For example:

autopkg run Finale_NoGarritan.pkg --pkg /path/to/Finale26.2.dmg

The file silentInstallerChoices.plist must be in the same directory as the recipe you are running
(usually AutoPkg's RecipeOverrides directory). You can obtain a copy of the file from the same
directory as this repo or linked on MakeMusic's Help Center article:

https://makemusic.zendesk.com/hc/en-us/articles/115007423647-Commands-to-silently-install-Finale-unattended-installer-#installMac


            - **Identifier**: `com.github.jazzace.pkg.finalenogarritan`

            - **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate NAMEs:
    - [dataJAR-recipes/Finale 26-Trial/Finale26-Trial.pkg.recipe](/autopkg-dupe-tracker/dataJAR-recipes/Finale 26-Trial/Finale26-Trial.pkg.recipe)
    - [jazzace-recipes/MakeMusic/Finale_NoGarritan.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/MakeMusic/Finale_NoGarritan.pkg.recipe)
    - [neilmartin83-recipes/Finale/Finale.pkg.recipe](/autopkg-dupe-tracker/neilmartin83-recipes/Finale/Finale.pkg.recipe)