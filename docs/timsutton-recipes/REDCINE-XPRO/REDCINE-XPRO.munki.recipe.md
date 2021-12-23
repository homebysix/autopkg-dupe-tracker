# REDCINE-XPRO.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest version of REDCINE-X PRO and imports into Munki.

There is some manipulation of the version info, to ensure a number
that always increases. The REDCINE-X PRO.app contains a CFBundleVersion
like "MAJOR.BUILDNUMBER." The package has historically added a point
version between these two numbers only for some releases, resulting
in a version that doesn't always compare higher. For this reason
we extract the CFBundleVersion and compare with this, as well as set
the pkginfo version with this so that our latest is always the highest.


            - **Identifier**: `com.github.timsutton.munki.redcine-xpro`

            - **Parent Recipes**: `com.github.timsutton.download.redcine-xpro`