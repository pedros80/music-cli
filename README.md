# Music CLI

Some python scripts used for stuff that happens regular-ish that I my need again... 

## GMan
Finds all the youtube downloads recursively in a directory, converts to mp3 and adds to a subdirectory. Meant to be used with [JDownloader 2](http://jdownloader.org/jdownloader2 "JDownloader 2") and a list of videos; although any process which gets the videos in mp4 to you machine'll do...

* Find all the videos
* Queue downloads
* When downloads are finished, run GMan on downloads directory, specifying output directory
* Copy output directory to wherever...

Uses `ffmpeg` to do the conversion.

Requires python3

## SampleSwapUnzipper
Finds all the zip files from [SampleSwap](https://sampleswap.org/index.php "SampleSwap") recursively in a directory and uznips the sound files contained therein to your directory of samples...

* Fill your SampleSwap basket
* Download file
* Repeat until bored
* Run SampleSwapUnzipper
* Use downloaded samples in hit music...

Need to replace your SampleSwap username (the prefix for the downloaded zip file) and any paths.

Requres python3