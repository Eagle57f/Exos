from PIL import Image


img = Image.open("pomme.jpg")
largeur_img=750
hauteur_img=500
for y in range(largeur_img):
    for x in range(hauteur_img):
        r, v, b=img.getpixel((y,x))
        l=int((r+v+b)/3)

        img.putpixel((y,x),(l, l, l))
img.show()