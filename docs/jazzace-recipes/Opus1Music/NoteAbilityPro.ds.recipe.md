# NoteAbilityPro.ds.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads latest version of NoteAbilityPro 3, extracts the package, and then copies it to a local path of your choosing.
If there is no new installer, the file will not be copied (processing will be stopped by the parent recipe).
Input keys:
- DS_PKGS_PATH is the destination path for the copy. A trailing slash is not required/desired.
  The path does not need to be on the same volume as the cache, as the pkg is being duplicated.
- DS_NAME is what the final package will be called, regardless of what was extracted by the parent recipe.
  It defaults to %NAME% (just the app name).


            - **Identifier**: `com.github.jazzace.ds.NoteAbilityPro`

            - **Parent Recipes**: `com.github.jazzace.pkg.NoteAbilityPro`
