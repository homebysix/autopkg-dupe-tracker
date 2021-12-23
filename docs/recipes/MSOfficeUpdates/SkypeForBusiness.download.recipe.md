# SkypeForBusiness.download.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest Skype for Business multilingual update pkg,
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

VERSION currently only supports one value: 'latest', which will download
the latest full update for the given CHANNEL.


            - **Identifier**: `com.github.autopkg.download.SkypeForBusiness`

            - **Parent Recipes**: `com.github.autopkg.download.MSOfficeMacProduct`


## Warnings

- These recipes have duplicate NAMEs:
    - [rtrouton-recipes/MicrosoftSkypeForBusiness365/MicrosoftSkypeForBusiness365.download.recipe](/autopkg-dupe-tracker/rtrouton-recipes/MicrosoftSkypeForBusiness365/MicrosoftSkypeForBusiness365.download.recipe)
    - [recipes/MSOfficeUpdates/SkypeForBusiness.download.recipe](/autopkg-dupe-tracker/recipes/MSOfficeUpdates/SkypeForBusiness.download.recipe)