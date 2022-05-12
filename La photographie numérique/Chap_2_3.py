from PIL import Image


img = Image.open("pomme.jpg")
largeur_img=750
hauteur_img=500
for y in range(largeur_img):
    for x in range(hauteur_img):
        r, v, b=img.getpixel((y,x))
#        n_r=v
#        n_v=b
#        n_b=r
        n_r=b
        n_b=r
        n_v=v

        img.putpixel((y,x),(n_r, n_v, n_b))
img.show()

'''
Ce programme permet de mettre la valeur du canal rouge à la valeur du canal vert,
la valeur du canal vert à la valeur du canal bleu,
et la valeur du canal bleu à la valeur du canal rouge.




'''