# FirefoxSignedPkg.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: This recipe downloads the signed installer package that Mozilla made available starting in Firefox 69.0. Because the downloaded file is already a package, this pkg recipe does not add any further actions.

The RELEASE key used in the standard Firefox recipes are not yet supported.
LOCALE controls the language localization to be downloaded.
Examples include 'en-US', 'de', 'sv-SE', and 'zh-TW'
See the following URL for possible LOCALE values:
    http://ftp.mozilla.org/pub/firefox/releases/latest/README.txt


            - **Identifier**: `com.github.autopkg.pkg.FirefoxSignedPkg`

            - **Parent Recipes**: `com.github.autopkg.download.FirefoxSignedPkg`


## Warnings

- These recipes have duplicate NAMEs:
    - [rtrouton-recipes/Firefox/Firefox.pkg.recipe](/autopkg-dupe-tracker/rtrouton-recipes/Firefox/Firefox.pkg.recipe)
    - [gregneagle-recipes/Mozilla/FirefoxAutoconfig.pkg.recipe](/autopkg-dupe-tracker/gregneagle-recipes/Mozilla/FirefoxAutoconfig.pkg.recipe)
    - [mosen-recipes/Mozilla/FirefoxESRPolicies.pkg.recipe](/autopkg-dupe-tracker/mosen-recipes/Mozilla/FirefoxESRPolicies.pkg.recipe)
    - [neilmartin83-recipes/Mozilla/FirefoxPolicies.pkg.recipe](/autopkg-dupe-tracker/neilmartin83-recipes/Mozilla/FirefoxPolicies.pkg.recipe)
    - [recipes/Mozilla/Firefox.pkg.recipe](/autopkg-dupe-tracker/recipes/Mozilla/Firefox.pkg.recipe)
    - [recipes/Mozilla/FirefoxSignedPkg.pkg.recipe](/autopkg-dupe-tracker/recipes/Mozilla/FirefoxSignedPkg.pkg.recipe)