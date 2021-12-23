# Cinema4DImporterPluginAfterEffectsCC2020.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Packages Cinema 4D Importer plugin for After Effects CC 2020.

NOTES:

- This recipe requires installing BOTH AutoPkg AND Cinema 4D itself.  IDEALLY this would occur in a clean virtual machine, and is not intended to occur on an AutoPkg "server".  Thank Maxon's cross-platform Java-based installer for this incredibly strange recipe
- I'm skipping CodeSignatureVerifier since presumably Cinema 4D has been sourced from a trusted location and then manually installed
- This recipe is dependent on Elliot Jordan's VersionSplitter processor.  To add his repo:

autopkg repo-add homebysix-recipes

            - **Identifier**: `com.github.foigus.pkg.Cinema4DImporterPluginAfterEffectsCC2020`

            - **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/Maxon/Cinema4DImporterPluginAfterEffectsCC2020.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/Maxon/Cinema4DImporterPluginAfterEffectsCC2020.pkg.recipe)
    - [foigus-recipes/Maxon/Cinema4DImporterPluginAfterEffectsCC2019.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/Maxon/Cinema4DImporterPluginAfterEffectsCC2019.pkg.recipe)