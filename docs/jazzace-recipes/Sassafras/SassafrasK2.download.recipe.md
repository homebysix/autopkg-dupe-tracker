# SassafrasK2.download.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Fetches the latest Sassafras K2 Mac installer for versions 7.0-7.6 specified by PRODUCT.

For versions 7.7 and later, use the new SassafrasClient/Admin/Server recipes.

REVISION is the major version without a decimal, for example:
7.0: 70
7.1: 71
7.2: 72
7.5: 75

This recipe supports only a REVISION of 70 through 76. If REVISION
is set to an empty string, the 7.6 version will be retrieved.

PRODUCT must be one of the following:
Admin
Server
Client

If you want to download more than one (e.g., both Admin and Server),
make an override for each and specify a unique identifier using the -n option
(e.g., autopkg make-override SassafrasK2.download -n SassafrasK2Server.download).



            - **Identifier**: `com.github.jazzace.download.sassafrasK2product`

            - **Parent Recipes**: `None`