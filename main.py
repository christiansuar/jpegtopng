import os
from PIL import Image

input_folder = input("enter input folder: (path directory) ").strip().strip('"')
if not os.path.exists(input_folder):
    print("Input folder does not exist.")
    exit()

output_folder = input("enter output folder: (path directory) ").strip().strip('"')
if not os.path.exists(output_folder):
    # if dont exist create it under the input folder
    os.makedirs(output_folder)

    print(f"Output folder created: {output_folder}")


for file in os.listdir(input_folder):
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".png") 
        with Image.open(input_path) as img:
            img.save(output_path, "PNG")
                    