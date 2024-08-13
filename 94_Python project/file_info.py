import os

# initialize an empty list to store the dictionaries that contain the file info
fileList = [] 

for file in os.listdir(): # Iterate through the list of files in the directory
    if os.path.isfile(file): # check to validate that file is a regular file
        fileInfo = {
            'File Name': file, 'size': os.path.getsize(file)
        } # add the file information to the dictionary

        fileList.append(fileInfo) # add the file_Info dictionaries to the list
print(fileList)