# Adobe CC Cleaner.jss-triggeronly.recipe.yaml

_Last updated 2021-12-23 19:58:08Z_

- **Description**: Downloads the latest version of Adobe Creative Cloud Cleaner and makes a pkg of it then uploads it to the JSS. the postinstall script runs the cleaner, which removes all Adobe CC apps from a client. The app is also moved to the Utilities folder so that it can be used subsequently, but is not obvious to the user.

- **Identifier**: `com.github.grahampugh.recipes.jss-triggeronly.AdobeCCCleaner`

- **Parent Recipes**: `com.github.blackthroat.pkg.AdobeCreativeCloudCleanerTool`