from PIL import Image


img = Image.open("pomme.jpg")
largeur_img=750
hauteur_img=500
for y in range(hauteur_img):
    for x in range(largeur_img):
        r, v, b=img.getpixel((x,y))
        if v>10 and y>250:
            n_v=0
        else:
            n_v = 255

        img.putpixel((x,y),(r,b, n_v))
img.show()

'''
Si la valeur du canal vert est supérieure à 10 et que la valeur de la coordonnée y est supérieure à 250,
alors la valeur du canal vert est mis à 0, sinon la valeur du canal vert est mis à 255.
'''