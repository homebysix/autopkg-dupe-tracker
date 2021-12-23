# QGIS.jss.recipe

            _Last updated 2021-12-23 20:01:49Z_

            - **Description**: Downloads the latest version of QGIS, creates a package, and uploads it to the JSS.

Supports either the latest release or Long Term (support) Release.  Override the key "RELEASE_TYPE" to specify which you need:
Latest Release = "pr"
Long Term (support) Release = "ltr"

Notes:  
- Pyhton 3.6+ is a prerequisite before installing QGIS 3 -- the created .pkg will hard fail if Python 3.6+ is not installed.
- The created .pkg will "uninstall" previous versions of QGIS.

            - **Identifier**: `com.github.mlbz521.jss.QGIS`

            - **Parent Recipes**: `com.github.mlbz521.pkg.QGIS`
