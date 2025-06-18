import gdown
import os 

"""
# a folder
url = "https://drive.google.com/drive/folders/1MQGki3KUXYeesGTrDSZhTrPNmDDYal75"
gdown.download_folder(url)
"""

# downloads a folder  with the folder ID

def get_folder_name(id):
    """
    """
    name = gdown.download_folder(id=id, quiet=False)
    return name 
    
id = "1MQGki3KUXYeesGTrDSZhTrPNmDDYal75"
print(get_folder_name(id))
print(os.getcwd())
