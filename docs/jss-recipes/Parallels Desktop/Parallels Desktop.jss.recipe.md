# Parallels Desktop.jss.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the major version of Parallels Desktop specified by MAJOR_VERSION, creates a package, and imports it into your JSS. This recipe has been tested with major versions 9 through 16.

For major versions 9 through 15, leave the PLATFORM_ARCH blank in your override.

For major version 16, set the PLATFORM_ARCH in your override to either "intel" or "m1" depending on your desired architecture.

            - **Identifier**: `com.github.jss-recipes.jss.ParallelsDesktop`

            - **Parent Recipes**: `com.github.homebysix.pkg.ParallelsDesktop`