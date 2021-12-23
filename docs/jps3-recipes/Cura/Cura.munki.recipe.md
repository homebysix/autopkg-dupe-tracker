# Cura.munki.recipe

_Last updated 2021-12-23 19:58:07Z_

- **Description**: Downloads the latest version of Cura 3D printer software as a dmg. From this it extracts Cura.app from the /Cura/ subfolder and copies to a new dmg file by itself. This new Cura.app only dmg is then imported into the Munki repository.

- **Identifier**: `com.github.jps3.munki.Cura`

- **Parent Recipes**: `com.github.jps3.download.Cura`

## Warnings

- These recipes have duplicate NAMEs:
    - [dataJAR-recipes/Ultimaker Cura/Ultimaker Cura.munki.recipe](/autopkg-dupe-tracker/dataJAR-recipes/Ultimaker Cura/Ultimaker Cura.munki.recipe)
    - [jps3-recipes/Cura/Cura.munki.recipe](/autopkg-dupe-tracker/jps3-recipes/Cura/Cura.munki.recipe)