# FirefoxAutoconfig.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads Firefox disk image, builds a package, including autoconfig 
resources (typically as generated via the CCK2 tool), then imports the pkg into
your Munki repo.

Place the autoconfig.zip  in the same directory as the recipe. You may 
optionally use a different name by setting AUTOCONFIG_FILENAME.
Firefox 35 and later require an AUTOCONFIG_DIR of "Contents/Resources"; 
pre-34 requires "Content/MacOS". Firefox 34 is not supported by this recipe. 
ORG_NAME is inserted into the pkg name to distinguish a vanilla 
"Firefox-35.0.pkg" from "Firefox_PretendCo-35.0.pkg". You might consider setting
a unique PKG_ID to differentiate your org's "flavor" of Firefox.

Values for RELEASE correspond to directories here: 
    http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/
Some useful values are: 
    'latest', 'latest-10.0esr', 'latest-esr', 'latest-3.6', 'latest-beta'
LOCALE corresponds to directories at 
    http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/$FIREFOX_BUILD/mac/
Examples include 'en-US', 'de', 'ja-JP-mac', 'sv-SE', and 'zh-TW'

No idea if all Firefox builds are available in all the same localizations, 
so you may need to verify that any particular combination is offered.

            - **Identifier**: `com.github.gregneagle.munki.FirefoxAutoconfig`

            - **Parent Recipes**: `com.github.gregneagle.pkg.FirefoxAutoconfig`


## Warnings

- These recipes have duplicate NAMEs:
    - [gregneagle-recipes/Mozilla/FirefoxAutoconfig.munki.recipe](/autopkg-dupe-tracker/gregneagle-recipes/Mozilla/FirefoxAutoconfig.munki.recipe)
    - [mosen-recipes/Mozilla/FirefoxESRPolicies.munki.recipe](/autopkg-dupe-tracker/mosen-recipes/Mozilla/FirefoxESRPolicies.munki.recipe)
    - [wardsparadox-recipes/Mozilla/FirefoxPolicies.munki.recipe](/autopkg-dupe-tracker/wardsparadox-recipes/Mozilla/FirefoxPolicies.munki.recipe)
    - [recipes/Mozilla/Firefox.munki.recipe](/autopkg-dupe-tracker/recipes/Mozilla/Firefox.munki.recipe)
    - [recipes/Mozilla/FirefoxSignedPkg.munki.recipe](/autopkg-dupe-tracker/recipes/Mozilla/FirefoxSignedPkg.munki.recipe)