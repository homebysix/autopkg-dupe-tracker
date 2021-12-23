# AbletonLive9Standard.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the most recent version of Ableton Live 9
Standard, and imports it into a Munki repo.

See the download recipe for a description of additional Input options.

The Munki postinstall script used here should perform all the post-install
tasks used by Ableton Live 9 Standard. Note that this script doesn't
seem to be compatible with the Suite edition.


            - **Identifier**: `com.github.timsutton.munki.AbletonLive9Standard`

            - **Parent Recipes**: `com.github.timsutton.download.AbletonLive9`
