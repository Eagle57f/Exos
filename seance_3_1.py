from tkinter import *
fen1 = Tk()
fen1.title("Exemple d’interface graphique")
fen1.geometry('500x200')
tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
tex1.pack()
bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
bou1.pack()
fen1.mainloop()

# .title sert à donner un titre a l'application (affiché tout en haut a gauche dans la barre au dessus de l app)
# .geometry sert a donner la taille en px de notre application
# fen1 est le nom donné a notre application (nom utlisé pour le code)
# .Label sert a créer une zone de texte
# text sert a definir le text affiché et fg la couleur du texte
# En supprimant tex1.pack(), le texte n'est plus affiché
# .pack() sert donc a placer un objet dans l'IG
# .Button sert a gréer un bouton
# fen1 sert a dire que c'est dans l'IG fen1, text sert a donner le texte dans le boutton, command sert a donner l'action a effectuer apres appui
# destroy va fermer l'IG
# 
# 
#  