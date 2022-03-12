"""Running this file repeatedly wont save the image again and again!!!"""
from PIL import Image, ImageFilter
# read the docs for every lib that u install

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)  # use .SMOOTH to smoothen and .SHARPEN to sharpen
print(img)
print(img.format)
print(img.size)
print(img.mode)
crooked = filtered_img.rotate(90)  # angle
crooked.save('Turned.png', 'png')
filtered_img.save("blur.png", 'png')  # we changed it to png as unlike jpeg it supports filters
# .save(new_name, extension)
"""filtered_img = img.convert('L')
   filtered_img.save('grey.png','png')
will make the pikachu grey!!!!!!!"""
# filtered_img.show() opens and actually shows the image! not the object, the actual image
small = filtered_img.resize((300, 300))  # accepts a tuple
small.save('small.png', 'png')
# But if u wanna crop:
box = (100, 100, 400, 400)  # pixels
region = filtered_img.crop(box)
region.save('cropped.png', 'png')  # cropped to only the face
img2 = Image.open('./astro.jpg')
print(img2.size)
img2.thumbnail((400, 200))  # resizes the image while retaining the aspect ratio of it
# also intelligently decides the right size
img2.save('Thumbnail.png', 'png')
print(img2.size)
