# FirefoxSignedPkg.install.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: This recipe downloads the signed installer package that Mozilla made available starting in Firefox 69.0, and installs it locally onto the computer running AutoPkg.

The RELEASE key used in the standard Firefox recipes are not yet supported.
LOCALE controls the language localization to be downloaded.
Examples include 'en-US', 'de', 'sv-SE', and 'zh-TW'
See the following URL for possible LOCALE values:
    http://ftp.mozilla.org/pub/firefox/releases/latest/README.txt


            - **Identifier**: `com.github.autopkg.install.FirefoxSignedPkg`

            - **Parent Recipes**: `com.github.autopkg.download.FirefoxSignedPkg`