# TeradiciClientBeta.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads latest Teradici client beta disk image and builds an installation package.

NOTEs:
- Teradici's client beta has no version information, thus the requirement for a package to have some semblance of versioning
- This recipe depends on homebysix's FindAndReplace.  Add homebysix's repo via:

autopkg repo-add homebysix-recipes

            - **Identifier**: `com.github.foigus.pkg.teradiciclientbeta`

            - **Parent Recipes**: `com.github.foigus.download.teradiciclientbeta`
