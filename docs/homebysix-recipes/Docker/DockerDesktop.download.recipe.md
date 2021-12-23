# DockerDesktop.download.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads the latest version of Docker Desktop.

Acceptable values for PLATFORM_ARCH include:
- 'amd64': Downloads the Intel version of Docker. (This is the default.)
- 'arm64': Downloads the Apple Silicon version of Docker.

NOTE: The Intel build does not function with Rosetta2, so separate packaging is
required to support Apple Silicon Macs.

            - **Identifier**: `com.github.homebysix.download.DockerDesktop`

            - **Parent Recipes**: `None`


## Warnings

- These recipes have duplicate NAMEs:
    - [chilcote-recipes/Docker/Docker.download.recipe](/autopkg-dupe-tracker/chilcote-recipes/Docker/Docker.download.recipe)
    - [fishd72-recipes/DockerEdge/DockerEdge.download.recipe](/autopkg-dupe-tracker/fishd72-recipes/DockerEdge/DockerEdge.download.recipe)
    - [moofit-recipes/Docker/DockerUniversal.download.recipe](/autopkg-dupe-tracker/moofit-recipes/Docker/DockerUniversal.download.recipe)
    - [homebysix-recipes/Docker/DockerDesktop.download.recipe](/autopkg-dupe-tracker/homebysix-recipes/Docker/DockerDesktop.download.recipe)
    - [smithjw-recipes/Docker/Docker.download.recipe.yaml](/autopkg-dupe-tracker/smithjw-recipes/Docker/Docker.download.recipe.yaml)