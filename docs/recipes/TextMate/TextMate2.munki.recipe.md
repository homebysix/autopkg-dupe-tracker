# TextMate2.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest TextMate 2 from their GitHub repo and imports into Munki.

The postinstall script symlinks the 'mate' command-line helper tool from
the application bundle to /usr/local/bin/mate, the same path that TextMate2
would install it to.

Set PRERELEASE to a non-empty string to download prereleases, either
via Input in an override or via the -k option,
i.e.: `-k PRERELEASE=yes`


            - **Identifier**: `com.github.autopkg.munki.TextMate2`

            - **Parent Recipes**: `com.github.autopkg.download.TextMate2`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [recipes/TextMate/TextMate.munki.recipe](/autopkg-dupe-tracker/recipes/TextMate/TextMate.munki.recipe)
    - [recipes/TextMate/TextMate2.munki.recipe](/autopkg-dupe-tracker/recipes/TextMate/TextMate2.munki.recipe)