# SPSSStatistics Patch.jss.recipe

            _Last updated 2021-12-23 20:01:49Z_

            - **Description**: Downloads and packages the latest or a specified verison of a SPSS Statistics Patch from a local file share and then uploads it to a JPS.

The created Policy's name will be in the format of "SPSS Statistics %MAJOR_VERSION% Patch"

Two override variables are avilable to support the installation of SPSS:
	* INSTALL_JDK_CLI
		* A JDK is required to install SPSS silently; if one is not installed, you can provide a command 
			line command to acquire one through any method that is support in your environemnt
	* INSTALL_PROPERTIES
		* As the name suggests, this the "installer.properties" that allows you to customize the install
			of SPSS.  The available parameters are included; customize for your environment.

Do note that the postinstall script that "handles the upgrade" searches the /Applications folder for the version of 
SPSS being upgraded and will inject the path into the install.properties file so it does not need to be specified
in the INSTALL_PROPERTIES override variable below, which is described above.


            - **Identifier**: `com.github.mlbz521.jss.SPSSStatisticsPatch`

            - **Parent Recipes**: `com.github.mlbz521.pkg.SPSSStatisticsPatch`
