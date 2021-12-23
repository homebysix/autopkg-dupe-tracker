# Office2019SuiteSKUless_additionalpkginfo.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: 
			Very specific fork for Office 2019 Suite.

			Downloads the latest Microsoft Office 2019 SKU-less installer package.

			Set the REGION key to:

			525133 for Office 365 and Americas Volume LATEST (default)
			871743 for Office 2016

			Due to the Downloads using Microsoft's Global CDN's the region code is now for type of installer

			Set the INSTALLERTYPE key to (this is for version only!):

			o365 for Office 365 (default)
			vl2019 for Office 2019
			vl2016 for Office 2016


            - **Identifier**: `com.github.wardsparadox.Office2019SuiteSKUless-additionalpkginfo.munki`

            - **Parent Recipes**: `com.github.autopkg.office-recipes.download.Office2019Suite`