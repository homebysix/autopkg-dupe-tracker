# OutsetPayloadPkgReqd.pkg.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Takes the file specified by the --pkg (or -p) run option and builds a package
that will install the file to /usr/local/outset/%ACTION_TYPE%.

This recipe requires the robperc-recipes and homebysix-recipes repos.

The pkg will be named using the payload's file name (up to the first period) 
with underscores and spaces removed.

This recipe assumes the item being passed (like a script) may not have a version number,
so it assigns an ever-increasing number (based on the current time) as the version number.

Suggested Usage:
1.  Make an override for each type of Outset folder you wish to target. Name the override
    to match the target folder — for example: 
        autopkg make-override OutsetPayloadPkgReqd.pkg -n Outset-login-once.pkg
2.  Change the value of ACTION_TYPE to match the target folder for that override.
3.  Run the override with the --pkg option — for example:
        autopkg run Outset-login-once.pkg --pkg /path/to/payload

Input Variables:
The legal values for ACTION_TYPE are the same as the folders within Outset's structure:
	boot-every
	boot-once
	login-every
	login-once
	login-privileged-every
	login-privileged-once
	on-demand

REVERSE_DOMAIN specifies what you would like the package identifier to begin with
(it will be followed by a "." and the name of your payload file including extension).
It is recommended that you change this value in your override to match your organization.


            - **Identifier**: `com.github.jazzace.pkg.OutsetPayloadPkgReqd`

            - **Parent Recipes**: `None`
