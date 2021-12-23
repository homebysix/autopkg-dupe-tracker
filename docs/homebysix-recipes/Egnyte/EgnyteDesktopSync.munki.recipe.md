# EgnyteDesktopSync.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of Egnyte Desktop Sync and imports it into Munki.

This recipe generally follows the guidelines outlined on this KB article:
    https://helpdesk.egnyte.com/hc/en-us/articles/202982694
With one exception: A postinstall script automatically launches the Sync app after installation.

The following input variables should be customized to your organization using a recipe override:
- LOCAL_ROOT
- DOMAIN
- REMOTE_FOLDERS
- SYNC_TYPE
- SYNC_ALL_LOCAL_FOLDERS
- SYNC_SPECIAL_CHAR_FILENAME

NOTE: According to Egnyte, Desktop Sync will no longer be supported after December 31st, 2019. This recipe will be deprecated at some point in the future.


            - **Identifier**: `com.github.homebysix.munki.EgnyteDesktopSync`

            - **Parent Recipes**: `com.github.homebysix.download.EgnyteDesktopSync`


## Warnings

- These recipes have duplicate NAMEs:
    - [dataJAR-recipes/Egnyte Desktop Sync NoPrefs/Egnyte Desktop Sync NoPrefs.munki.recipe](/autopkg-dupe-tracker/dataJAR-recipes/Egnyte Desktop Sync NoPrefs/Egnyte Desktop Sync NoPrefs.munki.recipe)
    - [homebysix-recipes/Egnyte/EgnyteDesktopSync.munki.recipe](/autopkg-dupe-tracker/homebysix-recipes/Egnyte/EgnyteDesktopSync.munki.recipe)