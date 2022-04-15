# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:41:04 2022

@author: thiba
"""

#--------------------------------------------------------------------------------------
#                                    Imports
#--------------------------------------------------------------------------------------

import csv
import re
import numpy as np
from scipy import spatial

import csv
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as tkfont

#------------------------------------Models--------------------------------------------


from gensim.models import Word2Vec

model = Word2Vec.load("Movie_Recomd_Sys.wv")

#--------------------------------------UI----------------------------------------------


#-------------------------------Page d'accueil-----------------------------------------

def clear_frame(base_frame):
   for widgets in base_frame.winfo_children():
      widgets.destroy()

def page1(root, base_frame, theme):
    
    global img
    clear_frame(base_frame)
    #creer des frames
    PageAccueil= tk.Frame(base_frame, bg=theme[0], bd=1)
    frame1 = tk.Frame(PageAccueil, bg=theme[0], bd=1, relief=tk.SUNKEN) 
    frame2 = tk.Frame(PageAccueil, bg=theme[0], bd=1) 
    frame3 = tk.Frame(PageAccueil, bg=theme[0], bd=1) 

    c = tk.Canvas(PageAccueil, bg=theme[0], bd=0, width=300, height=100, highlightthickness=0)
    c.pack()
    #Textes 
    titre = tk.Label(frame1, text="Bienvenue sur blabla", font =("Ralewayl",40), bg=theme[0], fg=theme[1])
    titre.pack()

    soustitre = tk.Label(frame1, text="yeee", font =("Raleway",30), bg=theme[0], fg=theme[1])
    soustitre.pack()

    #Boutons
    #Bouton valider
    browse_txt = tk.StringVar()
    browse_btn = tk.Button(frame2, textvariable=browse_txt, padx = 50 , pady = 20, command=lambda:recommandation(root, base_frame, theme),
                           font="Raleway", bg=theme[0], fg=theme[1], activebackground=theme[2], activeforeground=theme[1])
    browse_txt.set("Recommandations")
    browse_btn.pack(side= tk.LEFT)

    #Bouton annuler
    txt = tk.StringVar()
    browse_btn = tk.Button(frame2, textvariable=txt,padx = 49 , pady = 20, command=lambda:word_embedding(root, base_frame, theme),
                           font="Raleway", bg=theme[0], fg=theme[1],activebackground=theme[2], activeforeground=theme[1])
    txt.set("Word embedding")
    browse_btn.pack()

    #Bouton Paramètres
    txt = tk.StringVar()
    browse_btn = tk.Button(frame3, textvariable=txt,padx =60 , pady = 20, command=lambda:settings(root, base_frame, theme), 
                           font="Raleway", bg=theme[0], fg=theme[1], activebackground=theme[2], activeforeground=theme[1])
    txt.set("Settings")
    browse_btn.pack(side= tk.LEFT)

    #Bouton Quitter
    txt = tk.StringVar()
    browse_btn = tk.Button(frame3, textvariable=txt,padx = 70 , pady = 20, command=root.destroy, 
                           font="Raleway", bg=theme[0], fg=theme[1], activebackground=theme[2], activeforeground=theme[1])
    txt.set("Exit app")
    browse_btn.pack()
    vide = tk.Canvas(PageAccueil, bg = theme[0], bd=0, width=100, height=100, highlightthickness=0)


    #ajouter
    frame1.pack(expand=tk.YES)
    vide.pack(expand=tk.YES)
    frame2.pack(expand=tk.YES)
    frame3.pack(expand=tk.YES)


    # création d'un canvas
    canvas = tk.Canvas(PageAccueil, bg=theme[0], bd=0, width=300, height=200, highlightthickness=0)

    # logo
    img = ImageTk.PhotoImage(file="logo-insa.png")
    canvas.create_image(150, 100, image=img)
    canvas.pack(side=tk.BOTTOM, expand=tk.YES)

    PageAccueil.pack(expand=tk.YES)

    return PageAccueil
    
    
#-------------------------------Page Settings-----------------------------------------

def settings(root, base_frame,theme):
    OptionList=["Dark","Light","Pink"]

    clear_frame(base_frame)
    setting = tk.Frame(base_frame, bg=theme[0], bd=0, relief=tk.SUNKEN) 

    
    #titre
    titre = tk.Label(setting, text="Settings", font =("Ralewayl",40), bg=theme[0], fg=theme[1])
    titre.pack()
    vide = tk.Canvas(setting, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    
    #Selection Menu
    variable = tk.StringVar()
    variable.set("App Theme")
    opt = tk.OptionMenu(setting, variable, *OptionList)
    opt.config(font=('Helvetica', 12), bg=theme[0], fg=theme[1],highlightthickness=0,
               activebackground=theme[2], activeforeground=theme[1])
    opt.pack()

    vide = tk.Canvas(setting, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()

    def callback(root, base_frame):
        t = variable.get()
        if t=="Dark":
            theme=["#233C5D","#f0f8ff", "#172F4D"]
            clear_frame(base_frame)
            root.config(background=theme[0])
            settings(root, base_frame,theme)

        elif t=="Light":
            theme=["#f0f8ff","black", "#CDD2D7"]
            clear_frame(base_frame)
            root.config(background=theme[0])
            settings(root, base_frame,theme)
        
        elif t=="Pink":
            theme=["#e58da3","white","#C47A8B"]
            clear_frame(base_frame)
            root.config(background=theme[0])
            settings(root, base_frame,theme)
        



    #Bouton Paramètres
    txt = tk.StringVar()
    home_page = tk.Button(setting, textvariable=txt,padx = 34 , pady = 20, command=lambda:page1(root,base_frame,theme),bg=theme[0], fg=theme[1], 
                          font="Raleway", activebackground=theme[2], activeforeground=theme[1])
    txt.set("Home menu")
    home_page.pack()
    vide = tk.Canvas(setting, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    #Bouton Paramètres
    txt = tk.StringVar()
    confirm = tk.Button(setting, textvariable=txt,padx = 34 , pady = 20, command=lambda:callback(root, base_frame),bg=theme[0], fg=theme[1], 
                        font="Raleway", activebackground=theme[2], activeforeground=theme[1])
    txt.set("Confirm")
    confirm.pack(side=tk.LEFT)

    #Bouton Quitter
    txt = tk.StringVar()
    exit = tk.Button(setting, textvariable=txt,padx = 52 , pady = 20, command=root.destroy,bg=theme[0], fg=theme[1], 
                     font="Raleway", activebackground=theme[2], activeforeground=theme[1])
    txt.set("Exit")
    exit.pack()
    setting.pack(expand=tk.YES)

    base_frame.pack(expand=tk.YES)
    
#-------------------------------Page Recommandation-----------------------------------------        

def recommandation(root, base_frame,theme):
    
    clear_frame(base_frame)
    frame=tk.Frame(base_frame, bg=theme[0], bd=0, relief=tk.SUNKEN)
    vide = tk.Canvas(frame, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    #titre
    titre = tk.Label(frame, text="Recommandation", font =("Raleway",40), bg=theme[0], fg=theme[1])
    titre.pack()
    vide = tk.Canvas(frame, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    txt = tk.StringVar()
    home_page = tk.Button(frame, textvariable=txt,padx = 34 , pady = 20, command=lambda:page1(root,base_frame,theme),bg=theme[0], fg=theme[1], 
                          font="Raleway",  activebackground=theme[2], activeforeground=theme[1])
    txt.set("Home menu")
    
    def printInput():
        try:
            
            inp = inputtxt.get(1.0, "end-1c").lower()
            f = find_similar_movie(movie_dictionary[inp])[1:11]
            print(f)
            s = ""
            for i in f:
                s = s + "\n" + i
            lbl.config(text = "Films similaires "+s)
       
        except Exception:
            lbl.config(text = "Film inconnu")
        
    # TextBox Creation
    inputtxt = tk.Text(frame,
                       height = 5,
                       width = 20, bg=theme[0],  fg=theme[1])
      
    inputtxt.pack()
      
    # Button Creation
    printButton = tk.Button(frame,
                            text = "Chercher", 
                            command = printInput,
                            bg=theme[0],  fg=theme[1],
                            activebackground=theme[2], activeforeground=theme[1])
    printButton.pack()
      
    # Label Creation
    lbl = tk.Label(frame, text = "",bg=theme[0],  fg=theme[1],)
    lbl.pack()
    home_page.pack()
    vide = tk.Canvas(frame, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    frame.pack(expand=tk.YES)

#-------------------------------Page Recommandation-----------------------------------------        

def word_embedding(root, base_frame,theme):
    
    clear_frame(base_frame)
    frame=tk.Frame(base_frame, bg=theme[0], bd=0, relief=tk.SUNKEN)
    #titre
    titre = tk.Label(frame, text="Word Embedding", font =("Ralewayl",40), bg=theme[0], fg=theme[1])
    titre.pack()
    vide = tk.Canvas(frame, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    txt = tk.StringVar()
    home_page = tk.Button(frame, textvariable=txt,padx = 34 , pady = 20, command=lambda:page1(root,base_frame,theme),bg=theme[0], fg=theme[1], 
                          font="Raleway", activebackground=theme[2], activeforeground=theme[1])
    txt.set("Home menu")
    home_page.pack()
    vide = tk.Canvas(frame, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    frame.pack(expand=tk.YES)

##-------------------------------App----------------------------------------- 

def app():
    #fonction qui permet de lancer l'application

    #Création d'une première fenêtre
    root = tk.Tk()
    theme = ["#233C5D","#f0f8ff","#172F4D"]
    #personnalisation de la fenetre
    root.title("MovieRecommandation")
    root.geometry("1080x720")                   #taille initiale de la page
    root.minsize(1080,640)                      #taille minimum de la fenetre
    root.iconbitmap("movies.ico")               #icone
    root.config(background=theme[0])
    fraame = tk.Frame(root)
    page1(root, fraame,theme)
    fraame.pack()
    root.mainloop()



#-----------------------------------Variable-------------------------------------------

l = []
dico_mot = {}
movie_dictionary = {} 


#--------------------------------------------------------------------------------------
#                                    Classes
#--------------------------------------------------------------------------------------

class Description:
    
    #Constructeur
    def __init__(self, mot:str, coord):
        self.mot = mot
        self.coord = coord
        
    def toString(self):
        #retourne une chaine de caractère décrivant l'instance
        s = ""
        for i in self.coord:
            s=str(i)+ " " + s
        string = ("mot:"+self.mot +";vect:"+s) 
        return string

class Film:
    
    #Constructeur
    def __init__(self,titre:str,realisateur:str, genre:str,descri: Description):
        self.titre = titre
        self.realisateur=realisateur
        self.genre = genre
        self.description = descri
        self.vec = []

    def toString(self):
        #retourne une chaine de caractère décrivant l'instance
        string = ("titre:"+self.titre +";réalisateur:"+self.realisateur) 
        return string




#--------------------------------------------------------------------------------------
#                            Fonctions et Procédures
#--------------------------------------------------------------------------------------

#-------------------------------------Tests--------------------------------------------


def clean_plot_keywords(string: str, 
    punctuations=r''' !()-[]{};:'"\,<>./?@#$%^&*_~''') :
     # On supprime la ponctuation
    for x in string: 
        #pour tout les mots contenus dans string
        #string est sous la forme (mot1|mot2 etc)
        if x in punctuations: 
            #si la chaine de caratère contient un signe de ponctuation du tableau 
            #ponctuation
            string = string.replace(x, "|") 
            #on remplace la ponctuation par |
    string = string.lower() #on met les chaines de caractères sous forme de miniscule
    string = re.sub(r'\s+', ' ', string).strip()
    tab=string.split('|')
    if len(tab) == 0:
        tab = [""]
    return tab

def clean_genre(string: str):
        string = string.lower() #on met les chaines de caractères sous forme de miniscule
        string = re.sub(r'\s+', ' ', string).strip()
        tab=string.split('|')
        return tab
        

def lecture():
    #fonction qui permet de lire le fichier .cvs et renvoie ce qu'il contient
    with open("movie_metadata.csv",encoding="utf8", mode="r") as cvs_file:
        #on ouvre le fichier csv
        csv_reader=csv.DictReader(cvs_file, delimiter=";")
        line_count = 0
        liste = []
        for row in csv_reader:
            #on parcourt toutes les lignes du fichier
            #-----------il faut traiter ces données (voir sujet)---------------
            movie_title=row['movie_title']
            director_name=row['director_name']
            genres=row['genres']
            plot_keywords=row['plot_keywords']
            if len(plot_keywords) == 0 :
                plot_keywords = ""
            tab_genres = clean_genre(genres)
            tab_plot_keywords = clean_plot_keywords(plot_keywords)
            #------------------------------------------------------------------
            film = Film(movie_title.lower(),director_name,tab_genres,tab_plot_keywords)
            liste.append(film)
            line_count += 1
        #print(f'On a parcourut {line_count} lignes.')
        return liste
    
def vec_moyen(liste):
    #méthode donnant le vecteur moyen d'un film
    dim = len(liste[0].description[0].coord)
    for i in liste:
        vec = np.zeros(dim)
        if len(i.description) > 1:
            denominateur = len(i.description)
            for j in i.description:
                if len(j.coord) > 1:
                    for k in range(dim):
                        #on fait une moyenne des coordonnees des mots clefs
                        vec[k] = (j.coord[k] + vec[k])/denominateur
                i.vec = vec
            
def dict_movie(liste):
    #permet de creer un dictionnaire de film
     emmbed_dict = {}
     n = 0
     for i in liste:
         try:
             if len(i.vec) >1:
                 vector = i.vec
                 emmbed_dict[i.titre] = vector
                 #on associe le nom du film a son vecteur moyen
         except Exception:
             n += 1
     #print(f' {n} mots ne sont pas dans le modèle.')
     return emmbed_dict   

           
def vect(film):
    tab = []
    n = 0
    for i in film.description:
        if len(i) == 0:
            descri = Description(0,[0])
            tab.append(descri)
            
        else:
            try:
                vector = model.wv[i]
                descri = Description(i, vector)
                tab.append(descri)
            except Exception:
                n += 1
                descri = Description(0,[0])
                tab.append(descri)
        #print(f' {n} mots ne sont pas dans le modèle.')
    film.description = tab
    
l = lecture()
for i in l:
    vect(i)
vec_moyen(l)
movie_dictionary = dict_movie(l)  


def find_similar_movie(emmbedes):
    nearest = sorted(movie_dictionary.keys(), key = lambda word:
                     spatial.distance.euclidean(movie_dictionary[word],emmbedes))
    return nearest
        
#-------------------------------------Main---------------------------------------------


#print(find_similar_movie(movie_dictionary['Gladiator'.lower()])[0:10])
app()

#nom = input("entrer non film : ")
#for i in l:
    #if nom in i.titre:
        #print(i.realisateur)
    
