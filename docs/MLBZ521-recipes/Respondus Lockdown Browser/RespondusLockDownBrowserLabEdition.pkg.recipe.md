# RespondusLockDownBrowserLabEdition.pkg.recipe

            _Last updated 2021-12-23 19:58:06Z_

            - **Description**: Downloads and packages the latest verison Respondus' LockDown Browser and configures the install package for the Lab Edition.

The download recipe requires you to set your Institution ID and this recipe requires your Lab Hash.

Because Repondus does silly things by expecting the licencing information in the file name, this does package inception so that the package name is a standard format.

This pkg recipe differs from nstrauss-recipes's pkg recipe by not installing the LDB on the AutoPkg runner/system and simply performing the above steps to get the desired results (tl/dr:  less steps, similar result).

            - **Identifier**: `com.github.mlbz521.pkg.RespondusLockDownBrowserLabEdition`

            - **Parent Recipes**: `com.github.nstrauss.download.RespondusLockDownBrowser`