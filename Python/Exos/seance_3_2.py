from tkinter import *
from random import randrange
def drawline():
    global x1, y1, x2, y2, coul
    can1.create_oval(x1,y1,x2,y2,width=2,fill=coul)
    y2, y1 = y2+10, y1-10
def changecolor():
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8)
    print(c)
    coul = pal[c]
    print(coul)
x1, y1, x2, y2 = 10, 190, 190, 10
coul = 'dark green'
fen1 = Tk()
can1 = Canvas(fen1,bg='darkgrey',height=200,width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.destroy)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
fen1.mainloop()

# .Canvas sert a créer un emplacement de dessin
# Le Canvas passe a droite
# Une ligne est dessinée dans le Canvas, la fonction drawline() est utilisée
# create_line sert a dessiner une ligne
# x1 et x2 sont les coos d'un premier point de la droite et x2, y2 sert a donner un deuxieme point, le tout pour orienter en placer la droite, width sert a donner ma largeur de la droite, fill sert a donner la couleur de la droite
# change les coordonnées de la droite (la fait tourner dans ce porgramme) on pourrait l'écrire y2 += 10 et y1 -= 10
# Les prochaines droites dessinéees ont une couleur aléatoire. La fonction utilisée est changecolor()
#  type(pal) = list
# randrange() sert a choisir un nombre au hasard; (ici entre 0 et 7)
# il ne fonctionnera plus car global sert a dire au programme que la variable est globale, donc utilisable meme dans la fonction car les var on été definie en dehors de la fonction.
# Il faut supprimer "green" dans la liste et changer randrange(8) par randrange(7)
# Le programme affiche dans le terminal le nombre aléatoire entre 0 et 8 choisi et son coorespondant dans la liste.
# y2, y1 = y2+10, y1+10 et x1, y1, x2, y2 = 10, 10, 190, 10
# Le programme dessine des rectangles au lieu de lignes
# Le programme dessiner des ovals au lieu de lignes (ou rectangles). Pour create.rectangle, les coordonnées donnent les coos de deux points opposés. Pour le create_oval les coos sont ceux d'un rectangle invisible dans lequel l'ovale touche sur tout les bords du rectangle
