# FieryEX550_560.pkg.recipe

        _Last updated 2021-12-23 19:58:07Z_

        - **Description**: 
Convert the Fiery driver to a non-interactive installer package by removing the Install Wizard.app

The original installer works by installing to "/tmp/Fiery Printer Driver Installer.app", then the postinstall executes or copies from
inside the bundle. The outer flat package "Fiery Printer Driver.pkg" seems to do nothing much apart from running the single contained package.

Our strategy is to extract and unpack the inner package, delete the interactive wizard (causing the postinstall to skip the interactive setup),
and then re-pack the installer with the original postinstall scripts.


        - **Identifier**: `com.github.mosen.pkg.FieryEX550_560`

        - **Parent Recipes**: `com.github.mosen.download.FieryEX550_560`