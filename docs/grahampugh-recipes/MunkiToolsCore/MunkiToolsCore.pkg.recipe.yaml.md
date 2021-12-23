# MunkiToolsCore.pkg.recipe.yaml

            _Last updated 2021-12-23 20:01:51Z_

            - **Description**: Note: munkitools does not include a code signature. If your organization requires code signature, it is recommended to internally sign the application.

Downloads version 3 of the Munki tools via the official releases listing on GitHub. You can set INCLUDE_PRERELEASES to any value to have this recipe pull prerelease versions.

This recipe also extracts the core components, and repackages them for use in Jamf Pro.
Other parts of munkitools are not repackaged.

This recipe cannot be overridden to pull a download from an alternate location such as munkibuilds.org - it will only download the official releases. For this, use the munkitools2-autobuild.munki recipe with a manually-provided DOWNLOAD_URL variable.

The GitHubReleasesInfoProvider processor used by this recipe also respects an input variable: ''sort_by_highest_tag_names'', which, if set, will ignore the post dates of the releases and instead sort descending by tag names according to LooseVersion semantics.


            - **Identifier**: `com.github.grahampugh.recipes.pkg.MunkiToolsCore`

            - **Parent Recipes**: `None`
