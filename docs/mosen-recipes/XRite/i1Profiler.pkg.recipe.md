# i1Profiler.pkg.recipe

        _Last updated 2021-12-23 19:58:07Z_

        - **Description**: 
Build an unattended version of X-Rite i1Profiler.

Remove interactive scripts and applications (usually AppleScripts) to allow for unattended installation.

Normally the i1Profiler mpkg runs loginitem.app to get i1ProfilerTray.app into Login Items. 
It also launches the tray application during the install. These have been removed as they fail in a non-interactive
installation.

OVERRIDES

    NAME - The name used to find the downloaded package that was unpacked from a zip file. This should normally not change.

    PKG_NAME - The name of the package that will be created by this recipe. Defaults to `i1Profiler Silent.pkg`. You may have to override
    this in i1Profiler.munki because FlatPkgPacker does not have output variables.


        - **Identifier**: `com.github.mosen.pkg.i1Profiler`

        - **Parent Recipes**: `com.github.mosen.download.i1Profiler`

## Warnings

- These recipes have duplicate filenames:
    - [mosen-recipes/XRite/i1Profiler.pkg.recipe](/autopkg-dupe-tracker/mosen-recipes/XRite/i1Profiler.pkg.recipe)
    - [jazzace-recipes/X-Rite/i1profiler.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/X-Rite/i1profiler.pkg.recipe)
    - [moofit-recipes/i1profiler/i1profiler.pkg.recipe](/autopkg-dupe-tracker/moofit-recipes/i1profiler/i1profiler.pkg.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [mosen-recipes/XRite/i1Profiler.pkg.recipe](/autopkg-dupe-tracker/mosen-recipes/XRite/i1Profiler.pkg.recipe)
    - [jazzace-recipes/X-Rite/i1profiler.pkg.recipe](/autopkg-dupe-tracker/jazzace-recipes/X-Rite/i1profiler.pkg.recipe)
    - [moofit-recipes/i1profiler/i1profiler.pkg.recipe](/autopkg-dupe-tracker/moofit-recipes/i1profiler/i1profiler.pkg.recipe)

- These recipes have duplicate NAMEs:
    - [mosen-recipes/XRite/i1Profiler.pkg.recipe](/autopkg-dupe-tracker/mosen-recipes/XRite/i1Profiler.pkg.recipe)
    - [moofit-recipes/i1profiler/i1profiler.pkg.recipe](/autopkg-dupe-tracker/moofit-recipes/i1profiler/i1profiler.pkg.recipe)