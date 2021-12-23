# TeamViewerHostCustom.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest version of TeamViewer Host and imports it into a munki_repo.

The postinstall_script depends on supplying your custom module's config ID (ex. idc1a2b3c4)

NOTE:
- This recipe depends on keeleysam's MunkiPkginfoReceiptsEditor for marking certain pkg receipts as optional.  Add the repo via:

autopkg repo-add keeleysam-recipes

            - **Identifier**: `com.github.apizz.munki.TeamViewerHostCustom`

            - **Parent Recipes**: `com.github.apizz.pkg.TeamViewerHostCustom`