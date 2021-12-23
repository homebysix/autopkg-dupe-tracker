# GenericFieryFD50.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Deconstruct a Fiery driver package, remove the Fiery Driver Updater.app, and repack.  The FD50 and FD51-revision Fiery drivers appear to properly handle installing when COMMAND_LINE_INSTALL is set.

To start, download a FD50 or FD51 driver from:
http://www.efi.com/support-and-downloads/download-registration/

Note the name of the downloaded driver dmg (e.g. "Ricoh_E41_v1_0R_FD51_v1Cert.dmg") and create an override using the dmg name:
autopkg make-override GenericFieryFD50.pkg -n Ricoh_E41_v1_0R_FD51_v1Cert.pkg

Set the Input in the override to the following suggested items:
- NAME of the downloadable DMG without ".dmg", and adding "_No_Update" (e.g. Ricoh_E41_v1_0R_FD51_v1Cert_No_Update)
- PACKAGE_ID of com.efi.DMG-Name-with-hyphens-substituted-for-underscores.pkg
  (e.g. com.efi.Ricoh-E41-v1-0R-FD51-v1Cert.pkg)
- PACKAGE_VERSION of 1.$version, where $version is the digits after "FD" in the downloaded driver (e.g. 1.51)

Run the recipe with the "-p" option pointing to the downloaded driver dmg:
autopkg run Ricoh_E41_v1_0R_FD51_v1Cert.pkg -p /path/to/Ricoh_E41_v1_0R_FD51_v1Cert.dmg

Also note that the way that EFI's package postinstall is written causes it to behave differently when COMMAND_LINE_INSTALL is set.  When testing the output package, make sure to use "installer" rather than double-clicking the package.  From a different point of view, when the package output from this recipe installed via the GUI (i.e. Installer.app) it will NOT have the desired result of skipping the Fiery Driver Updater installation and running non-interactively.

            - **Identifier**: `com.github.foigus.pkg.GenericFieryFD50`

            - **Parent Recipes**: `com.github.foigus.download.GenericFieryFD50`