## How to extract file information with Python

**1- Create a file name file_info.py**

**2- Write the python script**

**a- Use `os` module**

    The `os` module in Python offers functions for interacting with the operating system. It is part of Python’s standard utility modules and provides a portable way to access operating system-dependent features. The `os.path` module, a submodule of `os`, is specifically used for common path name manipulations.

**b- initialize an empty list to store the dictionaries that contain the file info**

    fileList = [] 

**c- Iterate through the list of files in the directory**

    Use `os.listdir()` 

**d- Check to validate that file is a regular file**
    
    Use `os.path.isfile(file)` 

**e- Add the file information to the dictionary**

        fileInfo = {'File Name': file, 'size': os.path.getsize(file)} 

**f- Add the file_Info dictionaries to the list**
    
    Use fileList.append()


<img width="658" alt="image" src="https://github.com/user-attachments/assets/43bf164a-7369-431d-8fc6-50a62dfba277">


**3- Create some files for testing**


![image](https://github.com/user-attachments/assets/2549070b-3eb4-491f-bb12-a535e76a6160)


**4- Test and verify results**


![image](https://github.com/user-attachments/assets/2d9892ff-6472-4544-92d8-a1a57a20dd02)


