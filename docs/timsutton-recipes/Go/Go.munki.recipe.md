# Go.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads and imports Go into Munki, from the official Golang
downloads page.

Note that the installer pkgs have identifiers like 'go1.3.2', 'go1.4', etc.
As long as this 'go' prefix remains, Munki will compare package versions
as expected.

            - **Identifier**: `com.github.timsutton.munki.Go`

            - **Parent Recipes**: `com.github.timsutton.download.Go`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [timsutton-recipes/Go/Go.munki.recipe](/autopkg-dupe-tracker/timsutton-recipes/Go/Go.munki.recipe)
    - [precursorca-recipes/St. Clair Software/Go64.munki.recipe](/autopkg-dupe-tracker/precursorca-recipes/St. Clair Software/Go64.munki.recipe)