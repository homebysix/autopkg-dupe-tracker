# SendtoKindle.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads latest Send to Kindle and modifies a postinstall to exit 0 in case of scripting failure.

NOTE:
- This recipe depends on facebook's FileAppender.  Add facebook's repo via:
autopkg repo-add https://github.com/facebook/Recipes-for-AutoPkg

            - **Identifier**: `com.github.foigus.pkg.SendToKindle`

            - **Parent Recipes**: `com.github.foigus.download.SendToKindle`

## Warnings

- These recipes have duplicate URLDownloader URLs:
    - [foigus-recipes/Amazon/SendtoKindle.download.recipe](/autopkg-dupe-tracker/foigus-recipes/Amazon/SendtoKindle.download.recipe)
    - [foigus-recipes/Amazon/SendtoKindle.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/Amazon/SendtoKindle.pkg.recipe)

- These recipes have duplicate CURLDownloader URLs:
    - [foigus-recipes/Amazon/SendtoKindle.download.recipe](/autopkg-dupe-tracker/foigus-recipes/Amazon/SendtoKindle.download.recipe)
    - [foigus-recipes/Amazon/SendtoKindle.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/Amazon/SendtoKindle.pkg.recipe)