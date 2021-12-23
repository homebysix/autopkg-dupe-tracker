# FirefoxPrefs.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads Firefox disk image and imports into Munki.
Values for RELEASE correspond to directories here: http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/
Some useful values are: 'latest', 'latest-10.0esr', 'latest-esr', 'latest-3.6', 'latest-beta'
LOCALE corresponds to directories at http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/$RELEASE/mac/
Examples include 'en-US', 'de', 'ja-JP-mac', 'sv-SE', and 'zh-TW'
No idea if all Firefox builds are available in all the same localizations, so you may need to verify that any particular
combination is offered.

            - **Identifier**: `com.github.scriptingosx.munki.Firefox`

            - **Parent Recipes**: `com.github.scriptingosx.pkg.Firefox`
