#coding:utf-8
# === === Front === === #

from package.arriere import *
from package.carte import *
from package.champBataille import *
from package.cimetiere import *

from package.joueur import *
from package.mainJoueur import *
from package.partie import *
from package.pioche import *
from package.reserve import *
from package.royaume import *

def creerFront() :
    # Pre-condition : Aucune
    # Post-condition : Aucune 
    # Resultat : Crée un element de Type Front
    return {"F1" : "Vide", "F2" : "Vide", "F3" : "Vide"}  

def envoyerFront(front,carte,pos): 
    # Pre-condition : front est de type Front, carte de type Carte et pos de type str
    # Post-condition : Aucune 
    # Resultat : La carte est envoyé au front à la position indiquée en paramètre. Le front est modifié et renvoyé !
    carte.setPositionCarte(carte,pos)
    return front[pos] == carte

def getCartes(front) :
    # Renvoie les cartes contenues dans le front
    return [front["F1"],front["F2"],front["F3"]];

def emplacementVide(front,pos) :
    #Indique si un emplacement est vide
    return front[pos] == "Vide"

def estVide(front) :
    #Indique si le front est vide
    return front["F1"] == "Vide" and front["F2"]== "Vide" and front["F3"]=="Vide"

def nbCarteFront(front) : 
    # Pre-condition : front est de type Front
    # Post-condition : Aucune 
    # Resultat : Indique le nombre de carte présente sur le front
    nbCarte = 0
    if front["F1"] != "Vide" :
	nbCarte = nbCarte + 1
    if front["F2"] != "Vide" :
	nbCarte = nbCarte + 1 
    if front["F3"] != "Vide" :
	nbCarte = nbCarte + 1
    return nbCarte   

def extraireFront(front, pos) : 
    # Pre-condition : front est de type Front, pos est de type str et designe une position non vide
    # Post-condition : Aucune
    # Resultat : Renvoie la carte située à la position "pos" du front donné en parametre. Le front est modifié (car la carte est retiré du front) et la carte retirée est renvoyée. 
    res = front[pos]
    carte.setPositionCarte(front[pos],"Vide")
    front[pos] = "Vide"
    return res
