# Zscaler.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads Zscaler Mac app and imports into Munki.

If a logout/uninstall password is required for removing Zscaler, you can specify it in the
UNINSTALL_PASSWORD input variable. Please note that if you do this, there is a chance that end users
may be able to reverse-engineer the password; however if you're already providing the uninstall
option in MSC, the assumption is that this is not a concern.

            - **Identifier**: `com.github.homebysix.munki.Zscaler`

            - **Parent Recipes**: `com.github.rtrouton.pkg.zscaler`