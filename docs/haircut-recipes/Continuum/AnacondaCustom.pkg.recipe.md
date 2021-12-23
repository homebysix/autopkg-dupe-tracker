# AnacondaCustom.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of Anaconda Python, then creates a package that installs Anaconda to a known location defined by the PREFIX_DIR key. The intent is to install Anaconda in a location accessible to all users on a system. The default PREFIX_DIR is '/usr/local/anaconda'. A postinstall script symlinks all the binaries in the anaconda 'bin' directory to /usr/local/bin so users do not have to individually update their paths.

Per the parent recipe, different installer types are available. 
Use INSTALLER_TYPE 'sh' for this recipe to work correctly!
You can choose the Python 2 or 3 version of Anaconda with the PYTHON_MAJOR_VERSION key.

The CONDARC_CONTENTS file controls what gets written to the "admin" or top-level .condarc path at PREFIX_DIR/.condarc
In the default configuration using the supplied variables we simply specify the "defaults" package channel. You can specificy whatever you need here.
! Make sure your spacing for this input variable is valid for YAML syntax !

            - **Identifier**: `com.github.haircut.pkg.AnacondaCustom`

            - **Parent Recipes**: `com.github.hansen-m.download.Anaconda`
