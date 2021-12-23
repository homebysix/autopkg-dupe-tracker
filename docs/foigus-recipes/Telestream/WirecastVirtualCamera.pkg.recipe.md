# WirecastVirtualCamera.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the current version of the Wirecast Virtual Camera driver for Wirecast and extracts the package from the dmg.

This recipe is necessary because munkiimport refuses to import the Wirecast dmg (for the purposes of obtaining the Wirecast Virtual Camera package), and "force_munkiimport" isn't a good idea if this is automated.

            - **Identifier**: `com.github.foigus.pkg.WirecastVirtualCamera`

            - **Parent Recipes**: `com.github.foigus.download.Wirecast`
