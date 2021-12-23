# GoogleDrive_app.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of Google Drive (previously File Stream) and imports it into a munki repo.

Since Google Drive has macOS architecture specific PKGs that won't be installed, this will cause an endless install loop if the applicable PKG receipts aren't marked as optional. Unlike the sister GoogleDrive.munki.recipe which uses the PKG receipts to determine the install status, this recipe instead refers to the installed app version.

            - **Identifier**: `com.github.apizz.munki.GoogleDrive_app`

            - **Parent Recipes**: `com.github.nstrauss.pkg.GoogleDrive`


## Warnings

- These recipes have duplicate NAMEs:
    - [apizz-recipes/Google_Drive/GoogleDrive_app.munki.recipe](/autopkg-dupe-tracker/apizz-recipes/Google_Drive/GoogleDrive_app.munki.recipe)
    - [apizz-recipes/Google_Drive/GoogleDrive.munki.recipe](/autopkg-dupe-tracker/apizz-recipes/Google_Drive/GoogleDrive.munki.recipe)
    - [dankeller-recipes/GoogleDrive/GoogleDrive.munki.recipe](/autopkg-dupe-tracker/dankeller-recipes/GoogleDrive/GoogleDrive.munki.recipe)