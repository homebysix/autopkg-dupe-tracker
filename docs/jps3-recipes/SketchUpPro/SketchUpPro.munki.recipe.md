# SketchUpPro.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of SketchUp Pro by looking for the first match on the download page, then imports into your Munki repo. 

You can specify LOCALE (default: en) for alternative languages. At last check locales were: en, de, es, fr, it, ja, ko.

Note (20-Mar-2018): The previous functionality of this recipe which attempted to allow for easy configuration of which "RELEASE_YEAR" version to download and process was not working well due to the not-quite-straightforward way the developer creates their URL patterns. For the time being that functionality has been reverted such that RELEASE_YEAR is used as a convenience variable to limit the number of locations you would need to edit in your overrides. (You will need to update or recreate your RecipeOverride(s) for these changes to take effect for you.

Note (21-Mar-2018): If you encounter any errors in AutoPkg with these recipes, I recommend: (a) recreate your override(s); (b) rename or delete the cached downloads as that has cleared up the majority of hdiutil-related errors for me. Whether you save your receipts or not is up to your conscience and accountant.


            - **Identifier**: `com.github.jps3.munki.SketchUpPro`

            - **Parent Recipes**: `com.github.jps3.download.SketchUpPro`


## Warnings

- These recipes have duplicate filenames, ignoring numbers:
    - [gregneagle-recipes/SketchUpPro/SketchUpPro2018.munki.recipe](/autopkg-dupe-tracker/gregneagle-recipes/SketchUpPro/SketchUpPro2018.munki.recipe)
    - [jps3-recipes/SketchUpPro/SketchUpPro.munki.recipe](/autopkg-dupe-tracker/jps3-recipes/SketchUpPro/SketchUpPro.munki.recipe)