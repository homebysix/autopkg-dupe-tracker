# FirefoxESRPolicies.pkg.recipe

_Last updated 2021-12-23 20:01:50Z_

- **Description**: Downloads Firefox disk image and builds a package, injecting a policies.json file as "distribution"

Create a `distribution` directory containing the policies.json in the same directory as the recipe.
You may optionally use a different directory name (inside RECIPE_DIR) by setting DISTRIBUTION_PATH.

Values for RELEASE correspond to directories here:
http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/
Some useful values are:
'latest', 'latest-10.0esr', 'latest-esr', 'latest-3.6', 'latest-beta'
LOCALE corresponds to directories at
http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/$FIREFOX_BUILD/mac/
Examples include 'en-US', 'de', 'ja-JP-mac', 'sv-SE', and 'zh-TW'

No idea if all Firefox builds are available in all the same localizations,
so you may need to verify that any particular combination is offered.

Adapted from FirefoxAutoconfig.pkg.recipe by Greg Neagle


- **Identifier**: `com.github.mosen.pkg.FirefoxESRPolicies`

- **Parent Recipes**: `com.github.autopkg.download.firefox-rc-en_US`


## Warnings

- These recipes have duplicate NAMEs:
    - [rtrouton-recipes/Firefox/Firefox.pkg.recipe](/autopkg-dupe-tracker/rtrouton-recipes/Firefox/Firefox.pkg.recipe)
    - [gregneagle-recipes/Mozilla/FirefoxAutoconfig.pkg.recipe](/autopkg-dupe-tracker/gregneagle-recipes/Mozilla/FirefoxAutoconfig.pkg.recipe)
    - [mosen-recipes/Mozilla/FirefoxESRPolicies.pkg.recipe](/autopkg-dupe-tracker/mosen-recipes/Mozilla/FirefoxESRPolicies.pkg.recipe)
    - [neilmartin83-recipes/Mozilla/FirefoxPolicies.pkg.recipe](/autopkg-dupe-tracker/neilmartin83-recipes/Mozilla/FirefoxPolicies.pkg.recipe)
    - [recipes/Mozilla/Firefox.pkg.recipe](/autopkg-dupe-tracker/recipes/Mozilla/Firefox.pkg.recipe)
    - [recipes/Mozilla/FirefoxSignedPkg.pkg.recipe](/autopkg-dupe-tracker/recipes/Mozilla/FirefoxSignedPkg.pkg.recipe)