# CentrifyDC.pkg.recipe

    _Last updated 2021-12-23 20:01:50Z_

    - **Description**: 
This recipe unpacks the Centrify DirectControl package, and modifies it to exclude interactive scripts.
See "Installing remotely using Apple Remote Desktop" pg. 253 of "Admin Guide For Mac OS X.pdf".

I have not included the option to modify the `userscript` file inside the package to join a domain.
You can join a domain using your own configuration system, or using Munki's postinstall_script variable.

To do this, you can edit the CentrifyDC pkginfo file, and add a script containing `adjoin` for example:

        #!/bin/sh
        adjoin --password *adminpassword* *domain*

See the admin guide, included with the installer for more information on the parameters to `adjoin`.
You should run `adcheck [domain]` on each machine to make sure that it meets the agent pre-requisites. You may need to write your own wrapper for
this, as the `adcheck` command returns different codes, that you may want to interpret as success.

Variables:

TGZ_PATH: An absolute path to a downloaded copy of Centrify DirectControl for Mac from the Centrify Support Portal (tgz version).
VERSION:  The DirectControl version number, used when packaging. (The version number is not automatically determined yet).
NAME:     Base package name, defaults to CentrifyDC
PLATFORM: (Unused) Will be used to identify the dmg filename, currently not used.

Caveats:

Version is not determined (best location pkgroot/centrifydc.pkg/PackageInfo, pkg-info bundle id=com.centrify.CentrifyDC CFBundleShortVersionString)
adcheck isnt included in the install condition?
Detect minimum OS from original flat package, this is scripted so unsure about methodology.


    - **Identifier**: `com.github.mosen.pkg.CentrifyDC`

    - **Parent Recipes**: `None`
