# AssetsInDesignCC2018Plugin.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads Assets Plugin and imports it into Munki for installation for InDesign CC 2018.

NOTES:
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add this repo via:

autopkg repo-add hjuutilainen-recipes

- Specific pkgs are enabled via InstallerChoices depending on the product that's being installed.  Due to this, the packages are identical--thus force_munkiimport is set to true
- This recipe does not download the Assets package--feed the package into the recipe via the following format:

autopkg run AssetsInDesignCC2018Plugin.munki -p /path/WoodWing\ Assets\ for\ InDesignCC2018.pkg

            - **Identifier**: `com.github.foigus.munki.AssetsInDesignCC2018Plugin`

            - **Parent Recipes**: `com.github.foigus.download.AssetsInDesignPlugin`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/WoodWing/AssetsInDesignCC2018Plugin.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/AssetsInDesignCC2018Plugin.munki.recipe)
    - [foigus-recipes/WoodWing/AssetsInDesignCC2020Plugin.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/AssetsInDesignCC2020Plugin.munki.recipe)