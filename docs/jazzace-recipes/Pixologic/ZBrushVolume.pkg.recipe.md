# ZBrushVolume.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: This recipe takes the ZBrush volume license installer app that you have already downloaded and 
creates a package that leverages the silent install CLI method to automate installation. Additionally, the
postinstall script adds the volume licensing files (specific to your installation, provided by Pixologic) 
and a modified DefaultZScript.txt file (e.g., to keep ZHomePage from starting at launch every time)
to the correct locations in the application's directories.
This version of the recipe supports ZBrush 2021.5 and later and requires the homebysix-recipes repo.

Input Variables of note:
• LIC_FILES_DIR is the path to the local *directory* that holds the volume licensing files
  (license_ZBrush*_1seat.lic and FloatingLicenseDLL.lib will be used);
• ZSCRIPT_FILE is the path to the *file* you wish to use for DefaultZScript.txt
  (a sample file that suppresses the launch of ZHomePage upon opening the app is included in 
  the repo for this recipe).

Once the input variables are set (likely in an override), your command to create the pkg will
look something like this:

    autopkg run ZBrushVolume.pkg -p ~/Downloads/ZBrush_2021.6_FL_Installer.dmg

(Substitute the actual path to your downloaded disk image.)

            - **Identifier**: `com.github.jazzace.pkg.zbrushvolume`

            - **Parent Recipes**: `None`