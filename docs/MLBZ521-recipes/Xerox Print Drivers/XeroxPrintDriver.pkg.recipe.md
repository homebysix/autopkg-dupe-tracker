# XeroxPrintDriver.pkg.recipe

            _Last updated 2021-12-23 20:01:49Z_

            - **Description**: Downloads and packages the latest Xerox package based on the override-able parameters:  model, download type, and OS Version.

model example:  'Workcentre 6515'
download types:  The download type desired; the provided string is searched in the web page.  Some examples are:
    - "macOS Print and Scan Driver Installer" (default)
    - "ICA Scan USB Driver"
    - "IMAC CA Scan USB Driver"
    - "TWAIN Scan Driver"
OS version:  
    - x11 (default)
    - 10_15
    - 10_14
    - 10_13
    - (older OS Versions should be supported, however the format changes; contact me for details if this is needed)


Tested both "macOS Print and Scan Driver Installer" and "ICA Scan USB Driver" to download and package successfully.


            - **Identifier**: `com.github.mlbz521.pkg.XeroxPrintDriver`

            - **Parent Recipes**: `com.github.mlbz521.download.XeroxPrintDriver`
