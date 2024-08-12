import os

fileList = [] 

for file in os.listdir():
    if os.path.isfile(file):
        fileInfo = {
            'File Name': file, 'size': os.path.getsize(file)
        }

        fileList.append(fileInfo)
print(fileList)