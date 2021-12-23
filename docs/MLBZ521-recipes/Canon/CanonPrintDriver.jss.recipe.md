# CanonPrintDriver.jss.recipe

            _Last updated 2021-12-23 19:58:06Z_

            - **Description**: Downloads the latest Canon "Recommended Driver" package based on the override-able parameters:  model and OS Version.

model example:  'imageRUNNER ADVANCE C7565i III'
OS version options:  
	- macOS Big Sur v11.0:  MACOS_11_0 (default)
	- macOS Catalina v10.15:  MACOS_10_15
	- macOS Mojave v10.14:  MACOS_10_14
	- macOS High Sierra v10.13:  MACOS_10_13
	- (older OS Versions, including Windows and Linux should be supported by the processor as well, see my Shared Processors README)

The download recipe requires the Selenium Library (https://www.selenium.dev/documentation/) and a browser driver to be supplied.  See the CanonPrintDriverProcessor section (https://github.com/autopkg/MLBZ521-recipes/blob/master/Shared%20Processors/ReadMe.md#canonprintdriverprocessor) in my Shared Processors README for more info.


            - **Identifier**: `com.github.mlbz521.jss.CanonPrintDriver`

            - **Parent Recipes**: `com.github.mlbz521.pkg.CanonPrintDriver`