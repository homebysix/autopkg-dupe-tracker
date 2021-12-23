# OracleJava8.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest Oracle Java 8 JRE CPU release and imports into Munki.
The flat installer pkg within the installer app is copied out and imported.

Read more about CPU and PSU releases here:
    http://www.oracle.com/technetwork/java/javase/downloads/cpu-psu-explained-2331472.html

To use this recipe, you must accept the Oracle Binary Code License Agreement
for Java SE.
http://www.oracle.com/technetwork/java/javase/terms/license/index.html

The package's receipt version is useless, so we make an installs item for
the prefPane bundle, which has historically had consistent versioning.


            - **Identifier**: `com.github.autopkg.munki.OracleJava8`

            - **Parent Recipes**: `com.github.autopkg.download.OracleJava8`