# MSPowerPoint2019.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest PowerPoint 2019 multilingual update pkg,
and appends the version to the end of the filename.

CHANNEL can be set to several values in order to get more frequent updates
that can be used for testing purposes. See the explanations in the 'Channel'
table at http://macadmins.software/docs/MAU_ManifestServer.pdf. Supported
values are 'Production', 'InsiderSlow', 'InsiderFast', or a custom UUID to be
inserted into the Base URL.

LOCALE_ID sets the locale for a descriptive text that will be
extracted from the Microsoft update metadata. See
https://msdn.microsoft.com/en-us/goglobal/bb964664.aspx
for more information about locale IDs.

VERSION supports three values: 'latest', which will download
the latest full update for the given CHANNEL, 'latest-delta',
which will download the latest delta update for the given CHANNEL,
and 'latest-standalone' which will download the latest standalone
installer for the given CHANNEL. 'latest-standalone' does not support
'InsiderFast' CHANNEL.


            - **Identifier**: `com.github.autopkg.download.MSPowerPoint2019`

            - **Parent Recipes**: `com.github.autopkg.download.MSOfficeMacProduct`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [recipes/MSOfficeUpdates/MSPowerPoint2019.download.recipe](/autopkg-dupe-tracker/recipes/MSOfficeUpdates/MSPowerPoint2019.download.recipe)
    - [recipes/MSOfficeUpdates/MSPowerPoint2016.download.recipe](/autopkg-dupe-tracker/recipes/MSOfficeUpdates/MSPowerPoint2016.download.recipe)