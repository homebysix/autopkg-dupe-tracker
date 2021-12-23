# DSSPlayer.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest DSS Player package and modifies a postinstall to handle creating a LaunchD job file, changing permissions on a folder to allow non-admin serialization, and moving a PrivilegedHelperTool into position.

NOTES:
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add this repo via:

autopkg repo-add hjuutilainen-recipes

- This software may need .wma-capable playback libraries such as Telestream Flip4Mac or Telestream Switch.

            - **Identifier**: `com.github.foigus.pkg.DSSPlayer`

            - **Parent Recipes**: `com.github.foigus.download.DSSPlayer`