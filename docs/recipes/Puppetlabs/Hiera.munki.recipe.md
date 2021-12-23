# Hiera.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest Hiera using Puppet Labs' Mac download list at
downloads.puppetlabs.com/mac, and imports into Munki.

VERSION can be overridden with a specific version number, or left to
the default defined in the download recipe, 'latest'.

            - **Identifier**: `com.github.autopkg.munki.hiera`

            - **Parent Recipes**: `com.github.autopkg.download.hiera`
