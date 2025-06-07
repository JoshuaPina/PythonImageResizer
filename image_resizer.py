#The image I created is too large for Github...I will use PIL to resize it for Github.and

from PIL import Image

#Opening the image after moving it to the correct directory
img = Image.open("/Users/joshuapina/Downloads/my_soldiers_rage.png")

#Resizing the image. I tried 70%, 45%, and finally 30% of the original size.
#This represents the 3 different versions of the resized image

img = img.resize((int(img.width * 0.3), int(img.height * 0.3)))

#Converting and saving image to a smaller quality and different format
img.convert('RGB').save("resized_image3.jpg", "JPEG", optimize=True, quality=70)
