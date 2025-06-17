import gdown

# a folder
url = "https://drive.google.com/drive/folders/1MQGki3KUXYeesGTrDSZhTrPNmDDYal75"
gdown.download_folder(url)

# same as the above, but with the folder ID
id = "1MQGki3KUXYeesGTrDSZhTrPNmDDYal75"
gdown.download_folder(id=id)

