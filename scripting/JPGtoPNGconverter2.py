import sys 
import os 
from PIL import Image 


# Grab first and second arguements.
# Pokedex/(Folder with files to convert) new/(new Folder).
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# If the folder doesn't exists in the 
# root directory then make the new folder.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
counter = 1   
# Loop  though the files in the image folder     
for file_name in os.listdir(image_folder):
    
    # If the files have '.jpg' the we can access them.
    if file_name.find('.jpg') != -1:
        # Create image object. 
        img  = Image.open(f'{image_folder}{file_name}')
        
        # Gets the name of the file without the .ending.(.jpg)
        clean_name = os.path.splitext(file_name)[0]
        
        #saves the image as .png in the new folder.
        img.save(f'{output_folder}{clean_name}.png','png')
        
        print(f"File number {counter} done!")
        counter += 1
