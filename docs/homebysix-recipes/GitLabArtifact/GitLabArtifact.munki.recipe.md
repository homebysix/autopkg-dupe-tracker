# GitLabArtifact.munki.recipe

_Last updated 2021-12-23 19:58:08Z_

- **Description**: Download the latest CI/CD job artifact from the specified GitLab repository, and imports the pkg file at the artifact path into Munki. Can be used to automatically import MunkiPkg installer files built by CI/CD, for example. See the README.md file for details on using this recipe.

- **Identifier**: `com.github.homebysix.munki.GitLabArtifact`

- **Parent Recipes**: `com.github.homebysix.download.GitLabArtifact`