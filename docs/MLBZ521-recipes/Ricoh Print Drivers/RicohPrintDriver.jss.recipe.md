# RicohPrintDriver.jss.recipe

            _Last updated 2021-12-23 20:01:49Z_

            - **Description**: Downloads the latest Ricoh Driver package based on the override-able parameters:  model and OS Version.

model example:  'Aficio SP C830DN'
OS version options:  
	- Big Sur
	- Catalina
	- Mojave
	- High Sierra
	- Sierra
	- (Windows and Linux could be supported by the processor with some tweaks, see my Shared Processors README)

The download recipe requires the Selenium Library (https://www.selenium.dev/documentation/) and a browser driver to be supplied.  See the RicohPrintDriverProcessor section (https://github.com/autopkg/MLBZ521-recipes/blob/master/Shared%20Processors/ReadMe.md#RicohPrintDriverProcessor) in my Shared Processors README for more info.


            - **Identifier**: `com.github.mlbz521.jss.RicohPrintDriver`

            - **Parent Recipes**: `com.github.mlbz521.pkg.RicohPrintDriver`
