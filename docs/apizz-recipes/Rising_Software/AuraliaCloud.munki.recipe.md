# AuraliaCloud.munki.recipe

_Last updated 2021-12-23 20:01:50Z_

- **Description**: Downloads the latest version of Auralia Cloud and imports it into a munki_repo. Need to set MAJOR_VERSION, PLATFORM, and FILETYPE variables. PLATFORM should be either m (Mac) or w (Windows). FILETYPE should be pkg (Mac) or exe (Windows).

- **Identifier**: `com.github.apizz.munki.AuraliaCloud`

- **Parent Recipes**: `com.github.hansen-m.download.AuraliaCloud`
