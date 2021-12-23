# InspireDesignerExportCC2014.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Packages Inspire Designer Export plugin for InDesign CC 2014 and imports it into Munki

NOTES:
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add hjuutilainen's repo via:

autopkg repo-add hjuutilainen-recipes

- This recipe points to the default installation location of InDesign CC 2014.  Adjust the path as needed.
- This recipe does not download the Inspire Designer Export plugin disk image--feed the disk image into the recipe via the following format:

autopkg run InspireDesignerExportCC2014.munki -p /path/to/Adobe-InDesign-CC-Plugin-10.0.1-GA.dmg

            - **Identifier**: `com.github.foigus.munki.InspireDesignerExportPluginCC2014`

            - **Parent Recipes**: `com.github.foigus.pkg.InspireDesignerExportPluginCC2014`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [foigus-recipes/GMCSoftware/InspireDesigner12ExportCC2018.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesigner12ExportCC2018.munki.recipe)
    - [foigus-recipes/GMCSoftware/InspireDesigner11ExportCC2017.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesigner11ExportCC2017.munki.recipe)
    - [foigus-recipes/GMCSoftware/InspireDesigner14ExportCC2020.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesigner14ExportCC2020.munki.recipe)
    - [foigus-recipes/GMCSoftware/InspireDesignerExportCC2015.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesignerExportCC2015.munki.recipe)
    - [foigus-recipes/GMCSoftware/InspireDesignerExportCC2014.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesignerExportCC2014.munki.recipe)
    - [foigus-recipes/GMCSoftware/InspireDesigner11ExportCC2015.munki.recipe](/autopkg-dupe-tracker/foigus-recipes/GMCSoftware/InspireDesigner11ExportCC2015.munki.recipe)