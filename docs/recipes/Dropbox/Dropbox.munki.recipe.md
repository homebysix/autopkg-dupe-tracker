# Dropbox.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the current release version of Dropbox and imports into Munki.

Postinstall script extracts the DropboxHelperInstaller and sets the setuid
bit so that it can perform its setup tasks as root without asking for admin
privileges.

Dropbox will attempt to update periodically, and if it does not have permission to
overwrite the bundle at /Applications/Dropbox.app, it will instead download
the updated version to ~/Library/Application Support/Dropbox, and run this version
as long as it is more recent than the copy in /Applications.

This recipe uses blocking_applications to prevent the installation only if Dropbox
from /Applications is running. If an updated version from the user's home directory
is running, Munki can update the version in /Applications without requiring the user
to quit Dropbox.

            - **Identifier**: `com.github.autopkg.munki.dropbox`

            - **Parent Recipes**: `com.github.autopkg.download.dropbox`