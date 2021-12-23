# ParallelsDesktop.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the major version of Parallels Desktop specified by MAJOR_VERSION. This recipe has been tested with major versions 9 through 16.

For major versions 9 through 15, leave the PLATFORM_ARCH blank in your override.

For major version 16, set the PLATFORM_ARCH in your override to either "intel" or "m1" depending on your desired architecture.

For major version 17, set the PLATFORM_ARCH in your override to "image"

This recipe differs from the one in keeleysam-recipes because it offers code signature verification, does not require a ParallelsURLProvider processor, and also includes pkg and install recipes.

            - **Identifier**: `com.github.homebysix.download.ParallelsDesktop`

            - **Parent Recipes**: `None`

## Warnings

- These recipes have duplicate filenames:
    - [keeleysam-recipes/ParallelsDesktop/ParallelsDesktop.download.recipe](/autopkg-dupe-tracker/keeleysam-recipes/ParallelsDesktop/ParallelsDesktop.download.recipe)
    - [homebysix-recipes/Parallels/ParallelsDesktop.download.recipe](/autopkg-dupe-tracker/homebysix-recipes/Parallels/ParallelsDesktop.download.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [keeleysam-recipes/ParallelsDesktop/ParallelsDesktop.download.recipe](/autopkg-dupe-tracker/keeleysam-recipes/ParallelsDesktop/ParallelsDesktop.download.recipe)
    - [homebysix-recipes/Parallels/ParallelsDesktop.download.recipe](/autopkg-dupe-tracker/homebysix-recipes/Parallels/ParallelsDesktop.download.recipe)