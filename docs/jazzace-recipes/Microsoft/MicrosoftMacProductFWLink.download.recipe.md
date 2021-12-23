# MicrosoftMacProductFWLink.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads any Microsoft product that can be located using a Microsoft FWLink number.
Because this recipe is targeted at Mac products, the download is assumed to be a package (.pkg).

NOTE: This recipe fills a niche. Most people would be better off considering the recipes in the
main recipes repo or the rtrouton-recipes repo (supplemented for Munki by dataJAR-recipes).

This recipe is designed to be used with an override or child recipe.

The value of the FWLink number should be assigned to the input variable PRODUCTID in your override.
Here are a few FWLink values that may be useful:

525136 - Microsoft 365/Office 2019 Suite
871743 - Office 2016 Suite
2009112 - Microsoft 365 BusinessPro Suite (with Teams)
869428 - Teams Standalone Installer
525134 - Word 2019/365

While you can find the FWLink value for a product in various places, a (manually-) complied source list 
can be found at macadmins.software (just look for the 6- or 7-digit number at the end of the appropriate link).

This recipe make no attempt to capture version information, but the filename should contain the version 
number (because Microsoft includes that in the package name). If you want to capture that as a variable, 
you could use the pkg recipes in the rtrouton-recipes repo as a model (or just use those recipes).


            - **Identifier**: `com.github.jazzace.download.microsoftmacproductfwlink`

            - **Parent Recipes**: `None`