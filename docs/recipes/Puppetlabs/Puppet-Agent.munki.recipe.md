# Puppet-Agent.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest PuppetAgent and imports into Munki.

OS_VERSION can be overridden for the specific package, or left to the current
latest OS. As some of the vendored contents (like ruby and libraries) are compiled
specifically for each OS, we're setting the 'minimum_os_version' and 'maximum_os_version' keys.

            - **Identifier**: `com.github.autopkg.munki.puppet-agent`

            - **Parent Recipes**: `com.github.autopkg.download.puppet-agent`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [grahamgilbert-recipes/Puppetlabs/Puppet-Agent5.munki.recipe](/autopkg-dupe-tracker/grahamgilbert-recipes/Puppetlabs/Puppet-Agent5.munki.recipe)
    - [recipes/Puppetlabs/Puppet-Agent.munki.recipe](/autopkg-dupe-tracker/recipes/Puppetlabs/Puppet-Agent.munki.recipe)

- These recipes have duplicate NAMEs:
    - [grahamgilbert-recipes/Puppetlabs/Puppet-Agent5.munki.recipe](/autopkg-dupe-tracker/grahamgilbert-recipes/Puppetlabs/Puppet-Agent5.munki.recipe)
    - [recipes/Puppetlabs/Puppet-Agent.munki.recipe](/autopkg-dupe-tracker/recipes/Puppetlabs/Puppet-Agent.munki.recipe)