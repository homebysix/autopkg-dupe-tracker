# Anaconda3.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the current release version of Anaconda for Python 3 and imports it into Munki.

This differs from other recipes as we pull the version out of a .json file instead of the pkg receipts, as
the pkg receipts are all 0.

This is accomplished via our own custom processor (JSONFileReader) and an installcheck_script

            - **Identifier**: `com.github.dataJAR-recipes.munki.Anaconda 3`

            - **Parent Recipes**: `com.github.hansen-m.download.Anaconda3`

## Warnings

- These recipes have duplicate filenames:
    - [dataJAR-recipes/Anaconda 3/Anaconda3.munki.recipe](/autopkg-dupe-tracker/dataJAR-recipes/Anaconda 3/Anaconda3.munki.recipe)
    - [its-unibas-recipes/Continuum/Anaconda3.munki.recipe](/autopkg-dupe-tracker/its-unibas-recipes/Continuum/Anaconda3.munki.recipe)
    - [ygini-recipes/Anaconda/Anaconda3.munki.recipe](/autopkg-dupe-tracker/ygini-recipes/Anaconda/Anaconda3.munki.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [dataJAR-recipes/Anaconda 3/Anaconda3.munki.recipe](/autopkg-dupe-tracker/dataJAR-recipes/Anaconda 3/Anaconda3.munki.recipe)
    - [its-unibas-recipes/Continuum/Anaconda3.munki.recipe](/autopkg-dupe-tracker/its-unibas-recipes/Continuum/Anaconda3.munki.recipe)
    - [its-unibas-recipes/Continuum/Anaconda.munki.recipe](/autopkg-dupe-tracker/its-unibas-recipes/Continuum/Anaconda.munki.recipe)
    - [ygini-recipes/Anaconda/Anaconda3.munki.recipe](/autopkg-dupe-tracker/ygini-recipes/Anaconda/Anaconda3.munki.recipe)
    - [ygini-recipes/Anaconda/Anaconda2.munki.recipe](/autopkg-dupe-tracker/ygini-recipes/Anaconda/Anaconda2.munki.recipe)