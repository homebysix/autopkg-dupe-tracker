# GoogleDrive.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of Google Drive (previously File Stream) and imports it into a munki repo.

Since Google Drive has macOS architecture specific PKGs that won't be installed, this will cause an endless install loop if the applicable PKG receipts aren't marked as optional. To address this, these items are added in the Input variable dictionary under the pkg_ids_set_optional_true key.

If an admin wishes to use this same recipe to manage a single Google Drive PKG installer with 2 separate munki items - 1 for arm64, 1 for x86_64 - simply remove the applicable pkg ids from the pkg_ids_set_optional_true array.

            - **Identifier**: `com.github.apizz.munki.GoogleDrive`

            - **Parent Recipes**: `com.github.nstrauss.pkg.GoogleDrive`


## Warnings

- These recipes have duplicate filenames:
    - [apizz-recipes/Google_Drive/GoogleDrive.munki.recipe](/autopkg-dupe-tracker/apizz-recipes/Google_Drive/GoogleDrive.munki.recipe)
    - [dankeller-recipes/GoogleDrive/GoogleDrive.munki.recipe](/autopkg-dupe-tracker/dankeller-recipes/GoogleDrive/GoogleDrive.munki.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [apizz-recipes/Google_Drive/GoogleDrive.munki.recipe](/autopkg-dupe-tracker/apizz-recipes/Google_Drive/GoogleDrive.munki.recipe)
    - [dankeller-recipes/GoogleDrive/GoogleDrive.munki.recipe](/autopkg-dupe-tracker/dankeller-recipes/GoogleDrive/GoogleDrive.munki.recipe)

- These recipes have duplicate NAMEs:
    - [apizz-recipes/Google_Drive/GoogleDrive_app.munki.recipe](/autopkg-dupe-tracker/apizz-recipes/Google_Drive/GoogleDrive_app.munki.recipe)
    - [apizz-recipes/Google_Drive/GoogleDrive.munki.recipe](/autopkg-dupe-tracker/apizz-recipes/Google_Drive/GoogleDrive.munki.recipe)
    - [dankeller-recipes/GoogleDrive/GoogleDrive.munki.recipe](/autopkg-dupe-tracker/dankeller-recipes/GoogleDrive/GoogleDrive.munki.recipe)