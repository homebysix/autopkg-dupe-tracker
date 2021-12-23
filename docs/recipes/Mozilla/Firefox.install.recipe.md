# Firefox.install.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads Firefox disk image, builds a package and installs it.
Some useful values for RELEASE are: 'latest', 'esr-latest', 'beta-latest'.
LOCALE controls the language localization to be downloaded.
Examples include 'en-US', 'de', 'sv-SE', and 'zh-TW'
See the following URLs for more info:
    http://ftp.mozilla.org/pub/firefox/releases/latest/README.txt
    http://ftp.mozilla.org/pub/firefox/releases/latest-esr/README.txt
    http://ftp.mozilla.org/pub/firefox/releases/latest-beta/README.txt

            - **Identifier**: `com.github.autopkg.install.Firefox`

            - **Parent Recipes**: `com.github.autopkg.download.firefox-rc-en_US`

## Warnings

- These recipes have duplicate filenames:
    - [rtrouton-recipes/Firefox/Firefox.install.recipe](/autopkg-dupe-tracker/rtrouton-recipes/Firefox/Firefox.install.recipe)
    - [recipes/Mozilla/Firefox.install.recipe](/autopkg-dupe-tracker/recipes/Mozilla/Firefox.install.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [rtrouton-recipes/Firefox/Firefox.install.recipe](/autopkg-dupe-tracker/rtrouton-recipes/Firefox/Firefox.install.recipe)
    - [recipes/Mozilla/Firefox.install.recipe](/autopkg-dupe-tracker/recipes/Mozilla/Firefox.install.recipe)