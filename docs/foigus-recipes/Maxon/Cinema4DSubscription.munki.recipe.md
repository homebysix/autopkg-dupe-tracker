# Cinema4DSubscription.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest version of Cinema 4D Subscription and imports it into Munki.

NOTES:
- Set MAJOR_VERSION to the desired major version of Cinema 4D Subscription
- This recipe depends on homebysix's FindAndReplace.  Add homebysix's repo via:

autopkg repo-add homebysix-recipes

            - **Identifier**: `com.github.foigus.munki.Cinema4DSubscription`

            - **Parent Recipes**: `com.github.foigus.pkg.Cinema4DSubscription`