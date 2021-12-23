# AppStoreApp.munki.recipe

_Last updated 2021-12-23 19:58:07Z_

- **Description**: Checks for the update of a MAS app.  If the version on disk is up to date, then import into Munki directly.  If out of date, abort. This recipe MUST ONLY be used with an override - do not run this recipe directly. See the documentation here: https://github.com/autopkg/nmcspadden-recipes/#appstoreapp-recipe

- **Identifier**: `com.github.nmcspadden.munki.appstore`

- **Parent Recipes**: `None`