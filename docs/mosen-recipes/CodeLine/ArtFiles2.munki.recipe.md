# ArtFiles2.munki.recipe

        _Last updated 2021-12-23 19:58:07Z_

        - **Description**: 
Re-packs the Art Files 2 zip into a dmg, and imports into munki.

The download URL has a dmg extension but redirects to a zip archive containing an app bundle.
The recipe will unpack the zip file, and then create a DMG for the .app. This is imported into munki and
will be installed as a CopyFromDmg style package.


        - **Identifier**: `com.github.mosen.munki.ArtFiles2`

        - **Parent Recipes**: `com.github.mosen.download.ArtFiles2`