# BrotherPrinter.jss.recipe

            _Last updated 2021-12-23 19:58:06Z_

            - **Description**: Downloads the Brother Printer Driver, Software Package, Utility, or Firmware specified, creates a package, and uploads it to the JPS.  Obviously some packages are compatible with different models, but I haven't been able to think of a way to specify this in the name without it being extremely long.  You will need to specify the model specifically for this to work, take a look at the examples below.

How to specify the Model:
 - MFC-J6935DW = mfcj6935dw
 - HL-L9200CDWT = hll9200cdwt
 - HL-L9310CDW = hll9310cdw

Specify which OS Version:
 - Catalina = 10060
 - Mojave = 10052
 - High Sierra = 10045
 - Sierra = 10030
 - El Capitan = 10018
 - Yosemite = 10006
 - Mavericks = 132

Type:
 - Full Driver & Software Package = 583
 - Printer Driver = 10062
 - Scanner Driver = 10063
 - IPrint&Scan Push Scan Tool = 10381
 - Internet FAX Install Tool = 78
 - Firmware Update Tool = 318

This probably isn't the best way to do it, but it works...

            - **Identifier**: `com.github.mlbz521.jss.BrotherPrinter`

            - **Parent Recipes**: `com.github.mlbz521.pkg.BrotherPrinter`