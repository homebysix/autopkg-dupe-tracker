# TeradiciClient.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads latest Teradici client disk image, builds an installation package, and imports it into Munki.

NOTES:

- Teradici's client has no version information, thus the requirement for a package to have some semblance of versioning
- The USB redirection is based on a kext that uses Team ID RU4LW7W32C--this will need to be approved either manually or via a MDM

            - **Identifier**: `com.github.foigus.munki.teradiciclient`

            - **Parent Recipes**: `com.github.foigus.pkg.teradiciclient`
