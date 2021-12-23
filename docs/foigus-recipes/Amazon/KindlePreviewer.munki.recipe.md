# KindlePreviewer.munki.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads latest Kindle Previewer disk image and imports it into Munki.

NOTE: The Kindle Previewer postinstall script (at least as of 2.941) is the following:
####
#!/bin/sh

sudo chmod -R 755 /Applications/Kindle\ Previewer.app
sudo chown -R $USER /Applications/Kindle\ Previewer.app
####

And Kindle Previewer, when running, writes files and directories under:
/Applications/Kindle Previewer.app/Contents/MacOS

You will need to address this issue before Kindle Previewer will work correctly.

            - **Identifier**: `com.github.foigus.munki.kindlepreviewer`

            - **Parent Recipes**: `com.github.foigus.download.kindlepreviewer`