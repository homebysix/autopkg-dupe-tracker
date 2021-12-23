# FirefoxAutoconfig.jss.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads Firefox disk image and builds a package, including autoconfig 
resources (typically as generated via the CCK2 tool). 

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
so you may need to verify that any particular combination is offered. Then, uploads to the JSS.

            - **Identifier**: `com.github.golbiga.jss.FirefoxAutoconfig`

            - **Parent Recipes**: `com.github.gregneagle.pkg.FirefoxAutoconfig`


## Warnings

- These recipes have duplicate filenames:
    - [jss-recipes/Firefox/FirefoxAutoconfig.jss.recipe](/autopkg-dupe-tracker/jss-recipes/Firefox/FirefoxAutoconfig.jss.recipe)
    - [golbiga-recipes/JSS/FirefoxAutoconfig.jss.recipe](/autopkg-dupe-tracker/golbiga-recipes/JSS/FirefoxAutoconfig.jss.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [jss-recipes/Firefox/FirefoxAutoconfig.jss.recipe](/autopkg-dupe-tracker/jss-recipes/Firefox/FirefoxAutoconfig.jss.recipe)
    - [golbiga-recipes/JSS/FirefoxAutoconfig.jss.recipe](/autopkg-dupe-tracker/golbiga-recipes/JSS/FirefoxAutoconfig.jss.recipe)

- These recipes have duplicate NAMEs:
    - [rtrouton-recipes/JSS/Firefox.jss.recipe](/autopkg-dupe-tracker/rtrouton-recipes/JSS/Firefox.jss.recipe)
    - [jss-recipes/Firefox/Firefox.jss.recipe](/autopkg-dupe-tracker/jss-recipes/Firefox/Firefox.jss.recipe)
    - [jss-recipes/Firefox/FirefoxAutoconfig.jss.recipe](/autopkg-dupe-tracker/jss-recipes/Firefox/FirefoxAutoconfig.jss.recipe)
    - [novaksam-recipes/Firefox/Firefox.jss.recipe](/autopkg-dupe-tracker/novaksam-recipes/Firefox/Firefox.jss.recipe)
    - [scriptingosx-recipes/FirefoxPrefs/FirefoxPrefs.jss.recipe](/autopkg-dupe-tracker/scriptingosx-recipes/FirefoxPrefs/FirefoxPrefs.jss.recipe)
    - [golbiga-recipes/JSS/FirefoxAutoconfig.jss.recipe](/autopkg-dupe-tracker/golbiga-recipes/JSS/FirefoxAutoconfig.jss.recipe)