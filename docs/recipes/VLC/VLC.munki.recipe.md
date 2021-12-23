# VLC.munki.recipe

    _Last updated 2021-12-23 19:58:07Z_

    - **Description**: Downloads latest VLC disk image and imports into Munki.
This recipe defaults supported_architectures to x86_64. 
If you override SPARKLE_FEED_URL to 
"https://update.videolan.org/vlc/sparkle/vlc-intel64.xml", be sure to
adjust ARCH to "arm64".

    - **Identifier**: `com.github.autopkg.munki.VLC`

    - **Parent Recipes**: `com.github.autopkg.download.VLC`

## Warnings

- These recipes have duplicate NAMEs:
    - [dcoobs-recipes/VLC-Intel-asap/VLC-Intel-asap.munki.recipe](/autopkg-dupe-tracker/dcoobs-recipes/VLC-Intel-asap/VLC-Intel-asap.munki.recipe)
    - [dcoobs-recipes/VLC-Arm-asap/VLC-Arm-asap.munki.recipe](/autopkg-dupe-tracker/dcoobs-recipes/VLC-Arm-asap/VLC-Arm-asap.munki.recipe)
    - [apizz-recipes/VLC/VLCUniversal.munki.recipe](/autopkg-dupe-tracker/apizz-recipes/VLC/VLCUniversal.munki.recipe)
    - [recipes/VLC/VLC.munki.recipe](/autopkg-dupe-tracker/recipes/VLC/VLC.munki.recipe)
    - [aysiu-recipes/VLC-asap/VLC-asap.munki.recipe](/autopkg-dupe-tracker/aysiu-recipes/VLC-asap/VLC-asap.munki.recipe)
    - [jpiel-recipes/VLC-asap/VLC-Intel-asap.munki.recipe](/autopkg-dupe-tracker/jpiel-recipes/VLC-asap/VLC-Intel-asap.munki.recipe)
    - [jpiel-recipes/VLC-asap/VLC-Arm-asap.munki.recipe](/autopkg-dupe-tracker/jpiel-recipes/VLC-asap/VLC-Arm-asap.munki.recipe)