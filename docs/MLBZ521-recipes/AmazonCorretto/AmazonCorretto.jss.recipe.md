# AmazonCorretto.jss.recipe

            _Last updated 2021-12-23 20:01:49Z_

            - **Description**: Downloads the Amazon Corretto OpenJDK, builds a package, and uploads it to the JSS.

Optionally, this package will pull out the JVM Version which can be used with a Smart Group pointing to an extension attribute to determine latest version.  Use the EXTENSION_ATTRIBUTE override variable to use your current EA.

The JDK Major Version can be specified using the override variable "JDK_MAJOR_VERSION".  Currently available from Amazon are the 8 and 11 JDKs.

            - **Identifier**: `com.github.mlbz521.jss.AmazonCorrettoOpenJDK`

            - **Parent Recipes**: `com.github.mlbz521.pkg.AmazonCorrettoOpenJDK`


## Warnings

- These recipes have duplicate URLDownloader URLs:
    - [MLBZ521-recipes/AmazonCorretto/AmazonCorretto.download.recipe](/autopkg-dupe-tracker/MLBZ521-recipes/AmazonCorretto/AmazonCorretto.download.recipe)
    - [MLBZ521-recipes/AmazonCorretto/AmazonCorretto.pkg.recipe](/autopkg-dupe-tracker/MLBZ521-recipes/AmazonCorretto/AmazonCorretto.pkg.recipe)
    - [MLBZ521-recipes/AmazonCorretto/AmazonCorretto.jss.recipe](/autopkg-dupe-tracker/MLBZ521-recipes/AmazonCorretto/AmazonCorretto.jss.recipe)

- These recipes have duplicate CURLDownloader URLs:
    - [MLBZ521-recipes/AmazonCorretto/AmazonCorretto.download.recipe](/autopkg-dupe-tracker/MLBZ521-recipes/AmazonCorretto/AmazonCorretto.download.recipe)
    - [MLBZ521-recipes/AmazonCorretto/AmazonCorretto.pkg.recipe](/autopkg-dupe-tracker/MLBZ521-recipes/AmazonCorretto/AmazonCorretto.pkg.recipe)
    - [MLBZ521-recipes/AmazonCorretto/AmazonCorretto.jss.recipe](/autopkg-dupe-tracker/MLBZ521-recipes/AmazonCorretto/AmazonCorretto.jss.recipe)