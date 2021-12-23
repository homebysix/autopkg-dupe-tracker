# SampleSharedProcessor.recipe

            _Last updated 2021-12-23 20:01:50Z_

            - **Description**: This is an example of a recipe that can be used by another
recipe outside of this directory or repo, to refer to
a processor in this directory.

Instead of setting the 'Processor' key to a processor name
only, we separate the recipe identifier and the processor
name with a slash:

<dict>
    <key>Processor</key>
    <string>com.github.autopkg.recipes.SampleSharedProcessor/SampleSharedProcessor</string>
</dict>

..assuming that this recipe is in one of AutoPkg's search dirs.


            - **Identifier**: `com.github.autopkg.recipes.SampleSharedProcessor`

            - **Parent Recipes**: `None`
