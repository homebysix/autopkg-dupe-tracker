# Firefox.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads Firefox disk image and imports into Munki.
Some useful values for RELEASE are: 'latest', 'esr-latest', 'beta-latest'.
LOCALE controls the language localization to be downloaded.
Examples include 'en-US', 'de', 'sv-SE', and 'zh-TW'
See the following URLs for more info:
    http://ftp.mozilla.org/pub/firefox/releases/latest/README.txt
    http://ftp.mozilla.org/pub/firefox/releases/latest-esr/README.txt
    http://ftp.mozilla.org/pub/firefox/releases/latest-beta/README.txt

            - **Identifier**: `com.github.autopkg.munki.firefox-rc-en_US`

            - **Parent Recipes**: `com.github.autopkg.download.firefox-rc-en_US`

## Warnings

- These recipes have duplicate NAMEs:
    - [gregneagle-recipes/Mozilla/FirefoxAutoconfig.munki.recipe](/autopkg-dupe-tracker/gregneagle-recipes/Mozilla/FirefoxAutoconfig.munki.recipe)
    - [mosen-recipes/Mozilla/FirefoxESRPolicies.munki.recipe](/autopkg-dupe-tracker/mosen-recipes/Mozilla/FirefoxESRPolicies.munki.recipe)
    - [wardsparadox-recipes/Mozilla/FirefoxPolicies.munki.recipe](/autopkg-dupe-tracker/wardsparadox-recipes/Mozilla/FirefoxPolicies.munki.recipe)
    - [recipes/Mozilla/Firefox.munki.recipe](/autopkg-dupe-tracker/recipes/Mozilla/Firefox.munki.recipe)
    - [recipes/Mozilla/FirefoxSignedPkg.munki.recipe](/autopkg-dupe-tracker/recipes/Mozilla/FirefoxSignedPkg.munki.recipe)