# SassafrasK2Client.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Fetches the latest Sassafras KeyClient Mac installer and imports into
Munki. Additionally, fetch the k2clientconfig tool from the Sassafras website
for the purposes of customizing the installer.

This recipe supports KeyClient 7.0 and up only. See SassafrasK2Client.download
for details on the REVISION Input variable, which you may wish to override.

K2CLIENTCONFIG_OPTIONS is a string that should be overridden with command-line
options to the 'k2clientconfig' tool. No sanity checking is performed beyond
what's done by k2clientconfig. The recipe includes one suggested default, more
documentation here:
http://www.sassafras.com/hrl/7.2/k2clientconfigM.html

There are k2clientconfig options to kill KeyAccess before installation, and to
start it after installation, implying we might not necessarily need a logout.
Some testing shows that when these options are used, the installation is still
not in a consistent state. Requiring a restart seems the only sane choice for now,
but it should be further investigated.

We use a separate installs item for KeyAccess.app, because the options passed
to k2clientconfig may alter which packages are installed, and therefore the
receipts array.

Sassafras uses two decimals in their mpkg versions (skipping the third) but
uses three decimals everywhere else (webpage, actual bundle files, preference
pane, etc.), so we use the three-decimal version.

The 7.2.0.3 installer has a known issue with version numbers in the pkg
components, but since we generate an installs item for KeyAccess.app already,
we use its version in the pkginfo.


            - **Identifier**: `com.github.autopkg.munki.sassafras-k2client`

            - **Parent Recipes**: `com.github.autopkg.download.sassafras-k2client`

## Warnings

- These recipes have duplicate URLDownloader URLs:
    - [jazzace-recipes/Sassafras/SassafrasK2Client.ds.recipe](/autopkg-dupe-tracker/jazzace-recipes/Sassafras/SassafrasK2Client.ds.recipe)
    - [recipes/SassafrasK2Client/SassafrasK2Client.munki.recipe](/autopkg-dupe-tracker/recipes/SassafrasK2Client/SassafrasK2Client.munki.recipe)