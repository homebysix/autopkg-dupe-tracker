# DCPomatic2.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest DCP-o-matic from the official DCP-o-matic
website, and imports it into Munki.

By default this recipe will download the stable, "main" DCP-o-matic app,
but the download can be changed to one of the other options by changing APP
to any of the following:
Batch Converter, DCP-o-matic, Encode Server, KDM Creator

If you wish to download multiple products then one can make multiple
overrides from this one recipe. One would then typically modify
NAME and pkginfo keys appropriately.

CHANNEL can be either 'stable' or 'test'


            - **Identifier**: `com.github.timsutton.munki.DCPomatic2`

            - **Parent Recipes**: `com.github.timsutton.download.DCPomatic2`
