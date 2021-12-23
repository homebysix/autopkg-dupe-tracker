# MSEdge.download.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest Microsoft Edge pkg,
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

VERSION supports one value: 'latest', which will download
the latest full update for the given CHANNEL.


            - **Identifier**: `com.github.autopkg.download.MSEdge`

            - **Parent Recipes**: `com.github.autopkg.download.MSOfficeMacProduct`
