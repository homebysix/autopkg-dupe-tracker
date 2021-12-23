# RiftAfterEffectsCC2020.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: "Downloads" Rift and packages it for installation under After Effects CC 2020.

NOTE:
- This recipe cannot determine the version of Rift and must have it fed in as Input, whether via override or via CLI with -k
- This recipe does not download the Rift zip archive--feed the zip archive into the recipe via -p

The sum of the two notes above would lead to an example run of this recipe as follows:

autopkg run RiftAfterEffectsCC2020.pkg -p /path/to/rift_v1.4.2.zip -k VERSION=1.4.2

            - **Identifier**: `com.github.foigus.pkg.RiftAfterEffectsCC2020`

            - **Parent Recipes**: `None`
