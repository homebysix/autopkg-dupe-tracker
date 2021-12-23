# AdobeAcrobatProXUpdate.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads updates for Adobe Acrobat Pro X or XI and imports them 
into Munki. It will also set the appropriate 'requires' item for the 
previous update in the Munki pkginfo, if applicable. Historically, 
quarterly scheduled updates have been cumulative for Pro X/XI, and
out-of-cycle updates have not.

The name(s) in update_for in the pkginfo should be set to the name
of your base Adobe Acrobat Pro X or XI installer item in your Munki repo.

MAJOR_VERSION can be '10', '11', corresponding to Pro X, Pro XI, 
etc. You can override this recipe multiple times for different
values of MAJOR_VERSION.

VERSION can be a specific update version, ie. '10.1.6', or the 
default, 'latest'.

            - **Identifier**: `com.github.autopkg.munki.AdobeAcrobatProXUpdate`

            - **Parent Recipes**: `com.github.autopkg.download.AdobeAcrobatProXUpdate`
