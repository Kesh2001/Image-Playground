# we want it to run in terminal
# we want the command to be "JPGtoPNGconverter.py Pokedex\ new\"
# it will take all files from pokedex and make a "new" folder where the png versions will b saved
# OpenCV is another advanced library even used in Self Driving cars to process the footage

import os
import sys

from PIL import Image

# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# check if new\ exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through pokedex
# convert to png
# convert to png
# save them to new
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]  # splits the filename from its extension, making a tuple
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print(f'Converted {filename} into png type! ')

