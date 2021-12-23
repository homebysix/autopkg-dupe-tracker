# JumpCloud Agent.munki.recipe

        _Last updated 2021-12-23 20:01:50Z_

        - **Description**: Downloads the current release version of the JumpCloud Agent and then uploads to munki.

NOTE: The bootstrap.json file should be deployed to /opt/jc/agentBootstrap.json before
installing this PKG, else you'll be prompted for the connect_key. 
Amend the preinstall_script for this.

See: https://support.jumpcloud.com/customer/portal/articles/2389320-agent-deployment-via-command-line


        - **Identifier**: `com.github.dataJAR-recipes.munki.JumpCloud Agent`

        - **Parent Recipes**: `com.github.dataJAR-recipes.download.JumpCloud Agent`
