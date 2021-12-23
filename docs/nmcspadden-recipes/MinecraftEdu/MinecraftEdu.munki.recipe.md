# MinecraftEdu.munki.recipe

_Last updated 2021-12-23 20:01:49Z_

- **Description**: Packages the latest MinecraftEdu release, and imports it into Munki.  You MUST override the username and password variables or the recipe will fail. If you do not want to put your password in plaintext, you can use a hash of it generated here: http://minecraftedu.com/api/api.php?action=gethash&username=yourusername&password=yourpassword

- **Identifier**: `com.github.nmcspadden.munki.MinecraftEdu`

- **Parent Recipes**: `com.github.nmcspadden.pkg.MinecraftEdu`
