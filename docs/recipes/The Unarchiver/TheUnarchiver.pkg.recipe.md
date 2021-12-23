# TheUnarchiver.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the current release version of 'The Unarchiver' and builds a package.

Note: this recipe has issues with repeated runs due to a bug in curl starting
with OS X 10.10.5. This has been fixed for the next version of AutoPkg, but not
yet in a released version. It should still download and unzip properly if is it is the first run, without an already-downloaded file.


            - **Identifier**: `com.github.autopkg.pkg.TheUnarchiver`

            - **Parent Recipes**: `com.github.autopkg.download.TheUnarchiver`
