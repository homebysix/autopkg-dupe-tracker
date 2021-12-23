# Etcher-CLI.install.recipe

_Last updated 2021-12-23 20:01:50Z_

- **Description**: Downloads and installs the latest version of the balena-etcher-cli from GitHub. This is an experimental tool. Balena.io advise installing to /opt/etcher-cli as per https://www.balena.io/etcher/cli. AutoPkg cannot create a non-existent directory in this location, so this recipe uses /usr/local/bin as the install location. You may modify this if required.

- **Identifier**: `com.github.andrewvalentine.install.Etcher-CLI`

- **Parent Recipes**: `com.github.andrewvalentine.download.Etcher-CLI`
