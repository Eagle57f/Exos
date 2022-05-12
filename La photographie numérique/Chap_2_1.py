from PIL import Image


img = Image.open("pomme.jpg")
r, v, b=img.getpixel((250,300))
print(f"Canal rouge:{r} , canal vert:{v} , canal bleu:{b}")


'''
Exercice 1
1) Canal rouge:104 , canal vert:112 , canal bleu:29


'''