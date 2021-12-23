# Puppet.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest Puppet using Puppet Labs' Mac download list at
downloads.puppetlabs.com/mac, and imports into Munki.

Note that Puppet requires Facter.

VERSION can be overridden with a specific version number, or left to
the default, 'latest'.

            - **Identifier**: `com.github.autopkg.munki.puppet`

            - **Parent Recipes**: `com.github.autopkg.download.puppet`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [gerardkok-recipes/Puppet/Puppet6.munki.recipe](/autopkg-dupe-tracker/gerardkok-recipes/Puppet/Puppet6.munki.recipe)
    - [gerardkok-recipes/Puppet/Puppet5.munki.recipe](/autopkg-dupe-tracker/gerardkok-recipes/Puppet/Puppet5.munki.recipe)
    - [recipes/Puppetlabs/Puppet.munki.recipe](/autopkg-dupe-tracker/recipes/Puppetlabs/Puppet.munki.recipe)