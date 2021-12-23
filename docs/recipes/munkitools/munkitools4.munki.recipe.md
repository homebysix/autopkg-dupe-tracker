# munkitools4.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Note: munkitools does not include a code signature. If your
organization requires code signature, it is recommend to internally sign
the application.

Downloads and imports version 4 of the Munki tools via
the official releases listing on GitHub. You can set INCLUDE_PRERELEASES
to any value to have this recipe pull prerelease versions.

Note that Munki 4 includes an additional component pkg, munkitools_app_usage.
This recipe imports this to the Munki with the appropriate 'requires' key,
however as it is considered an optional component, this recipe does not
add it as an update_for any Munki component. Admins should add
munkitools_app_usage to a manifest manually if its installation on clients
is desired.

Note that Munki 4 offers the option to include Python to be embedded 
in preparation for macOS no longer including the Python environment in future OSes.
This recipe includes the embedded Python installation and adds the Python package
as a requirement to the other munki pkginfos.

This recipe cannot be overridden to pull a download from an alternate location.

The GitHubReleasesInfoProvider processor used by this recipe also
respects an input variable: 'sort_by_highest_tag_names', which
if set, will ignore the post dates of the releases and instead sort
descending by tag names according to LooseVersion semantics.

MUNKI_ICON should be overridden with your icon name.


            - **Identifier**: `com.github.autopkg.munki.munkitools4`

            - **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [recipes/munkitools/munkitools.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools.munki.recipe)
    - [recipes/munkitools/munkitools3.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools3.munki.recipe)
    - [recipes/munkitools/munkitools4.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools4.munki.recipe)
    - [recipes/munkitools/munkitools5.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools5.munki.recipe)
    - [recipes/munkitools/munkitools2.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools2.munki.recipe)