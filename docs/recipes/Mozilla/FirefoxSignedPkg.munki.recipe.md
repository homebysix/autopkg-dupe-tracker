# FirefoxSignedPkg.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: This recipe downloads the signed installer package that Mozilla made available starting in Firefox 69.0, and imports the pkg file into a Munki repo.

The RELEASE key used in the standard Firefox recipes are not yet supported.
LOCALE controls the language localization to be downloaded.
Examples include 'en-US', 'de', 'sv-SE', and 'zh-TW'
See the following URL for possible LOCALE values:
    http://ftp.mozilla.org/pub/firefox/releases/latest/README.txt


            - **Identifier**: `com.github.autopkg.munki.FirefoxSignedPkg`

            - **Parent Recipes**: `com.github.autopkg.download.FirefoxSignedPkg`

## Warnings

- These recipes have duplicate NAMEs:
    - [gregneagle-recipes/Mozilla/FirefoxAutoconfig.munki.recipe](/autopkg-dupe-tracker/gregneagle-recipes/Mozilla/FirefoxAutoconfig.munki.recipe)
    - [mosen-recipes/Mozilla/FirefoxESRPolicies.munki.recipe](/autopkg-dupe-tracker/mosen-recipes/Mozilla/FirefoxESRPolicies.munki.recipe)
    - [wardsparadox-recipes/Mozilla/FirefoxPolicies.munki.recipe](/autopkg-dupe-tracker/wardsparadox-recipes/Mozilla/FirefoxPolicies.munki.recipe)
    - [recipes/Mozilla/Firefox.munki.recipe](/autopkg-dupe-tracker/recipes/Mozilla/Firefox.munki.recipe)
    - [recipes/Mozilla/FirefoxSignedPkg.munki.recipe](/autopkg-dupe-tracker/recipes/Mozilla/FirefoxSignedPkg.munki.recipe)