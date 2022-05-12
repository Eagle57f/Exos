from PIL import Image


img = Image.open("pomme.jpg")
img.putpixel((575,250),(0, 0, 255))
img.show()