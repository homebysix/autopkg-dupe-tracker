# AccuBarcodeProwithJRE.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Packages Accubarcode Pro with JRE.

NOTES

- This recipe requires installing BOTH AutoPkg AND Accubarcode Pro with JRE itself--the latter BY HAND.  IDEALLY this would occur in a clean virtual machine, and is not intended to occur on an AutoPkg "server"--thank Install4j for this incredibly strange recipe
- This recipe uses relative paths (to obtain the fonts installed in the user's home directory) and assumes the AutoPkg Cache is at the default location of "~/Library/AutoPkg/Cache"--ensure the same user installs Accubarcode Pro with JRE and runs this recipe
- This recipe depends on jessepeterson's ModeChanger.  Add jessepeterson's repo via:

autopkg repo-add jessepeterson-recipes

- I'm skipping a few things I normally do for my AutoPkg recipes:
  - CodeSignatureVerifier: Presumably this software has been manually sourced from a trusted location and then manually installed
  - A .munki Recipe: Since the retrieval of the Accubarcode Pro with JRE installer is manual, the installation is manual, and running this recipe on a clean VM is manual, there doesn't seem to make much sense to automate the import of the resulting package into Munki

            - **Identifier**: `com.github.foigus.pkg.AccuBarcodeProwithJRE`

            - **Parent Recipes**: `None`
