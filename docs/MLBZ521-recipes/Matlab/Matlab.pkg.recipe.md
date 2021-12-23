# Matlab.pkg.recipe

            _Last updated 2021-12-23 20:01:49Z_

            - **Description**: Downloads and packages the latest verison of Matlab from a local file share.

I license most software separately in environment and do not use the built licensePath key.  If you want to use this, you'll want to fork this recipe more than likely.

One override variable is avilable to support the installation of Matlab:
	* INSTALL_INPUT
		* As the name suggests, this is the "installer.input" that allows you to customize the install
			of Matlab.  The available parameters are included; customize for your environment.

If you want to customize the products that are installed, a copy of an original, albeit old, installer_input.txt is available in the recipe directory.

I've seen people are unable to locate it as it's not included in newer versions even though the documentation points to it.


            - **Identifier**: `com.github.mlbz521.pkg.Matlab`

            - **Parent Recipes**: `com.github.mlbz521.download.Matlab`
