# Firefox.jss.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads Firefox disk image and builds a package, then uploads to the JSS.
Values for FIREFOX_BUILD correspond to directories here: http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/
Some useful values are: 'latest', 'latest-10.0esr', 'latest-esr', 'latest-3.6', 'latest-beta'
LOCALE corresponds to directories at http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/$FIREFOX_BUILD/mac/
Examples include 'en-US', 'de', 'ja-JP-mac', 'sv-SE', and 'zh-TW'
No idea if all Firefox builds are available in all the same localizations, so you may need to verify that any particular
combination is offered.

            - **Identifier**: `com.github.novaksam.jss.Firefox`

            - **Parent Recipes**: `com.github.autopkg.pkg.Firefox_EN`

## Warnings

- These recipes have duplicate filenames:
    - [rtrouton-recipes/JSS/Firefox.jss.recipe](/autopkg-dupe-tracker/rtrouton-recipes/JSS/Firefox.jss.recipe)
    - [jss-recipes/Firefox/Firefox.jss.recipe](/autopkg-dupe-tracker/jss-recipes/Firefox/Firefox.jss.recipe)
    - [novaksam-recipes/Firefox/Firefox.jss.recipe](/autopkg-dupe-tracker/novaksam-recipes/Firefox/Firefox.jss.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [rtrouton-recipes/JSS/Firefox.jss.recipe](/autopkg-dupe-tracker/rtrouton-recipes/JSS/Firefox.jss.recipe)
    - [jss-recipes/Firefox/Firefox.jss.recipe](/autopkg-dupe-tracker/jss-recipes/Firefox/Firefox.jss.recipe)
    - [novaksam-recipes/Firefox/Firefox.jss.recipe](/autopkg-dupe-tracker/novaksam-recipes/Firefox/Firefox.jss.recipe)

- These recipes have duplicate NAMEs:
    - [rtrouton-recipes/JSS/Firefox.jss.recipe](/autopkg-dupe-tracker/rtrouton-recipes/JSS/Firefox.jss.recipe)
    - [jss-recipes/Firefox/Firefox.jss.recipe](/autopkg-dupe-tracker/jss-recipes/Firefox/Firefox.jss.recipe)
    - [jss-recipes/Firefox/FirefoxAutoconfig.jss.recipe](/autopkg-dupe-tracker/jss-recipes/Firefox/FirefoxAutoconfig.jss.recipe)
    - [novaksam-recipes/Firefox/Firefox.jss.recipe](/autopkg-dupe-tracker/novaksam-recipes/Firefox/Firefox.jss.recipe)
    - [scriptingosx-recipes/FirefoxPrefs/FirefoxPrefs.jss.recipe](/autopkg-dupe-tracker/scriptingosx-recipes/FirefoxPrefs/FirefoxPrefs.jss.recipe)
    - [golbiga-recipes/JSS/FirefoxAutoconfig.jss.recipe](/autopkg-dupe-tracker/golbiga-recipes/JSS/FirefoxAutoconfig.jss.recipe)