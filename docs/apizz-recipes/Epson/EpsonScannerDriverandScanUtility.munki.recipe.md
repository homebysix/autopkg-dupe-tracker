# EpsonScannerDriverandScanUtility.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest version of the Epson Scanner Driver and EPSON Scan Utility from Epson's site and imports it into a munki repo.  

IMPORTANT:
This recipe requires that you find the support page for your product and copy that URL for 
use as the base string for the SEARCH_URL key in your override. In order for the recipe to 
work, the target OS must be explicitly specified in the URL.

Recommended Procedure for Creating URL:
1. Go to the Epson site for your country.
2. Find the support page for your Epson device.
3. The support page will attempt to determine your current OS version and will display that 
in a pop-up menu on the page. If that is OS you are targeting for deployment, temporarily 
change the value in that popup menu to any other OS, wait a second (enough for the page to 
quickly reload), and then change to the OS you are targeting for deployment. If you are 
targeting a different OS, then directly change the OS in the popup menu. 
4. Copy the URL.
5. Create an override of this recipe (or edit an existing override).
6. In the Input section, paste the URL that you copied earlier into the string for SEARCH_URL.
7. Check the URL you just pasted. Confirm that it ends with one of the following strings
(substituting the number of the OS as appropriate). You can append this string if it is not 
present. 

For macOS 10.12 and later:     ?review-filter=macOS+10.12.x
For OS X 10.11.x and earlier:  ?review-filter=Mac+OS+X+10.11.x

For example, the URL for the Epson Perfection V850 Pro fetched from the US Epson site with macOS Mojave as the deployment OS is:

    https://epson.com/Support/Scanners/Perfection-Series/Epson-Perfection-V850-Pro/s/SPT_B11B224201?review-filter=macOS+10.14.x

            - **Identifier**: `com.github.apizz.munki.EpsonScannerDriverandScanUtility`

            - **Parent Recipes**: `com.github.apizz.download.EpsonScannerDriverandScanUtility`

## Warnings

- These recipes have duplicate NAMEs:
    - [apizz-recipes/Epson/EpsonScannerDriverandScanUtility.munki.recipe](/autopkg-dupe-tracker/apizz-recipes/Epson/EpsonScannerDriverandScanUtility.munki.recipe)
    - [apizz-recipes/Epson/EpsonScannerDriverandScanUtility-NewCert.munki.recipe](/autopkg-dupe-tracker/apizz-recipes/Epson/EpsonScannerDriverandScanUtility-NewCert.munki.recipe)