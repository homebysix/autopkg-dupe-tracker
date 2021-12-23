# AdobeAcrobatPro9Update.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads updates for Adobe Acrobat Pro 9 and imports them into
Munki. It will also set the appropriate 'requires' item for the
previous update in the Munki pkginfo.

Acrobat Pro 9 updates get their own installer type in Munki,
and makepkginfo will handle requiring a logout for these. Acrobat
Pro 9 uses a separate recipe from X/XI as its download is provided
as a zip file, which must be re-packed to a .dmg.

The name(s) in update_for in the pkginfo should be set to the name
of your base Adobe Acrobat Pro 9 item in your Munki repo.

VERSION can be a specific update version, ie. '9.5.2', or the
default, 'latest'.

            - **Identifier**: `com.github.autopkg.munki.AdobeAcrobatPro9Update`

            - **Parent Recipes**: `com.github.autopkg.download.AdobeAcrobatPro9Update`