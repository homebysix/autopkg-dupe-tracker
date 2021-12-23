# Fission2.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads and imports Fission 2 into Munki.

SYSTEM_VERSION is a minimum OS version expressed as a four-character
integer, i.e. (10majorminor), which is sent to the RA Sparkle feed
server. Fission 2 currently requires 10.7, but it's possible that
later revisions will require a higher OS, so this may be overridden.

The Fission app already includes the minimum OS version required
in its application bundle, so Munki will automatically set the
correct minimum_os_version pkginfo key.

            - **Identifier**: `com.github.timsutton.munki.Fission2`

            - **Parent Recipes**: `com.github.timsutton.download.Fission2`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [timsutton-recipes/RogueAmoeba/Fission2.munki.recipe](/autopkg-dupe-tracker/timsutton-recipes/RogueAmoeba/Fission2.munki.recipe)
    - [homebysix-recipes/RogueAmoeba/Fission.munki.recipe](/autopkg-dupe-tracker/homebysix-recipes/RogueAmoeba/Fission.munki.recipe)