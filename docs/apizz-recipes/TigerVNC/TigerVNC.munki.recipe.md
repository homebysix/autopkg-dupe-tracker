# TigerVNC.munki.recipe

_Last updated 2021-12-23 20:01:50Z_

- **Description**: Downloads the latest version of TigerVNC and imports it into a munki_repo. Since TigerVNC is distributed with the version number in the app name, this recipe makes sure the app is copied in the form of %DESTINATION_PATH%/%NAME%.app, thereby stripping out the version, in order to maintain a single TigerVNC app in the desired location.

- **Identifier**: `com.github.apizz.munki.TigerVNC`

- **Parent Recipes**: `com.github.apizz.download.TigerVNC`
