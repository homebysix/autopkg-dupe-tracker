# FrameioPanel.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Repackage the Frame.io Panel and import it into Munki.

NOTE:

- This recipe does not download the Frame.io package--feed the package into the recipe via the following format:
autopkg run FrameioPanel.munki -p /path/to/FrameioPanel_280.zxp

            - **Identifier**: `com.github.foigus.munki.FrameioPanel`

            - **Parent Recipes**: `com.github.foigus.pkg.FrameioPanel`
