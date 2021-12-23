# CrowdStrikeFalcon.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads a CrowdStrike Falcon Sensor pkg via CrowdStrike's API and imports it into a munki repo.

You must provide a Client ID and Secret along with the Policy ID to determine which senor version to download.

You must also specify a LICENSE_ID in order to license the Sensor post install. postinstall script based on https://github.com/autopkg/MLBZ521-recipes/blob/master/CrowdStrike%20Falcon/CrowdStrike%20Falcon.pkg.recipe

            - **Identifier**: `com.github.apizz.munki.CrowdStrikeFalcon`

            - **Parent Recipes**: `com.github.mlbz521.download.CrowdStrikeFalcon`
