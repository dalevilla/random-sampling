# Random Sampling
A random sampling script. Move n random files from the lowest subdirectories of a source location to the destination directory. Folders for each label are also created in the dest directory.

# Usage
Download the file **rand_sample.py**, run in the terminal using the example below

```
python rand_sample.py "D:\\SOURCE PATH" "D:\\DESTINATION PATH" 15

```

which will copy 15 files from all subdirectories in the source path. More options are available using ```--help```.

## Exclude

An exclude option is included to remove some folders from being sampled. To use exclude, the user should put ```-e``` or ```--exclude``` for every folder to be excluded. For example, using the sample directory below

>topdir
  >subdir1
  >subdir2
  >subdir3
  >subdir4
  
to exclude subdir2 and subdir3, the user would have to add the following options below

```
-e subdir2 -e subdir3
```

# License

The script is licensed using MIT License.
