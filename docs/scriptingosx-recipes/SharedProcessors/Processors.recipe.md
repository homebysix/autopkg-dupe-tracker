# Processors.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Stub Recipe to locate the shared processors in this folder. 

To use the processors here, instead of setting the 'Processor' key to a processor name
only, we separate the recipe identifier and the processor
name with a slash:

<dict>
    <key>Processor</key>
    <string>com.github.scriptingosx.SharedProcessors/ProcessorName</string>
</dict>

Currently ScriptingOSX has the following shared processors:
- Notification: shows a OS X notification (Sample: XQuartz/XQuartz.notify.recipe)
- SendPKGWithARD: uses ARD to send and install a pkg to a given computer list in Apple Remote Desktop
- FileTemplate: copies a template file and fills placeholders with autopkg key (e.g. %NAME%, %version%) (used in FirefoxUSC.pkg)


            - **Identifier**: `com.scriptingosx.processors`

            - **Parent Recipes**: `None`

## Warnings

- These recipes have duplicate filenames:
    - [scriptingosx-recipes/SharedProcessors/Processors.recipe](/autopkg-dupe-tracker/scriptingosx-recipes/SharedProcessors/Processors.recipe)
    - [robperc-recipes/Processors/Processors.recipe](/autopkg-dupe-tracker/robperc-recipes/Processors/Processors.recipe)
    - [moofit-recipes/Processors/Processors.recipe](/autopkg-dupe-tracker/moofit-recipes/Processors/Processors.recipe)

- These recipes have duplicate filenames, ignoring numbers:
    - [scriptingosx-recipes/SharedProcessors/Processors.recipe](/autopkg-dupe-tracker/scriptingosx-recipes/SharedProcessors/Processors.recipe)
    - [robperc-recipes/Processors/Processors.recipe](/autopkg-dupe-tracker/robperc-recipes/Processors/Processors.recipe)
    - [moofit-recipes/Processors/Processors.recipe](/autopkg-dupe-tracker/moofit-recipes/Processors/Processors.recipe)