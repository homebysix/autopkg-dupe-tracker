# EclipseTemurin8.pkg.recipe.yaml

            _Last updated 2021-12-23 20:01:51Z_

            - **Description**: Downloads the current release version of AdoptOpenJDK 8 and builds a package. This is based from the tar version rather than the signed pkg version, so that the true version number can be obtained.

FEATURE_VERSION may be any valid whole number, e.g. 8, 11, 16, 17. See https://api.adoptium.net/v3/info/available_releases for available feature versions.

RELEASE_TYPE can be 'ga' (general availablility) or 'ea' (early access).

OS may be 'mac' or others.

ARCH may be 'x64' (or 'arm' for some builds).

IMAGE_TYPE may be 'jdk', 'jre', 'testimage', 'debugimage' or 'staticlibs'.

JVM_IMPLEMENTATION may be "hotspot", "openj9" or "dragonwell".

HEAP_SIZE may be 'normal' or 'large'.

VENDOR may be 'adoptopenjdk', 'openjdk', 'adoptium', 'alibaba', 'ibm'.

Note that not all options are available for all vendors, and not all listed vendors may be currently available.


            - **Identifier**: `com.github.grahampugh.recipes.pkg.EclipseTemurin-8`

            - **Parent Recipes**: `com.github.grahampugh.recipes.download.EclipseTemurin-8`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [grahampugh-recipes/EclipseTemurin/EclipseTemurin11.pkg.recipe.yaml](/autopkg-dupe-tracker/grahampugh-recipes/EclipseTemurin/EclipseTemurin11.pkg.recipe.yaml)
    - [grahampugh-recipes/EclipseTemurin/EclipseTemurin8.pkg.recipe.yaml](/autopkg-dupe-tracker/grahampugh-recipes/EclipseTemurin/EclipseTemurin8.pkg.recipe.yaml)

- These recipes have duplicate NAMEs:
    - [grahampugh-recipes/EclipseTemurin/EclipseTemurin8-signed-installer.pkg.recipe.yaml](/autopkg-dupe-tracker/grahampugh-recipes/EclipseTemurin/EclipseTemurin8-signed-installer.pkg.recipe.yaml)
    - [grahampugh-recipes/EclipseTemurin/EclipseTemurin8.pkg.recipe.yaml](/autopkg-dupe-tracker/grahampugh-recipes/EclipseTemurin/EclipseTemurin8.pkg.recipe.yaml)