# DaVinciResolve12.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the most recent version of DaVinci Resolve 12 and imports into Munki.

Please see directions in the download recipe about additional Input variables required for this
recipe.

Resolve also includes the CUDA driver installed via a postinstall script. It may or may not
install, depending on whether a equivalent version of the CUDA driver exists already on the system.
The postinstall script calls another script located within the application bundle to perform the
actual installation. It can be found here within this recipe's CACHE_DIR (look for CUDA_VER):

pkg_payload/Library/Application Support/Blackmagic Design/DaVinci Resolve/Prereqs/install.sh

Even if the CUDA driver does install via the Resolve installer pkg, it should not require a
restart, as it reloads its kext and support daemons in postinstall scripts. You may consider
adding the CUDA driver as a separate item in Munki and adding it as a 'requires' for Resolve.

One caveat with this package, is that this installer runs a script that evalutes
the owner of /dev/console to derive a home directory, which then is configured system-wide
as a cache location for Resolve. If this installer is run while a user is logged in, then
this user's home will be used, and if run at the loginwindow, the root user's home will be.


            - **Identifier**: `com.github.timsutton.munki.davinciresolve12`

            - **Parent Recipes**: `com.github.timsutton.download.davinciresolve12`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [blackthroat-recipes/Blackmagic/DaVinciResolve15.munki.recipe](/autopkg-dupe-tracker/blackthroat-recipes/Blackmagic/DaVinciResolve15.munki.recipe)
    - [timsutton-recipes/Blackmagic/DaVinciResolve12.munki.recipe](/autopkg-dupe-tracker/timsutton-recipes/Blackmagic/DaVinciResolve12.munki.recipe)
    - [timsutton-recipes/Blackmagic/DaVinciResolve14.munki.recipe](/autopkg-dupe-tracker/timsutton-recipes/Blackmagic/DaVinciResolve14.munki.recipe)