# CorelDRAWUpdate.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest updates for CorelDRAW and imports it into Munki. The base version is modifiable via the BASE_VERSION input variable. 
		The architecture can be chosen from Intel and M1 by modifying the ARCHITECTURE variable. 
		Additionally the SUPPORTED_ARCHITECTURE variable has to be adjusted accordingly to x86_64 (Intel) or arm64 (M1)

            - **Identifier**: `com.github.its-unibas.munki.CorelDRAWUpdate`

            - **Parent Recipes**: `com.github.its-unibas.download.CorelDRAWUpdate`