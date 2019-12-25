from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# filtered_img = img.filter(ImageFilter.SMOOTH)

#L turns it black and white.
filtered_img = img.convert('L') 
# 
# filtered_img.save("grey.png",'png')

#Resizes an image 
#.resize can be used but it kills the aspect ratio. 
#.thumbnail keeps the aspect ratio.
# img.thumbnail((400,200))

box = (100,100,400,400)
region = filtered_img.crop(box)
region.save('cropped.jpg') 
# resize = filtered_img.resize((300,300))
# resize.save('resize.png','png')

# crooked = filtered_img.rotate(180)
# crooked.save("thumbnail.jpg")

# filtered_img.show()