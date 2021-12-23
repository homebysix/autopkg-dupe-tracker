# spartan.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of Spartan from www.wavefun.com and imports it into Munki
			The Versioner Processor overwrites the version defined in the download recipe because the CFBundleVersion is better for munki to process. 
			With the CFBundleShortVersionString as display name the full version name will be visible in the Managed Software Centre.


            - **Identifier**: `com.github.its-unibas.munki.spartan`

            - **Parent Recipes**: `com.github.its-unibas.download.spartan`
