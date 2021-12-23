# i1Profiler.munki.recipe

        _Last updated 2021-12-23 20:01:50Z_

        - **Description**: 
Import X-Rite i1Profiler into your munki repository (Using the unattended package created by i1Profiler.pkg).

OVERRIDES

    NAME - The name of the item in your munki repository, defaults to `i1Profiler`.

    MUNKI_REPO_SUBDIR - The subdirectory of your munki repository where this package will be imported.
    defaults to `apps/XRite`.

    PKG_NAME - The filename of the flat package created by i1Profiler.pkg. Because FlatPkgPacker doesn't have outputs,
    you have to override this on both recipes if you don't want the package name to be `i1Profiler Silent.pkg`

    pkginfo - The default template pkginfo. The hasp installer does not always run (com.xrite.hasp.installer.pkg), therefore 
    by default it must be marked as optional to prevent munki from showing the item as not installed.



        - **Identifier**: `com.github.mosen.munki.i1Profiler`

        - **Parent Recipes**: `com.github.mosen.download.i1Profiler`


## Warnings

- These recipes have duplicate filenames:
    - [dataJAR-recipes/i1Profiler/i1Profiler.munki.recipe](/autopkg-dupe-tracker/dataJAR-recipes/i1Profiler/i1Profiler.munki.recipe)
    - [mosen-recipes/XRite/i1Profiler.munki.recipe](/autopkg-dupe-tracker/mosen-recipes/XRite/i1Profiler.munki.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [dataJAR-recipes/i1Profiler/i1Profiler.munki.recipe](/autopkg-dupe-tracker/dataJAR-recipes/i1Profiler/i1Profiler.munki.recipe)
    - [mosen-recipes/XRite/i1Profiler.munki.recipe](/autopkg-dupe-tracker/mosen-recipes/XRite/i1Profiler.munki.recipe)

- These recipes have duplicate NAMEs:
    - [dataJAR-recipes/i1Profiler/i1Profiler.munki.recipe](/autopkg-dupe-tracker/dataJAR-recipes/i1Profiler/i1Profiler.munki.recipe)
    - [mosen-recipes/XRite/i1Profiler.munki.recipe](/autopkg-dupe-tracker/mosen-recipes/XRite/i1Profiler.munki.recipe)