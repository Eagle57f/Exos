from PIL import Image


img = Image.open("pomme.jpg")
largeur_img=750
hauteur_img=500
for y in range(largeur_img):
    for x in range(hauteur_img):
        r, v, b=img.getpixel((y,x))
        n_r=255-r
        n_b=255-b
        n_v=255-v

        img.putpixel((y,x),(n_r, n_v, n_b))
img.show()