from PIL import Image


img = Image.open("pomme.jpg")
largeur_img=750
hauteur_img=500
for y in range(hauteur_img):
    for x in range(largeur_img):
        r, v, b=img.getpixel((x,y))
        if b<100:
            n_b = 255 - b
        else:
            n_b = b

        img.putpixel((x,y),(r,v,n_b))
img.show()

'''
Si la valeur du canal bleu est inférieure à 100,
alors la valeur du canal bleu est mis en négative.
'''