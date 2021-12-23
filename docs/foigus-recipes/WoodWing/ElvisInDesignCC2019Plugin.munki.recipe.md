# ElvisInDesignCC2019Plugin.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads Elvis Plugin and imports it into Munki for installation for InDesign CC 2019.

NOTES:
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add this repo via:

autopkg repo-add hjuutilainen-recipes

- Specific pkgs are enabled via InstallerChoices depending on the product that's being installed.  Due to this, the packages are identical--thus force_munkiimport is set to true
- This recipe does not download the Elvis package--feed the package into the recipe via the following format:

autopkg run ElvisInDesignCC2019Plugin.munki -p /path/to/Elvis\ InDesign.pkg

            - **Identifier**: `com.github.foigus.munki.ElvisInDesignCC2019Plugin`

            - **Parent Recipes**: `com.github.foigus.download.ElvisInDesignPlugin`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/WoodWing/ElvisInDesignCC2019Plugin.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/ElvisInDesignCC2019Plugin.munki.recipe)
    - [foigus-recipes/WoodWing/ElvisInDesignCC2015Plugin.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/ElvisInDesignCC2015Plugin.munki.recipe)
    - [foigus-recipes/WoodWing/ElvisInDesignCC2018Plugin.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/WoodWing/ElvisInDesignCC2018Plugin.munki.recipe)