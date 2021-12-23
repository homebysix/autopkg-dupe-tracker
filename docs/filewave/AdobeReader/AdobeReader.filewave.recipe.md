# AdobeReader.filewave.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest Adobe Reader and imports into FileWave.
Set MAJOR_VERSION to "10" to get the latest/last version of Adobe Reader 10 instead of 11.

Additional notes:
- The Reader website states that 10.6.4 is a minimum requirement for 11.
- The preinstall_script is there to get around an oversight in the package's
preflight script, looking to find a user's trash folder to copy the .app into.


            - **Identifier**: `com.github.autopkg.filewave.AdobeReader`

            - **Parent Recipes**: `com.github.autopkg.download.AdobeReader`
