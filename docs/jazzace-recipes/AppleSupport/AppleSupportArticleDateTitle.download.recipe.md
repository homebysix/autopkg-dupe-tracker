# AppleSupportArticleDateTitle.download.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of a particular Apple Support Article (specified in the input keys)
and, if it has updated, copies it to the designated directory as HTML.
The HTML file is named with the modification date, Article Number, and the Article Title 
(the date and title are automatically gathered from the downloaded file).

Input Keys:
    ARTICLE is the Apple Support Article number, usually two letters (HT) and six digits.
    LANG is the language and country descriptor, consisting of two letters for the language, a dash, and 
        two letters for the country (e.g., en-us). Many will want to force the US version in order to get
        the earliest indication of a change. 
    SAVE_LOCATION is the path to the directory where the HTML file should be saved. The path should exist. 


            - **Identifier**: `com.github.jazzace.download.AppleSupportArticleDateTitle`

            - **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate URLDownloader URLs:
    - [jazzace-recipes/AppleSupport/AppleSupportArticle.download.recipe](/autopkg-dupe-tracker/jazzace-recipes/AppleSupport/AppleSupportArticle.download.recipe)
    - [jazzace-recipes/AppleSupport/AppleSupportArticleDateTitle.download.recipe](/autopkg-dupe-tracker/jazzace-recipes/AppleSupport/AppleSupportArticleDateTitle.download.recipe)