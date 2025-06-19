# ScriptsUserLAnd
Collection of code to be run in userland.

## installation and set up
we presume that the user is using a UserLAnd Debian virtual machine installed on an Android smart phone. 

- clone the repository into the users virtual machine
- run the command `chmod +x setup.sh` to allow you to run the setup script
- run the command `. setup.sh` this will install all the required packages on the users virtual machine. 

## preparing the sample Beamer presentation
This repository comes equipped with a sample beamer presentation. This presentation contains the slides in an ADSC talk about using NLP on my phone.
To save on storage, the images used in the sample beamer presentation are stored in an external google drive and are filtered out using the file `.gitignore`

- run the command `chmod +x prepare_pictures.sh`.
- run the command `./prepare_pictures.sh`, this bash script will
call the python function `google_drive_downloader.py`
which uses the python package `gdown` to download a collection of photos from a public folder on my Google drive.
should the user wish to download images from a different folder on a Google drive, they would need to alter
the `google_drive_downloader.py` file. A good tutorial for using `gdown` can be found  
[here](https://medium.com/@gauravkachariya/download-google-drive-files-on-linux-via-command-line-c0ce06b51dba)
