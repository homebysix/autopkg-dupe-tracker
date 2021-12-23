# ProVideoFormats.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest update of the Pro Video Formats provided by Apple for their pro apps.

*** WARNING: If you are not running macOS Mojave 10.14.5 or later, you should manually download
    Pro Video Formats 2.0.7, the terminal version for OS X 10.11:
    https://support.apple.com/kb/DL1947
    You can use the -p or --pkg option when running your child recipe to process the installer if desired
    (e.g., to load version 2.0.7 into your management system). ***

*** Note 1: This Recipe requires an external processor. You must have Nate Felton's recipe repo
    available in your cache: com.github.autopkg.n8felton-recipes ***
*** Note 2: The downloaded installer is an updater that requires that you have one of the following installed:
    * Final Cut Pro X
    * Compressor 4.1
    * Motion 4.0 or later
    Having that software installed means you also agreed to the appropriate Software License Agreement(s).
    Version 2.1 and later requires macOS 10.14.3 or later. ***    


            - **Identifier**: `com.github.jazzace.download.ProVideoFormats`

            - **Parent Recipes**: `None`