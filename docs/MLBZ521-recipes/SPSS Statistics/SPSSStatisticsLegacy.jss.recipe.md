# SPSSStatisticsLegacy.jss.recipe

            _Last updated 2021-12-23 20:01:49Z_

            - **Description**: Downloads and packages the latest or a specified verison of SPSS Statistics from a local file share and then uploads it to a JPS.

Tested on versions of SPSS 26 and older.

The created Policy's name will be in the format of "%NAME% %MAJOR_VERSION%"

Two override variables are avilable to support the installation of SPSS:
	* INSTALL_JDK_CLI
		* A JDK is required to install SPSS silently; if one is not installed, you can provide a command 
			line command to acquire one through any method that is support in your environemnt
	* INSTALL_PROPERTIES
		* As the name suggests, this the "installer.properties" that allows you to customize the install
			of SPSS.  The available parameters are included; customize for your environment.


            - **Identifier**: `com.github.mlbz521.jss.SPSSStatisticsLegacy`

            - **Parent Recipes**: `com.github.mlbz521.pkg.SPSSStatisticsLegacy`


## Warnings

- These recipes have duplicate NAMEs:
    - [MLBZ521-recipes/SPSS Statistics/SPSSStatisticsLegacy.jss.recipe](/autopkg-dupe-tracker/MLBZ521-recipes/SPSS Statistics/SPSSStatisticsLegacy.jss.recipe)
    - [MLBZ521-recipes/SPSS Statistics/SPSSStatistics.jss.recipe](/autopkg-dupe-tracker/MLBZ521-recipes/SPSS Statistics/SPSSStatistics.jss.recipe)