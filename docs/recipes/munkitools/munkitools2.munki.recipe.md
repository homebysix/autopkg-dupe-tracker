# munkitools2.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Note: munkitools does not include a code signature. If your
organization requires code signature, it is recommend to internally sign
the application.

Downloads and imports version 2 of the Munki tools via
the official releases listing on GitHub.

By default only "final" releases are included. Set INCLUDE_PRERELEASES
to a non-empty value to include releases on GitHub marked as
"prereleases."

This recipe cannot be overridden to pull a download from an
alternate location such as munkibuilds.org - it will only download the
official releases. For this, use the munkitools2-autobuild.munki
recipe. Assuming you are overriding this recipe, you can copy your
existing override for use with the autobuild recipe.

The GitHubReleasesInfoProvider processor used by this recipe also
respects an input variable: 'sort_by_highest_tag_names', which
if set, will ignore the post dates of the releases and instead sort
descending by tag names according to LooseVersion semantics.

MUNKI_ICON should be overridden with your icon name.


            - **Identifier**: `com.github.autopkg.munki.munkitools2`

            - **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [recipes/munkitools/munkitools.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools.munki.recipe)
    - [recipes/munkitools/munkitools3.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools3.munki.recipe)
    - [recipes/munkitools/munkitools4.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools4.munki.recipe)
    - [recipes/munkitools/munkitools5.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools5.munki.recipe)
    - [recipes/munkitools/munkitools2.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools2.munki.recipe)

- These recipes have duplicate NAMEs:
    - [recipes/munkitools/munkitools2.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools2.munki.recipe)
    - [recipes/munkitools/munkitools2-autobuild.munki.recipe](/autopkg-dupe-tracker/recipes/munkitools/munkitools2-autobuild.munki.recipe)