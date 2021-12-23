# Outlook2016Updates-fr_FR.munki.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest Outlook 2016 multilingual update pkg,
appends the version to the end of the filename, and imports into
Munki.

If this is an update_for something, you may define this in your
pkginfo Input override below.

LOCALE_ID sets the locale for a descriptive text that will be
extracted from the Microsoft update metadata. See
https://msdn.microsoft.com/en-us/goglobal/bb964664.aspx
for more information about locale IDs.

VERSION supports two values: 'latest', and 'latest-delta', defaulting to
'latest'. If 'latest-delta' is selected, the delta update will be selected
instead of the full update.

If 'latest-delta' is selected, the pkginfo's installs item that's generated
will also include a 'minimum_update_version' set, declaring a minimum app
version to which this delta can be applied. It will also have a 'requires'
item set to this minimum update version, whose name can be set explicitly
with 'munki_required_update_name'. If left blank, NAME will be used.

PLEASE NOTE: This recipe doesn't currently support a workflow where _both_
full and delta updates can be imported and clients will automatically select
only the correct update. It only tries to add as much "safety" as possible
when importing a delta update. Choosing to import delta updates will likely
require additional work on the part of the admin (for example, using an
installcheck_script).

            - **Identifier**: `com.github.ygini.munki.MSOutlook2016Updates-fr_FR`

            - **Parent Recipes**: `com.github.autopkg.munki.MSOutlook2016`
