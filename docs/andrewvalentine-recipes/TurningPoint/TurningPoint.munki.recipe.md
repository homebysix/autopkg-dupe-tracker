# TurningPoint.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads and imports the current version of TurningPoint into Munki. Note the following:

- A preinstall script is provided that removes the old TurningPoint.app. As Turning Technologies changed the bundle name to TurningPoint App.app, this step is required if you want to remove the deprecated bundle as part of the update.
- A postinstall script is provided that automates the setup of integration with Microsoft Powerpoint.
- An uninstall script is provided that removes the .app and the CFMSupport directory.

If you do not wish to use these scripts, you should address this in your recipe override.

If you work in a business or educational environment, you should be aware of what version of the software your organization currently supports and is licensed for before using this recipe.

            - **Identifier**: `com.github.andrewvalentine.munki.TurningPoint`

            - **Parent Recipes**: `com.github.andrewvalentine.download.TurningPoint`
