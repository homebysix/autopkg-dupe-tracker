# Firefox.jamf.recipe.yaml

            _Last updated 2021-12-23 20:01:51Z_

            - **Description**: Downloads the latest version of Firefox and makes a pkg. Then, uploads the package to the Jamf Pro Server and creates a Self Service Policy and Smart Group. Values for FIREFOX_BUILD correspond to directories here: http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/
Some useful values are: 'latest', 'latest-10.0esr', 'latest-esr', 'latest-3.6', 'latest-beta'
LOCALE corresponds to directories at http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/$FIREFOX_BUILD/mac/
Examples include 'en-US', 'de', 'ja-JP-mac', 'sv-SE', and 'zh-TW'
No idea if all Firefox builds are available in all the same localizations, so you may need to verify that any particular combination is offered.


            - **Identifier**: `com.github.grahampugh.recipes.jamf.Firefox`

            - **Parent Recipes**: `com.github.autopkg.pkg.Firefox_EN`
