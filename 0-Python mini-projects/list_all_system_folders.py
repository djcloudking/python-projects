# list all the files in a list of folders that the user provides

import os

folders = input("Please provide the list of folders names with spaces between:").split() 

for folder in folders:
    files = os.listdir(folder)
    print("=================== listing files for the folder -" + folder)
  