# OracleJava8.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest Oracle Java 8 JRE CPU release and copies out the flat installer pkg
within the installer app wrapper, appending the version number to the filename.
(Note the version of the actual pkg id for the com.oracle.jre pkg component is still
always "1.0".)

Read more about CPU and PSU releases here:
    http://www.oracle.com/technetwork/java/javase/downloads/cpu-psu-explained-2331472.html

To use this recipe, you must accept the Oracle Binary Code License Agreement for Java SE.
http://www.oracle.com/technetwork/java/javase/terms/license/index.html


            - **Identifier**: `com.github.autopkg.pkg.OracleJava8`

            - **Parent Recipes**: `com.github.autopkg.download.OracleJava8`