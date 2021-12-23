# WoodwingStudioInDesignCC2020.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Packages Woodwing Studio for InDesign 2020 and imports it into Munki.

NOTES:
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add this repos via:

autopkg repo-add hjuutilainen-recipes

- Specific pkgs are disabled via InstallerChoices depending on the product that's being installed.  Due to this, the packages are identical--thus force_munkiimport is set to true
- This recipe does not download the Woodwing Studio disk image--feed the disk image into the recipe via the following format:
- This recipe does not attempt to clean up or uninstall the previous name of the product (Smart Connection for 2020)

autopkg run WoodwingStudioInDesignCC2020.munki.recipe -p /path/to/WoodWing_Studio_for_InDesign_and_InCopy_2020_v15.2.0_Build49.dmg

            - **Identifier**: `com.github.foigus.munki.WoodwingSmartConnectionInDesignCC2020`

            - **Parent Recipes**: `None`
