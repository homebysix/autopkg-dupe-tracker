# SonarQubeScanner.munki.recipe

_Last updated 2021-12-23 19:58:07Z_

- **Description**: Downloads, repackages, and imports into Munki the latest version of SonarQube Scanner. Will also configure the scanner to contact a desired server via Munki postinstall script. Defaults to not setting the SonarQube server address.

- **Identifier**: `com.github.apettinen.munki.SonarQubeScanner`

- **Parent Recipes**: `com.github.apettinen.pkg.SonarQubeScanner`