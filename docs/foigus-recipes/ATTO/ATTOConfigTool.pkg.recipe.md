# ATTOConfigTool.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Packages ATTO Config Tool.

Note: This recipe requires installing BOTH AutoPkg AND the ConfigTool itself--the latter BY HAND.  IDEALLY this would occur in a clean virtual machine, and is not intended to occur on an AutoPkg "server".  Thank Flexera InstallAnywhere and a cross-platform Java-based application for this incredibly strange recipe.

I'm skipping a few things I normally do for my AutoPkg recipes:
- CodeSignatureVerifier: Presumably this software has been manually sourced from a trusted location and then manually installed
- A .munki Recipe: Since the retrieval of the ConfigTool installer is manual, the installation is manual, and running this recipe on a clean VM is manual, there doesn't seem to make much sense to automate the import of the resulting package into Munki

            - **Identifier**: `com.github.foigus.pkg.ATTOConfigTool`

            - **Parent Recipes**: `None`