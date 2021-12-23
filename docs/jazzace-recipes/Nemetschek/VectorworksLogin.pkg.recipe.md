# VectorworksLogin.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: This recipe creates a package that copies a prepared LoginDialog.xml file to the 
appropriate space in the user account such that the server settings for your instance are 
pre-populated. The package must be run in a user context (e.g., GUI session, Outset login-once,
ARD as current console user). Specify the full path to the LoginDialog.xml file in LOGIN_FILE_PATH.

The easiest way to obtain a properly formatted LoginDialog.xml file is to launch Vectorworks, 
manually adjust the settings (including Do Not Show At Startup) in the GUI, click Login, then
Quit. You will find the file at ~/Library/Application Support/Vectorworks/20##/Settings/SeriesG/
(substituting your Major Version for 20## and Series for G, which you then use as input variables).


            - **Identifier**: `com.github.jazzace.pkg.vectorworkslogin`

            - **Parent Recipes**: `None`
