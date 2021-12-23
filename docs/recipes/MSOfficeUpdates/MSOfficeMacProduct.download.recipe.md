# MSOfficeMacProduct.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads a Microsoft Office Mac product. This recipe should only
ever be used as a child recipe with specific values overridden.

PRODUCT is one of the keys defined in PROD_DICT in the
MSOfficeMacURLandUpdateInfoProvider processor. Common values are:
Excel2016, Excel2019, Word2016, Word2019, etc

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


            - **Identifier**: `com.github.autopkg.download.MSOfficeMacProduct`

            - **Parent Recipes**: `None`