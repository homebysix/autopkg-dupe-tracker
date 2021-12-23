# Modul8.munki.recipe

_Last updated 2021-12-23 19:58:07Z_

- **Description**: Downloads the latest verison of Modul8 and imports it into a munki_repo. Final munki item will copy the entire contents of the modul8vX folder, including documentation, modules, etc. Requires making an override and supplying your Modul8 license serial number in order to get the latest download URL.

- **Identifier**: `com.github.apizz.munki.modul8`

- **Parent Recipes**: `com.github.apizz.download.modul8`