# TeradiciClientBeta.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads latest Teradici client beta disk image, builds an installation package, and imports it into Munki.

NOTES:

- Teradici's client beta has no version information, thus the requirement for a package to have some semblance of versioning
- The USB redirection is based on a kext that uses Team ID RU4LW7W32C--this will need to be approved either manually or via a MDM
- This recipe depends on homebysix's FindAndReplace.  Add homebysix's repo via:

autopkg repo-add homebysix-recipes

            - **Identifier**: `com.github.foigus.munki.teradiciclientbeta`

            - **Parent Recipes**: `com.github.foigus.pkg.teradiciclientbeta`