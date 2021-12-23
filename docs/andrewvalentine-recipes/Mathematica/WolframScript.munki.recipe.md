# WolframScript.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Imports WolframScript into Munki.

This is designed to be run against a local .dmg. To run this recipe successfully, you must:

- Register for a Wolfram ID.
- Download the latest version of Mathematica using the Wolfram Research Mathematica Download Manager (WRMDM). The WRMDM downloads the Mathematica dmg to your Downloads folder.
- Mount the dmg.
- Run the following command:

autopkg run -vvv -p /Volumes/Mathematica/WolframScript.pkg Mathematica.munki

WolframScript is typically an add on for Mathematica. If you wish to bundle this with your organisational install of Mathematica, add the WolframScript item as an update_for your Mathematica item in your recipe override.

            - **Identifier**: `com.github.andrewvalentine.munki.WolframScript`

            - **Parent Recipes**: `None`