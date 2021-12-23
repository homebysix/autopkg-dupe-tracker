# Thunderbird.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads Thunderbird disk image and imports into Munki.
Some useful values for RELEASE are: 'latest', 'beta-latest'.
LOCALE controls the language localization to be downloaded.
Examples include 'en-US', 'de', 'sv-SE', and 'zh-TW'
See the following URLs for more info:
    http://ftp.mozilla.org/pub/thunderbird/releases/latest/README.txt
    http://ftp.mozilla.org/pub/thunderbird/releases/latest-beta/README.txt

            - **Identifier**: `com.github.autopkg.munki.thunderbird`

            - **Parent Recipes**: `com.github.autopkg.download.thunderbird`