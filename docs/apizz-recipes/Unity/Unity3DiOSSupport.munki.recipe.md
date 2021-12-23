# Unity3DiOSSupport.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Download the latest version of the Unity iOS Support pkg and imports it into a munki_repo.

Need to supply the munki item name for Unity 3D in UNITY_MUNKI_ITEM_NAME to correctly link this support installer to it along with the correct version.

A preinstall script in this support package checks to make sure the same version of Unity 3D is installed, otherwise it fails.

            - **Identifier**: `com.github.apizz.autopkg.munki.Unity3DiOS`

            - **Parent Recipes**: `com.github.apizz.autopkg.download.Unity3DiOS`