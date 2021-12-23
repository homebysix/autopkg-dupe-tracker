# KindlePreviewer.download.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: Downloads latest Kindle Previewer disk image.

NOTE: The Kindle Previewer postinstall script (at least as of 2.941) is the following:
####
#!/bin/sh

sudo chmod -R 755 /Applications/Kindle\ Previewer.app
sudo chown -R $USER /Applications/Kindle\ Previewer.app
####

And Kindle Previewer, when running, writes files and directories under:
/Applications/Kindle Previewer.app/Contents/MacOS

Depending on your management system, you may need to address this issue.

            - **Identifier**: `com.github.foigus.download.kindlepreviewer`

            - **Parent Recipes**: `None`
