# ParallelsDesktop.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of Parallels Desktop and imports it into Munki. This recipe has been tested with major versions 9 through 16.

For major versions 9 through 15, leave the PLATFORM_ARCH blank in your override.

For major version 16, set the PLATFORM_ARCH in your override to either "intel" or "m1" depending on your desired architecture. Create multiple overrides if you wish to offer both flavors via Munki.

For major version 17, set the PLATFORM_ARCH in your override to "image"

This recipe differs from the one in keeleysam-recipes because it offers code signature verification, does not require a ParallelsURLProvider processor, and also includes pkg and install recipes.

            - **Identifier**: `com.github.homebysix.munki.ParallelsDesktop`

            - **Parent Recipes**: `com.github.homebysix.pkg.ParallelsDesktop`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [keeleysam-recipes/ParallelsDesktop/ParallelsDesktop6.munki.recipe](/autopkg-dupe-tracker/keeleysam-recipes/ParallelsDesktop/ParallelsDesktop6.munki.recipe)
    - [keeleysam-recipes/ParallelsDesktop/ParallelsDesktop7.munki.recipe](/autopkg-dupe-tracker/keeleysam-recipes/ParallelsDesktop/ParallelsDesktop7.munki.recipe)
    - [keeleysam-recipes/ParallelsDesktop/ParallelsDesktop9.munki.recipe](/autopkg-dupe-tracker/keeleysam-recipes/ParallelsDesktop/ParallelsDesktop9.munki.recipe)
    - [keeleysam-recipes/ParallelsDesktop/ParallelsDesktop10.munki.recipe](/autopkg-dupe-tracker/keeleysam-recipes/ParallelsDesktop/ParallelsDesktop10.munki.recipe)
    - [keeleysam-recipes/ParallelsDesktop/ParallelsDesktop8.munki.recipe](/autopkg-dupe-tracker/keeleysam-recipes/ParallelsDesktop/ParallelsDesktop8.munki.recipe)
    - [homebysix-recipes/Parallels/ParallelsDesktop.munki.recipe](/autopkg-dupe-tracker/homebysix-recipes/Parallels/ParallelsDesktop.munki.recipe)