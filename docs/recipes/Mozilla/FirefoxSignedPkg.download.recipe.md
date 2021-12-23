# FirefoxSignedPkg.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: This recipe downloads the signed installer package that Mozilla made available starting in Firefox 69.0 and 68.1esr.

You may choose a specific release stream by placing the appropriate key in the 
LATEST_RELEASE input variable. The two most common are:
    LATEST_FIREFOX_VERSION for the latest (regular) release (this is the default), and
    FIREFOX_ESR for latest ESR release.
Other values to try can be found by examining the JSON file at:
    https://product-details.mozilla.org/1.0/firefox_versions.json
(Not all will work.)

LOCALE controls the language localization to be downloaded.
Examples include 'en-US', 'de', 'sv-SE', and 'zh-TW'
See the following URL for possible LOCALE values:
    http://ftp.mozilla.org/pub/firefox/releases/latest/README.txt


            - **Identifier**: `com.github.autopkg.download.FirefoxSignedPkg`

            - **Parent Recipes**: `None`

## Warnings

- These recipes have duplicate NAMEs:
    - [recipes/Mozilla/FirefoxWindows.download.recipe](/autopkg-dupe-tracker/recipes/Mozilla/FirefoxWindows.download.recipe)
    - [recipes/Mozilla/FirefoxSignedPkg.download.recipe](/autopkg-dupe-tracker/recipes/Mozilla/FirefoxSignedPkg.download.recipe)
    - [recipes/Mozilla/Firefox.download.recipe](/autopkg-dupe-tracker/recipes/Mozilla/Firefox.download.recipe)
    - [hansen-m-recipes/Mozilla/Firefox-Win.download.recipe](/autopkg-dupe-tracker/hansen-m-recipes/Mozilla/Firefox-Win.download.recipe)
    - [hansen-m-recipes/Mozilla/Firefox64-Win.download.recipe](/autopkg-dupe-tracker/hansen-m-recipes/Mozilla/Firefox64-Win.download.recipe)