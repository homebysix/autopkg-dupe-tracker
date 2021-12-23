# IzPackExecutor.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: This is a stub recipe for IzPackExecutor Processor.

This Processor can be used by another
recipe outside of this directory or repo by referring to
the Processor in this directory.

Instead of setting the 'Processor' key to a processor name
only, one should separate the recipe identifier and the processor
name with a slash:

<dict>
    <key>Processor</key>
    <string>com.github.bnpl.autopkg.proc.IzPackExecutor/IzPackExecutor</string>
</dict>

..assuming that this recipe is in one of AutoPkg's search dirs.


            - **Identifier**: `com.github.bnpl.autopkg.proc.IzPackExecutor`

            - **Parent Recipes**: `None`
