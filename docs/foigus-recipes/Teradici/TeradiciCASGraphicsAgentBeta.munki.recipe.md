# TeradiciCASGraphicsAgentBeta.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the latest version of Teradici CAS PCoIP Graphics Agent Beta and imports it into Munki.

NOTES:
"PCoIP Agent.app" agent needs the following PPPC rights:
- Accessibility
- Screen Recording
Remember Screen Recording must be allowed by hand.

The installation instructions: 
https://www.teradici.com/web-help/pcoip_agent/graphics_agent/macos/21.07/admin-guide/installing/installing-macos/
say the initial installation requires a restart (presumably following the allowance of PPPC rights).

The upgrade instructions:
https://www.teradici.com/web-help/pcoip_agent/graphics_agent/macos/21.07/admin-guide/installing/updating-macos/
indicate a restart is not necessary.

To account for this difference, this recipe does NOT require a restart but can be overridden with RestartAction values noted in the Munki Wiki:
https://github.com/munki/munki/wiki/Supported-Pkginfo-Keys
It is assumed the common case is the admin restarting the computer following the hand-approval of Screen Recording PPPC rights.

The default state of this recipe (FORCE_MUNKIIMPORT is set (thus true) and STOP_ON_NO_NEW_DOWNLOAD is true) should behave properly for most use cases (e.g. automated runs).  The force_munkiimport is needed because (currently) every Graphics Agent Beta package has a receipt of "com.teradici.pcoip-agent.Unspecified" with version 1.10.0.  This has been reported to Teradici under case 00049483.

            - **Identifier**: `com.github.foigus.munki.TeradiciCASGraphicsAgentBeta`

            - **Parent Recipes**: `com.github.foigus.download.TeradiciCASGraphicsAgentBeta`