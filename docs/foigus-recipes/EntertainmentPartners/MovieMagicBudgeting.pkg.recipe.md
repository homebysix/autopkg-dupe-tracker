# MovieMagicBudgeting.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Packages Movie Magic Budgeting.

Notes:
- This recipe requires installing BOTH AutoPkg AND the Movie Magic Budgeting itself--the latter BY HAND.  IDEALLY this would occur in a clean virtual machine, and is not intended to occur on an AutoPkg "server".  Thank Flexera InstallAnywhere and a cross-platform Java-based application for this incredibly strange recipe.
- This recipe skips installing the template budgets in the user's home directory.  These are available in the "MMData" folder in the application's folder.
- Currently the installation package can be downloaded here https://www.ep.com/home/managing-production/movie-magic-budgeting/

I'm skipping a few things I normally do for my AutoPkg recipes:
- CodeSignatureVerifier: Presumably this software has been manually sourced from a trusted location and then manually installed
- A .munki Recipe: Since the retrieval of the Movie Magic Budgeting installer is manual, the installation is manual, and running this recipe on a clean VM is manual, there doesn't seem to make much sense to automate the import of the resulting package into Munki.  Due to the lack of a .munki recipe, please ensure your pkginfo has "MM Budgeting" as a blocking_application

            - **Identifier**: `com.github.foigus.pkg.MovieMagicBudgeting`

            - **Parent Recipes**: `None`