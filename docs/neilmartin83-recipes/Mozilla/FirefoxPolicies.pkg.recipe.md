# FirefoxPolicies.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads Firefox disk image and builds a package, copying your
'distribution/policies.json' file into the application bundle. Adapted from 
Greg Neagle's FirefoxAutoconfig.pkg recipe.

Create a 'distribution' directory in the same directory as the recipe
and copy your policies.json file there. Firefox versions below 60 are not 
supported by this recipe. ORG_NAME is inserted into the pkg name to distinguish 
a vanilla "Firefox-60.0.pkg" from "Firefox_PretendCo-60.0.pkg". You might 
consider setting a unique PKG_ID to differentiate your org's "flavor" of Firefox.

Values for RELEASE correspond to directories here: 
    http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/
Some useful values are: 
    'latest', 'latest-10.0esr', 'latest-esr', 'latest-3.6', 'latest-beta'
LOCALE corresponds to directories at 
    http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/$FIREFOX_BUILD/mac/
Examples include 'en_GB', 'en-US', 'de', 'ja-JP-mac', 'sv-SE', and 'zh-TW'

No idea if all Firefox builds are available in all the same localizations, 
so you may need to verify that any particular combination is offered.

            - **Identifier**: `com.github.neilmartin83.pkg.FirefoxPolicies`

            - **Parent Recipes**: `com.github.autopkg.download.firefox-rc-en_US`


## Warnings

- These recipes have duplicate NAMEs:
    - [rtrouton-recipes/Firefox/Firefox.pkg.recipe](/autopkg-dupe-tracker/rtrouton-recipes/Firefox/Firefox.pkg.recipe)
    - [gregneagle-recipes/Mozilla/FirefoxAutoconfig.pkg.recipe](/autopkg-dupe-tracker/gregneagle-recipes/Mozilla/FirefoxAutoconfig.pkg.recipe)
    - [mosen-recipes/Mozilla/FirefoxESRPolicies.pkg.recipe](/autopkg-dupe-tracker/mosen-recipes/Mozilla/FirefoxESRPolicies.pkg.recipe)
    - [neilmartin83-recipes/Mozilla/FirefoxPolicies.pkg.recipe](/autopkg-dupe-tracker/neilmartin83-recipes/Mozilla/FirefoxPolicies.pkg.recipe)
    - [recipes/Mozilla/Firefox.pkg.recipe](/autopkg-dupe-tracker/recipes/Mozilla/Firefox.pkg.recipe)
    - [recipes/Mozilla/FirefoxSignedPkg.pkg.recipe](/autopkg-dupe-tracker/recipes/Mozilla/FirefoxSignedPkg.pkg.recipe)