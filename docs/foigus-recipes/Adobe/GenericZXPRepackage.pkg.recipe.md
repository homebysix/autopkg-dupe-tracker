# GenericZXPRepackage.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Repackage an Adobe ZXP extension.

NOTE:

- This recipe expects an unencrypted .zxp file.  These are NOT available from Adobe Exchange, they either must be obtained from the vendor directly or by building an Admin Console package that contains the Extension (and thus contains the .zxp file)
- It's highly-suggested to create overrides of this recipe with unique names, such as "autopkg make-override GenericZXPRepackage.pkg -n FoobarbazExtension.pkg"
- The NAME, PACKAGE_ID, and EXTENSION_PATH values _must_ be overridden to run this recipe
- EXTENSION_PATH can be determined by installing the extension and looking for the extension name in /Library/Application Support/Adobe/CEP/extensions 
- This recipe does not download the .zxp file--feed the source file into the recipe via the following format:
autopkg run FoobarbazExtension.pkg -p /path/to/FoobarbazExtension_Install.pkg/Contents/Resources/post/addon/ZXP/123456.zxp

            - **Identifier**: `com.github.foigus.pkg.GenericZXPRepackage`

            - **Parent Recipes**: `None`
