# ARCHICADUpdate.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Imports the latest update build of ARCHICAD into munki which has been downloaded by its parent based on the override-able parameters: MAJOR_VERSION, LOCALIZATION, and RELEASE_TYPE
The installation target can be changed by setting INSTALL_DIR to a different location. Useful e.g. if multiple language versions should be available on a Mac.

MAJOR_VERSION options include:  20, 21, 22, 23, and 24
LOCALIZATION options include:  INT (international english, part of many other licenses), AUS, AUT, BRA, CHE, CHI, CZE, FIN, FRA, GER, GRE, HUN, ITA, JPN, KOR, NED, NOR, NZE, POL, POR, RUS, SPA, SWE, TAI, TUR, UKI, UKR, and USA
RELEASE_TYPE options include:  AC (for full version), SOLO, and START
MINIMUM_OS_VERSION: AC 20: 10.9, AC 21: 10.10, AC 22: 10.11, AC 23: 10.13, AC 24: 10.13. These are the absolute minimum versions as stated by GRAPHISOFT. Some are listed as "untested but should run".


            - **Identifier**: `com.github.wycomco.munki.ARCHICADUpdate`

            - **Parent Recipes**: `com.github.wycomco.download.ARCHICADUpdate`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [wycomco-recipes/archicad_updates/ARCHICADUpdate.munki.recipe](/autopkg-dupe-tracker/wycomco-recipes/archicad_updates/ARCHICADUpdate.munki.recipe)
    - [robperc-recipes/ArchiCad/ArchiCAD19Update.munki.recipe](/autopkg-dupe-tracker/robperc-recipes/ArchiCad/ArchiCAD19Update.munki.recipe)
    - [robperc-recipes/ArchiCad/ArchiCAD18Update.munki.recipe](/autopkg-dupe-tracker/robperc-recipes/ArchiCad/ArchiCAD18Update.munki.recipe)