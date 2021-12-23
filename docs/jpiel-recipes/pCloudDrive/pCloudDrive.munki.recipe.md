# pCloudDrive.munki.recipe

_Last updated 2021-12-23 20:01:50Z_

- **Description**: Recreate the pCloudDrive pkg to have the app version as pkg version. This package requires osxfuse package to be installed. It is safer to install it when no user is logged in, so it requires logout. If your autopkg host is connecting to internet using multiple WAN IP, the download may fail.

- **Identifier**: `com.github.jpiel.munki.pCloudDrive`

- **Parent Recipes**: `com.github.jpiel.download.pCloudDrive`
