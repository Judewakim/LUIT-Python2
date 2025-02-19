# FOUNDATIONAL
# Create a script that generates a list of dictionaries about files in the working directory. Then print the list.
# Push your code to GitHub and include the link in your write up.

# ADVANCED
# Modify the script into a function such that any path can be passed as a parameter.  This parameter should be optional and should default to working directory when the variable is not passed. The function should then create the list of dictionaries about files from that path. The function should also return information on files nested in folders (recursive).

# COMPLEX (Very Tricky)
# Modify the function to display recursive file information as dictionary of dictionaries.

# imports
import os
import time
import stat

def get_files_info(): # function get_files_info()
    files_info = []  # creates empty list for files
    for filename in os.listdir('.'): # loops through every file (variable named filename) in the listdir() method
        if os.path.isfile(filename): #if its a file. COME BACK AND ADD ELIF THAT IF ITS A DIR TO RECURSE THROUGH IT
            file_stat = os.stat(filename) #stats about each file
            file_info = { 
                #all the data about each file
                'name': filename,
                'size_bytes': file_stat.st_size,
                'last_modified': time.ctime(file_stat.st_mtime),
                'permissions': stat.filemode(file_stat.st_mode),
                'owner': file_stat.st_uid,
                'group': file_stat.st_gid
            }
            files_info.append(file_info) #add the file info for each file into the files_info list
    return files_info #return the list

def print_ll_view(files_info): # function print in 'll' view
    for file in files_info: #for each file in the files_info list
        print(f"{file['permissions']} {file['owner']} {file['group']} {file['size_bytes']} {file['last_modified']} {file['name']}") # what gets printed to screen

#functions get called in main.py