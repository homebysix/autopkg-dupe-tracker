# RelaySmartAgentKextlessCA.pkg.recipe

        _Last updated 2021-12-23 20:01:50Z_

        - **Description**: Repackage the DMG installer Lightspeed, exclude MobileFilterKext
and include certificate material. The user must specify the path to the a folder containing
SmartAgent.dmg, ca_key.pem, ca.pem, localhost_key.pem, and localhost.pem. At runtime specify
the path via the `--key RELAY_DIR="/path/to/folder/"` option.

        - **Identifier**: `com.github.nstrauss.pkg.RelaySmartAgentKextlessCA`

        - **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate NAMEs:
    - [nstrauss-recipes/Lightspeed Relay/RelaySmartAgentKextlessCA.pkg.recipe](/autopkg-dupe-tracker/nstrauss-recipes/Lightspeed Relay/RelaySmartAgentKextlessCA.pkg.recipe)
    - [nstrauss-recipes/Lightspeed Relay/RelaySmartAgentKextless.pkg.recipe](/autopkg-dupe-tracker/nstrauss-recipes/Lightspeed Relay/RelaySmartAgentKextless.pkg.recipe)
    - [nstrauss-recipes/Lightspeed Relay/RelaySmartAgent.pkg.recipe](/autopkg-dupe-tracker/nstrauss-recipes/Lightspeed Relay/RelaySmartAgent.pkg.recipe)