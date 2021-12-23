# Mathematica.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Imports Mathematica into Munki.

This is designed to be run against a local .dmg. To run this recipe successfully, you must:

- Register for a Wolfram ID.
- Download the latest version of Mathematica using the Wolfram Research Mathematica Download Manager (WRMDM). The WRMDM downloads the Mathematica dmg to your Downloads folder.
- Run the following command:

autopkg run -vvv -p /path/to/downloaded_mathematica_dmg Mathematica.munki

A postinstall_script that adds Mathematica to the client application firewall is included in this repo. If you wish to use this, add it to your recipe override.

            - **Identifier**: `com.github.andrewvalentine.munki.Mathematica`

            - **Parent Recipes**: `None`