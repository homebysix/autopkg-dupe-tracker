# FirefoxPrefs.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads Firefox disk image and builds a package. This also adds the configuration files necessary for the USC Labs
Values for FIREFOX_BUILD correspond to directories here: http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/
Some useful values are: 'latest', 'latest-10.0esr', 'latest-esr', 'latest-3.6', 'latest-beta'
LOCALE corresponds to directories at http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/$FIREFOX_BUILD/mac/
Examples include 'en-US', 'de', 'ja-JP-mac', 'sv-SE', and 'zh-TW'
No idea if all Firefox builds are available in all the same localizations, so you may need to verify that any particular
combination is offered.

            - **Identifier**: `com.github.scriptingosx.pkg.Firefox`

            - **Parent Recipes**: `com.github.autopkg.download.firefox-rc-en_US`