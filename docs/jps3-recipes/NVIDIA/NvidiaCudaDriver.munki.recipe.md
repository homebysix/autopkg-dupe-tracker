# NvidiaCudaDriver.munki.recipe

_Last updated 2021-12-23 20:01:50Z_

- **Description**: Downloads the latest NVIDIA CUDA driver for Mac from the NVDIA web site, and imports into Munki repo. PLEASE NOTE: This package, while recommended by some vendors, such as Adobe for After Effects, is not signed. Neither is any of the software being installed, which is mostly system-level (ex. kexts or Extensions, Frameworks, and libraries). The installer pkg is also served over HTTP. It is pretty much a trifecta of security fail. But... for many situations until NVIDIA fixes this, it is all we have to work with. (Name 'em and shame 'em!)

- **Identifier**: `com.github.jps3.munki.NvidiaCudaDriver`

- **Parent Recipes**: `com.github.jps3.download.NvidiaCudaDriver`
