# alberta-covid-19.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the Alberta COVID-19 Data page and date stamps it using the date at the 
top of the web page (the last date of full results). Designed to run daily.
This saves the web page and the following 4 data sets: Case, Summary, Geospatial, and Vaccine.
Input Keys:
    SAVE_LOCATION is the path to the directory where the web page should be copied. The path must exist.
    PAGE_NAME_PREFIX is the text (if any) that will precede the datestamp in the (copied) filename.


            - **Identifier**: `com.github.jazzace.download.abcovid19`

            - **Parent Recipes**: `None`