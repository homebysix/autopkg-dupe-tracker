# FirefoxESRPolicies.munki.recipe

_Last updated 2021-12-23 19:58:07Z_

- **Description**: Downloads Firefox disk image, builds a package, injects the policies.json, then imports the pkg into
your Munki repo.

Create a `distribution` directory containing the policies.json in the same directory as the recipe.
You may optionally use a different directory name (inside RECIPE_DIR) by setting DISTRIBUTION_PATH.

You might consider setting a unique PKG_ID to differentiate your org's "flavor" of Firefox.

Values for RELEASE correspond to directories here:
http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/
Some useful values are:
'latest', 'latest-10.0esr', 'latest-esr', 'latest-3.6', 'latest-beta'
LOCALE corresponds to directories at
http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/$FIREFOX_BUILD/mac/
Examples include 'en-US', 'de', 'ja-JP-mac', 'sv-SE', and 'zh-TW'

No idea if all Firefox builds are available in all the same localizations,
so you may need to verify that any particular combination is offered.

Adapted from FirefoxAutoconfig.munki.recipe by Greg Neagle


- **Identifier**: `com.github.mosen.munki.FirefoxESRPolicies`

- **Parent Recipes**: `com.github.mosen.pkg.FirefoxESRPolicies`

## Warnings

- These recipes have duplicate NAMEs:
    - [gregneagle-recipes/Mozilla/FirefoxAutoconfig.munki.recipe](/autopkg-dupe-tracker/gregneagle-recipes/Mozilla/FirefoxAutoconfig.munki.recipe)
    - [mosen-recipes/Mozilla/FirefoxESRPolicies.munki.recipe](/autopkg-dupe-tracker/mosen-recipes/Mozilla/FirefoxESRPolicies.munki.recipe)
    - [wardsparadox-recipes/Mozilla/FirefoxPolicies.munki.recipe](/autopkg-dupe-tracker/wardsparadox-recipes/Mozilla/FirefoxPolicies.munki.recipe)
    - [recipes/Mozilla/Firefox.munki.recipe](/autopkg-dupe-tracker/recipes/Mozilla/Firefox.munki.recipe)
    - [recipes/Mozilla/FirefoxSignedPkg.munki.recipe](/autopkg-dupe-tracker/recipes/Mozilla/FirefoxSignedPkg.munki.recipe)