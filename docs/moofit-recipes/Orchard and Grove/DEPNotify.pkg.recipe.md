# DEPNotify.pkg.recipe

        _Last updated 2021-12-23 20:01:50Z_

        - **Description**: Downloads a specific version of DEPNotify, as determined by the input field below, and adds in additional
resources to allow for customisation.

The additional resources should belong in a folder alongside this recipe when configuring an override:

1. Create a folder next to the override, and add your resources.
2. Add the name of the folder to the RESOURCES key variable below
3. The Copier processor will copy the contents of the folder into the "/Library/Application Support/DEPNotify"
   folder.
4. Call these assets with the various commands after the pkg has been deployed.

Bear in mind, by repackaging the installer, it will remove the original signature.


        - **Identifier**: `com.github.moofit-recipes.pkg.DEPNotify`

        - **Parent Recipes**: `com.github.moofit-recipes.download.DEPNotify`


## Warnings

- These recipes have duplicate filenames:
    - [moofit-recipes/Orchard and Grove/DEPNotify.pkg.recipe](/autopkg-dupe-tracker/moofit-recipes/Orchard and Grove/DEPNotify.pkg.recipe)
    - [rderewianko-recipes/DEPNotify/DEPNotify.pkg.recipe](/autopkg-dupe-tracker/rderewianko-recipes/DEPNotify/DEPNotify.pkg.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [moofit-recipes/Orchard and Grove/DEPNotify.pkg.recipe](/autopkg-dupe-tracker/moofit-recipes/Orchard and Grove/DEPNotify.pkg.recipe)
    - [rderewianko-recipes/DEPNotify/DEPNotify.pkg.recipe](/autopkg-dupe-tracker/rderewianko-recipes/DEPNotify/DEPNotify.pkg.recipe)

- These recipes have duplicate NAMEs:
    - [moofit-recipes/Orchard and Grove/DEPNotify.pkg.recipe](/autopkg-dupe-tracker/moofit-recipes/Orchard and Grove/DEPNotify.pkg.recipe)
    - [rderewianko-recipes/DEPNotify/DEPNotify.pkg.recipe](/autopkg-dupe-tracker/rderewianko-recipes/DEPNotify/DEPNotify.pkg.recipe)