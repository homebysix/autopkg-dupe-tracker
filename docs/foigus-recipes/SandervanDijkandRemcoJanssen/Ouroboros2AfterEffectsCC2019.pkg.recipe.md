# Ouroboros2AfterEffectsCC2019.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: "Downloads" Ouroboros 2 and packages it for installation under After Effects CC 2019.

NOTE:
- This recipe cannot determine the version of Ouroboros 2 and must have it fed in as Input, whether via override or via CLI with -k
- This recipe does not download the Ouroboros 2 zip archive--feed the zip archive into the recipe via -p

The sum of the two notes above would lead to an example run of this recipe as follows:

autopkg run Ouroboros2AfterEffectsCC2019.pkg -p /path/to/ouroboros_2.0.3.zip -k VERSION=2.0.3

            - **Identifier**: `com.github.foigus.pkg.Ouroboros2AfterEffectsCC2019`

            - **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/SandervanDijkandRemcoJanssen/Ouroboros2AfterEffectsCC2019.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/SandervanDijkandRemcoJanssen/Ouroboros2AfterEffectsCC2019.pkg.recipe)
    - [foigus-recipes/SandervanDijkandRemcoJanssen/Ouroboros2AfterEffectsCC2020.pkg.recipe](/autopkg-dupe-tracker/foigus-recipes/SandervanDijkandRemcoJanssen/Ouroboros2AfterEffectsCC2020.pkg.recipe)