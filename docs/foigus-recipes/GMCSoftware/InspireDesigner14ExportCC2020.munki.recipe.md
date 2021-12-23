# InspireDesigner14ExportCC2020.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Packages Inspire Designer 14 Export plugin for InDesign CC 2020 and imports it into Munki

NOTES:
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add hjuutilainen's repo via:

autopkg repo-add hjuutilainen-recipes

- This recipe points to the default installation location of InDesign CC 2020.  Adjust the path as needed.
- This recipe does not download the Inspire Designer 14 Export plugin disk image--feed the disk image into the recipe via the following format:

autopkg run InspireDesigner14ExportCC2020.munki -p /path/to/Adobe-InDesign-2020-Plugin-12.0.6-Hotfix.dmg

            - **Identifier**: `com.github.foigus.munki.InspireDesigner14ExportCC2020`

            - **Parent Recipes**: `com.github.foigus.pkg.InspireDesigner14ExportCC2020`

## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/GMCSoftware/InspireDesigner12ExportCC2018.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesigner12ExportCC2018.munki.recipe)
    - [foigus-recipes/GMCSoftware/InspireDesigner11ExportCC2017.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesigner11ExportCC2017.munki.recipe)
    - [foigus-recipes/GMCSoftware/InspireDesigner14ExportCC2020.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesigner14ExportCC2020.munki.recipe)
    - [foigus-recipes/GMCSoftware/InspireDesignerExportCC2015.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesignerExportCC2015.munki.recipe)
    - [foigus-recipes/GMCSoftware/InspireDesignerExportCC2014.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesignerExportCC2014.munki.recipe)
    - [foigus-recipes/GMCSoftware/InspireDesigner11ExportCC2015.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesigner11ExportCC2015.munki.recipe)