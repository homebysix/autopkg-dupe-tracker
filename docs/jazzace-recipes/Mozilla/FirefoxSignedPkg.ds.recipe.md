# FirefoxSignedPkg.ds.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: This recipe downloads the signed installer package that Mozilla made available starting in Firefox 69.0 and 68.1esr 
and then copies the package to a local path of your choosing. 
Note that this recipe breaks with .ds convention because it appends version information to the file name, 
so the DS_NAME input variable is omitted.
Input key:
- DS_PKGS_PATH is the destination path for the copy.
  A trailing slash is not required/desired. The path does not need to be on the same volume as the cache.


            - **Identifier**: `com.github.jazzace.ds.FirefoxSignedPkg`

            - **Parent Recipes**: `com.github.autopkg.download.FirefoxSignedPkg`
