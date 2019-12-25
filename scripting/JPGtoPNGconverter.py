import sys 
import os 
from PIL import Image

# Gets the name of the root new root diectory.
def get_root_name():
    root = input("What folder are you trying to access? ")
    return root


# Gets the new folder name from the user.
def get_newfolder_name():
    new_folder_name = input("Name of folder converted files will be stored. ")
    return new_folder_name 


# Returns true if a file is not in JPEG format
# and false if it is not.
def is_jpg(filename):
    try:
        image = Image.open(filename)
        return image.format =='JPEG'
    except IOError:
        return False
    
    
# Creates a new  directory with the  folder name
# and current root name 
def create_directory(current_path):
    if not os.path.exists(current_path):
        os.makedirs(f'./{root}/{new_folder_name}')


# Saves converted  files into the new directory.
def save_files(entries):
    for entry in entries:
        file_name = f'./{root}/{entry.name}'
        if is_jpg(file_name):
            
            name = str(entry.name)
            
            edited_name = name.replace('.jpg','.png')
            
            img = Image.open(file_name)
            
            new_name = f'./{root}/{new_folder_name}/{edited_name}'
            
            img.save(new_name,'png')
    
        
        
#Gets the main(root) directory name from the user.
root = get_root_name()

#Gets the new folder name from the user.
new_folder_name = get_newfolder_name()


current_path = f'./{root}/{new_folder_name}'

# Scans all files in a directory 
# and stores them in entries

with os.scandir(f'./{root}') as entries:
    
    # Creates a new directory based on the current path
    # and the directory name given.
    create_directory(current_path)
    
    # Saves all the converted files in
    # the directory that was created
    save_files(entries)

                
            
        



