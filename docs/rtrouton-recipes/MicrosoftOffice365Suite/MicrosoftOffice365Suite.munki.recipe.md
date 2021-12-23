# MicrosoftOffice365Suite.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest Microsoft Office 365 SKU-less installer suite package,
appends the version to the end of the filename, and imports into Munki.

      Set the ID key to:
      525133 for Americas (default)
      532572 for Europe
      532577 for Asia

            - **Identifier**: `com.github.rtrouton.munki.MicrosoftOffice365Suite`

            - **Parent Recipes**: `com.github.rtrouton.download.MicrosoftOffice365Suite`
