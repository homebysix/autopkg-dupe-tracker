# webpage.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest version of a particular web page when it changes and makes a date-stamped copy.
Since this recipe simply captures the raw HTML, if you open the resulting file, it will often fail in resolving things
like stylesheets and internal links because any shorthand references will not point to the correct location.

This recipe date+timestamps the filename of the download, using Elliot Jordan’s FindAndReplace processor
to strip the (reserved) colons and " GMT" from the filename. You’ll need to add homebysix-recipes to your 
local RecipeRepos in order to run this recipe.

Input Keys:
    PAGE_URL is the full URI for the page to be checked/downloaded.
    SAVE_LOCATION is the path to the directory where the web page should be copied. The path must exist.
    PAGE_NAME_PREFIX is the text (if any) that will precede the datestamp in the (copied) filename.
This is useful if you are overriding this recipe multiple times and having the results sit in the same directory.

The default values act as a kind of RSS feed for Anthony Reimer’s MacLabs blog posts.
Override with the values that suit your use case.


            - **Identifier**: `com.github.jazzace.download.webpage`

            - **Parent Recipes**: `None`