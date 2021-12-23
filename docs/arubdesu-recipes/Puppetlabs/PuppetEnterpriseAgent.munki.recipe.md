# PuppetEnterpriseAgent.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest PuppetAgent and imports into Munki.

OS_VERSION can be overridden for the specific package, or left to the current
latest OS available. As some of the vendored contents (like ruby and libraries) are compiled
specifically for each OS, we're setting the 'minimum_os_version' and 'maximum_os_version' keys.

            - **Identifier**: `com.github.autopkg.arubdesu-recipes.munki.PuppetEnterpriseAgent`

            - **Parent Recipes**: `com.github.autopkg.arubdesu-recipes.download.PuppetEnterpriseAgent`
