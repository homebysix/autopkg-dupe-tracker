# ZendStudio.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Verifies your pre-downloaded Zend Studio download and prepares it for processing by child recipes.

Zend Studio can be downloaded here: https://www.zend.com/downloads/zend-studio
An email address is required to initiate the download.

Once you've downloaded, pass the resulting file in to this recipe using the PKG variable or -p flag:
    autopkg run -v ZendStudio.download -p ~/Downloads/ZendStudio-13.6.1-macosx.cocoa.x86_64.dmg

            - **Identifier**: `com.github.homebysix.download.ZendStudio`

            - **Parent Recipes**: `None`