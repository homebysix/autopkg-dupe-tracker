# SketchUpPro.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest version of SketchUp Pro by looking for the first match on the download page. 

You can specify LOCALE (default: en) for alternative languages. At last check (21-Mar-2018) locales were: en, de, es, fr, it, ja, ko, pt-BR, ru, sv, zh-CN, and zh-TW.

(The previous functionality of this recipe which attempted to allow for easy configuration of which "RELEASE_YEAR" version to download/import/etc was not working well. For the nonce that functionality has been reverted. You will need to update or recreate your RecipeOverride(s). The RELEASE_YEAR variable is just used to help with consistent naming, _NOT_ in choosing which version to download.)

Note: It sppears that every major release is done annually and requires and updated license. You will want to keep that in mind if you are automating your deployments without testing!


            - **Identifier**: `com.github.jps3.download.SketchUpPro`

            - **Parent Recipes**: `None`