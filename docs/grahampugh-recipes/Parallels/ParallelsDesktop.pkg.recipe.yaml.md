# ParallelsDesktop.pkg.recipe.yaml

            _Last updated 2021-12-23 20:01:51Z_

            - **Description**: Creates a package for Parallels Desktop.
This is done with the help of the pd-autodeploy file obtained from Parallels website.
There is no download recipe since Parallels Desktop is not publicly available.
Requires running as: autopkg run --pkg /path/to/downloaded-parallels.dmg "ParallelsDesktop.pkg"
You must override the LICENSE_KEY.
It is also possible to override the software update settings. See ParallelsDesktopPackager.py for details.


            - **Identifier**: `com.github.grahampugh.recipes.pkg.ParallelsDesktop`

            - **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate NAMEs:
    - [homebysix-recipes/Parallels/ParallelsDesktop.pkg.recipe](/autopkg-dupe-tracker/homebysix-recipes/Parallels/ParallelsDesktop.pkg.recipe)
    - [grahampugh-recipes/Parallels/ParallelsDesktop.pkg.recipe.yaml](/autopkg-dupe-tracker/grahampugh-recipes/Parallels/ParallelsDesktop.pkg.recipe.yaml)