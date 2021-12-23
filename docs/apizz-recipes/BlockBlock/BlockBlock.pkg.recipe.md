# BlockBlock.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of BlockBlock from GitHub and creates a PKG.

The native BlockBlock Installer.app utilizes a shell script to install / uninstall BlockBlock. While most of software components are simply copied from within the installer app to their respective locations, the default preferences.plist is created on the fly. To address this, this recipe creates this defaults file via the PLIST_DEFAULTS input variable. If you wish to alter the defaults for your environment, simply add / update the applicable keys and values.

            - **Identifier**: `com.github.apizz.pkg.BlockBlock`

            - **Parent Recipes**: `com.github.zentralpro.download.blockblock`
