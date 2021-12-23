# PantoneColorManager.download.recipe

        _Last updated 2021-12-23 19:58:07Z_

        - **Description**: 
Download the current release of Pantone Color Manager

You will still need to activate PCM with your PANTONE registration.
Either by registering your PANTONE color guide or buy purchasing an application license separately.

If you don't have X-Rite Device Services installed, this package will also install that to support calibration
via spectrophotometer.

2015-12-22: Added Static URL to override Sparkle URL because pantone have let the certificate expire on pcm.pantone.com
2019-02-15: Re-introducing SparkleUpdateInfoProvider because certificate is back in working order, and now points directly to a dmg, which simplifies the Munki recipe



        - **Identifier**: `com.github.mosen.download.PantoneColorManager`

        - **Parent Recipes**: `None`