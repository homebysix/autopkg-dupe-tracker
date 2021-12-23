# EpsonProDrivers.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest version of the Epson product driver from Epson's site.
These will generally be drivers for professional printers and the like not included in
the drivers supplied by Apple.
Make separate overrides for each device driver you may want. An override is required.

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

For example, the URL for the Epson Stylus Pro 3880 fetched from the Canadian Epson site with 
macOS Catalina as the deployment OS is:

   https://epson.ca/Support/Printers/Professional-Imaging-Printers/Epson-Stylus-Pro-Series/Epson-Stylus-Pro-3880/s/SPT_CA61201-VM?review-filter=macOS+10.15.x

(The US URL is the same, except it is .com instead of .ca. Only the Canadian and US sites 
have been tested.)

This recipe uses Epson's new code signing authority. Turn off code signature verification
if you require older installers.


            - **Identifier**: `com.github.jazzace.download.EpsonProDrivers`

            - **Parent Recipes**: `None`