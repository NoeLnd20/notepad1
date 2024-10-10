from tkinter import *
from tkinter import filedialog, colorchooser
from tkmacosx import *


#texte.config(font=(style_actuelle,taille_actuelle, police_actuelle))


#Création de la page
root = Tk()
root.geometry("500x500")
root.title("NotePad")
texte = Text(root)
texte.pack(expand=YES, fill="both")

police_actuelle = "Arial"
taille_actuelle = 12
style_actuelle = "normal"
#Création des fichiers

def ouvrir_fichier():
    fichier = filedialog.askopenfilename(title="Ouvrir un fichier", defaultextension="*.txt", filetypes=[("Tous les fichiers", "*.txt")])
    if fichier:
        with open(fichier, "r") as f:
            texte.delete(1.0, END)
            texte.insert(END, f.read())
            root.title(f"NotePad : {fichier}")

def enregistrer_fichier():
    fichier = filedialog.asksaveasfilename(title="Enregistrer un fichier", defaultextension="*.txt", filetypes=[("Tous les fichiers", "*.txt")])
    if fichier:
        with open(fichier, "w") as f:
            contenu = texte.get(1.0, END)
            f.write(contenu)
def quitter_application():
    root.quit()
menu_bar = Menu(root)
menu_fichier = Menu(menu_bar)
menu_bar.add_cascade(label="Fichier", menu=menu_fichier)
menu_fichier.add_command(label="Ouvrir", command=ouvrir_fichier)
menu_fichier.add_command(label="Enregistrer", command=enregistrer_fichier)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=quitter_application)

#Création Couleur
def couleur_fond():
    couleur = colorchooser.askcolor()
    texte.configure(bg=couleur[1])
def couleur_texte():
    couleur = colorchooser.askcolor()
    texte.configure(fg=couleur[1])

menu_couleur = Menu(menu_bar)
menu_bar.add_cascade(label="Couleurs", menu=menu_couleur)
menu_couleur.add_command(label="Couleur du fond", command=couleur_fond)
menu_couleur.add_command(label="Couleur du texte", command= couleur_texte)


#Création style
def appliquer_tag(style): 
    texte.tag_remove("gras", "sel.first", "sel.last")
    texte.tag_remove("italique", "sel.first", "sel.last")

    if style == "gras":
        texte.tag_add("gras", "sel.first", "sel.last")
    elif style == "italique":
        texte.tag_add("gras", "sel.first", "sel.last")
    elif style == "italique_gras":
        texte.tag_add("gras", "sel.first", "sel.last")
        texte.tag_add("gras", "sel.first", "sel.last")

    texte.tag_configure("gras", font=(police_actuelle, taille_actuelle, "bold"))
    texte.tag_configure("italique", font=(police_actuelle, taille_actuelle, "italic"))

def normal_style():
    texte.tag_remove("gras", "sel.first", "sel.last")
    texte.tag_remove("italique", "sel.first", "sel.last")
    
def italique_style():
    appliquer_tag("italique")

def gras_style():
    appliquer_tag("gras")

def gras_italique_style():
    appliquer_tag("italique_gras")

menu_style = Menu(menu_bar)
menu_bar.add_cascade(label="Style", menu=menu_style)
menu_style.add_command(label="Normal", command=normal_style)
menu_style.add_command(label="Gras", command=gras_style)
menu_style.add_command(label="Italique", command=italique_style)
menu_style.add_command(label="Gras et Italique", command=gras_italique_style)



#Les polices
def helvetica():
    global police_actuelle
    police_actuelle = "helvetica"
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def arial():
    global police_actuelle
    police_actuelle = "arial"
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def inter():
    global police_actuelle
    police_actuelle = "inter"
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def avenir():
    global police_actuelle
    police_actuelle = "avenir"
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def roboto():
    global police_actuelle
    police_actuelle = "Roboto"
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def raleway():
    global police_actuelle
    police_actuelle = "raleway"
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def futura():
    global police_actuelle
    police_actuelle = "futura"
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
menu_police = Menu(menu_bar)
menu_bar.add_cascade(label="Police", menu=menu_police)
menu_police.add_command(label="Helvetica", command=helvetica)
menu_police.add_command(label="Futura", command=futura)
menu_police.add_command(label="Inter", command=inter)
menu_police.add_command(label="Avenir", command=avenir)
menu_police.add_command(label="Roboto", command=roboto)
menu_police.add_command(label="Raleway", command=raleway)
menu_police.add_separator()
menu_police.add_command(label="Arial", command=arial)


#Less tailles
def h1():
    global taille_actuelle
    taille_actuelle = 32
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def h2():
    global taille_actuelle
    taille_actuelle = 24
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def h3():
    global taille_actuelle
    taille_actuelle = 18
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def h4():
    global taille_actuelle
    taille_actuelle = 16
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def h5():
    global taille_actuelle
    taille_actuelle = 14
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def h6():
    global taille_actuelle
    taille_actuelle = 12
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
def paragraphe():
    global taille_actuelle
    taille_actuelle = 16
    texte.configure(font=(police_actuelle, taille_actuelle, style_actuelle))
menu_taille = Menu(menu_bar)
menu_bar.add_cascade(label="Taille", menu=menu_taille)
menu_taille.add_command(label="H1", command=h1)
menu_taille.add_command(label="H2", command=h2)
menu_taille.add_command(label="H3", command=h3)
menu_taille.add_command(label="h4", command=h4)
menu_taille.add_command(label="H5", command=h5)
menu_taille.add_command(label="H6", command=h6)
menu_taille.add_separator()
menu_taille.add_command(label="Paragraphe", command=paragraphe)

root.config(menu=menu_bar)


















root.mainloop()