# TheUnarchiver.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest 'The Unarchiver' and imports into Munki.

Note: this recipe has issues with repeated runs due to a bug in curl starting
with OS X 10.10.5. This has been fixed for the next version of AutoPkg, but not
yet in a released version. It should still download and unzip properly if is it is the first run, without an already-downloaded file.

The application's LSMinimumSystemVersion is currently inaccurate, but the
sparkle:minimumSystemVersion element is correct, so we use MunkiPkginfoMerger
to merge the minimum_os_version that is output from SparkleUpdateInfoProvider
in the .download ParentRecipe.

            - **Identifier**: `com.github.autopkg.munki.TheUnarchiver`

            - **Parent Recipes**: `com.github.autopkg.download.TheUnarchiver`
