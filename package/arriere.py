#coding:utf-8
# === === Arriere === === #

from package.carte import *
from package.champBataille import *
from package.cimetiere import *
from package.front import *
from package.joueur import *
from package.mainJoueur import *
from package.partie import *
from package.pioche import *
from package.reserve import *
from package.royaume import *
def creerArriere() :
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de Type Arriere
    return {"A1" : "Vide", "A2" : "Vide", "A3" : "Vide"}

def emplacementVide(arriere,pos) :
    #Indique si un emplacement est vide
    return arriere[pos] == "Vide"

def estVide(arriere) :
    #Indique si l'arriere est vide
    return arriere["A1"] == "Vide" and arriere["A2"]== "Vide" and arriere["A3"]=="Vide"

def getCartes(arriere) :
    # Renvoie les cartes contenues dans l'arriere
    return [arriere["A1"],arriere["A2"],arriere["A3"]];

def envoyerArriere(arriere,carte,pos) :
    # Pre-condition : arriere est de type Arriere, carte est de type Carte. pos est un string dont le premier caractère est un A et le deuxieme est un chiffre
    # Post-condition : Aucune 
    # Resultat : La carte donnée en parametre est positionné dans l'arriere, à la position pos. La fonction modifie donc l'arriere et le renvoie
    carte.setPositionCarte(carte,pos)
    return arriere[pos] == carte

def nbCarteArriere(arriere) : 
    # Pre-condition : arriere est de type Arriere
    # Post-condition : Aucune 
    # Resultat : Indique le nombre de carte présente sur l'arriere 
    nbCarte = 0
    if arriere["A1"] != "Vide" :
	nbCarte = nbCarte + 1
    if arriere["A2"] != "Vide" :
	nbCarte = nbCarte + 1 
    if arriere["A3"] != "Vide" :
	nbCarte = nbCarte + 1
    return nbCarte 

def extraireArriere(arriere,pos) : 
    # Pre-condition : arriere est de type Arriere, pos est un str 
    # Post-condition : Aucune 
    # Resultat : renvoie la carte située à la position pos, et modifie l'arriere en retirant la carte. 
    res = arriere[pos]
    setPositionCarte(arriere[pos],"Vide")
    arriere[pos] = "Vide"
    return res 
