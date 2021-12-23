# MSTeams.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest MS Teams pkg,
appends the version to the end of the filename, and imports into
Munki.

If this is an update_for something, you may define this in your
pkginfo Input override below.

CHANNEL, LOCALE_ID, and VERSION are inherited from the .download recipe but can
still be overridden in an override for this .munki recipe.

CHANNEL can be set to several values in order to get more frequent updates
that can be used for testing purposes. See the explanations in the 'Channel'
table at http://macadmins.software/docs/MAU_ManifestServer.pdf. Supported
values are 'Production', 'InsiderSlow', 'InsiderFast', or a custom UUID to be
inserted into the Base URL.

LOCALE_ID sets the locale for a descriptive text that will be
extracted from the Microsoft update metadata. See
https://msdn.microsoft.com/en-us/goglobal/bb964664.aspx
for more information about locale IDs.

VERSION supports one value: 'latest', which will download
the latest full update for the given CHANNEL.


            - **Identifier**: `com.github.autopkg.munki.MSTeams`

            - **Parent Recipes**: `com.github.autopkg.download.MSTeams`

## Warnings

- These recipes have duplicate filenames:
    - [apettinen-recipes/MSTeams/MSTeams.munki.recipe](/autopkg-dupe-tracker/apettinen-recipes/MSTeams/MSTeams.munki.recipe)
    - [recipes/MSOfficeUpdates/MSTeams.munki.recipe](/autopkg-dupe-tracker/recipes/MSOfficeUpdates/MSTeams.munki.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [apettinen-recipes/MSTeams/MSTeams.munki.recipe](/autopkg-dupe-tracker/apettinen-recipes/MSTeams/MSTeams.munki.recipe)
    - [recipes/MSOfficeUpdates/MSTeams.munki.recipe](/autopkg-dupe-tracker/recipes/MSOfficeUpdates/MSTeams.munki.recipe)