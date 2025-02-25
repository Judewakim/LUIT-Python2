# FOUNDATIONAL
# Create a script that generates a list of dictionaries about files in the working directory. Then print the list.
# Push your code to GitHub and include the link in your write up.

# ADVANCED
# Modify the script into a function such that any path can be passed as a parameter.  This parameter should be optional and should default to working directory when the variable is not passed. The function should then create the list of dictionaries about files from that path. The function should also return information on files nested in folders (recursive).

# COMPLEX (Very Tricky)
# Modify the function to display recursive file information as dictionary of dictionaries.

import os
import time

def get_files_info(path='.'):  # Function that collects file details, defaulting to current directory
    files_info = []  # List to store file details
    
    for root, _, files in os.walk(path):  # Recursively traverse directories and files
        for filename in files:
            file_path = os.path.join(root, filename)  # Construct the full file path
            file_stat = os.stat(file_path)  # Get file details/statistics
            
            files_info.append({  # Store file details in a dictionary
                'name': filename,  # File name
                'path': file_path,  # Full file path
                'size_bytes': file_stat.st_size,  # File size in bytes
                'last_modified': time.ctime(file_stat.st_mtime),  # Last modified time
                'permissions': oct(file_stat.st_mode)[-3:],  # File permissions in octal format (last 3 digits)
            })
    
    return files_info  # Return the list of file details

def print_ll_view(files_info):  # Function to print file details in 'll' view format
    for file in files_info:  # Loop through the list of file dictionaries
        print(f"{file['permissions']} {file['size_bytes']} {file['last_modified']} {file['path']}")  # Print file details

if __name__ == "__main__":  # Run the script only if executed directly
    path = input("Enter the directory path (press Enter to use current directory): ") or "."  # Prompt user for path, default to current directory
    files_data = get_files_info(path)  # Get file details for the specified path
    print("\nLinux CLI 'll' View:")  # Print header
    print_ll_view(files_data)  # Display file details
