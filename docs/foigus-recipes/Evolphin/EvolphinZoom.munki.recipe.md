# EvolphinZoom.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Packages Evolphin Zoom for installation and imports it into Munki.

NOTES:
- This recipe depends on hjuutilainen's ChecksumVerifier.  Add hjuutilainen's repo via:

autopkg repo-add hjuutilainen-recipes

- This recipe does not download the Evolphin Zoom package--feed the package into the recipe via the following format:

autopkg run EvolphinZoom.munki -p /path/to/EvolphinZoom.pkg

- Evolphin recommends non-current versions of AIR.  See here:

http://help.evolphin.com/docs/drag-and-drop-stopped-working-in-the-asset-browser/

            - **Identifier**: `com.github.foigus.munki.EvolphinZoom`

            - **Parent Recipes**: `com.github.foigus.pkg.EvolphinZoom`