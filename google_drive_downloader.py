import gdown
import os 

"""
# a folder
url = "https://drive.google.com/drive/folders/1MQGki3KUXYeesGTrDSZhTrPNmDDYal75"
gdown.download_folder(url)
"""

# downloads a folder  with the folder ID

# default id of one of my google folders
default_id = "1MQGki3KUXYeesGTrDSZhTrPNmDDYal75"

def get_folder_name(id = default_id):
    gdown.download_folder(id=id, output = 'Public_images', quiet=False)
    return 

if __name__ == "__main__":
    get_folder_name()
