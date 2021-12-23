# MSWord2016.filewave.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest Word 2016 multilingual update pkg,
and appends the version to the end of the filename.

LOCALE_ID sets the locale for a descriptive text that will be
extracted from the Microsoft update metadata. See
https://msdn.microsoft.com/en-us/goglobal/bb964664.aspx
for more information about locale IDs.

VERSION supports two values: 'latest', and 'latest-delta', defaulting to
'latest'. If 'latest-delta' is selected, the delta update will be selected
instead of the full update. An additional output variable will be made
available: 'minimum_version_for_delta', which is the minimum required
version of the application required for the delta update, which can be
used by other processors in a child recipe.


            - **Identifier**: `com.github.peshay.filewave.MSWord2016`

            - **Parent Recipes**: `com.github.autopkg.download.MSWord2016`

## Warnings

- These recipes have duplicate NAMEs:
    - [peshay-recipes/Microsoft/Office2016Word.filewave.recipe](/autopkg-dupe-tracker/peshay-recipes/Microsoft/Office2016Word.filewave.recipe)
    - [peshay-recipes/Microsoft/MSWord2016.filewave.recipe](/autopkg-dupe-tracker/peshay-recipes/Microsoft/MSWord2016.filewave.recipe)