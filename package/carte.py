#coding:utf-8
# === === Carte === === #

import mainJoueur 
import royaume
import joueur

def creerCarte(role):
    #Pre-condition : La carte renvoie un élément de type carte ayant comme role le role donné en parametre (role est un String)
    #Pre-condition : role est "Archer" ou "Garde" ou "Soldat" ou "Roi1" ou "Roi2" 
    #Post-condition : 
    #Resultat : 
    return { "role" : role, "estVerticale" : True, "positionCarte" : "Vide", "pointDegatSubit" : 0 } 

def estVerticale(carte) :
    # Pre-condition : La carte est de type Carte.
    # Post-condition : Aucune
    # Resultat : Retourne True si la carte est verticale, retourne False sinon
    return carte["estVerticale"]

def changementMode(carte) : 
    # Pre-condition : la carte est de type Carte 
    # Post-condition : Aucune
    # Resultat : Le mode de la carte a été modifié :  Vertical si Horizontal et inversement. La carte est modifiée et renvoyée 
    if carte["estVerticale"] == True :
        carte["estVerticale"] = False
    else :
        carte["estVerticale"] = True
    return carte
    

def positionCarte(carte) :
    # Pre-condition : La carte est type Carte 
    # Post-condition : Aucune
    # Resultat : Retourne la chaine de caractère représentant la position de la carte sur le plateau ("F1","F2",...,"A3")  
    return carte["positionCarte"]
    
def setPositionCarte(carte,pos) : 
    # Pre-condition : La carte est type Carte, la pos est une string 
    # Post-condition : Aucune
    # Resultat : Modifie la position de la carte. Cette fonction renvoie aussi la carte modifiée
    carte["positionCarte"] = pos
    return carte    

def pointAttaque(carte, main) : 
    # Pre-condition : la carte est de type Carte
    # Post-condition : Aucune
    # Resultat : retourne le nombre de point d'attaque de la carte
    if roleCarte(carte) == "Soldat" :
        return mainJoueur.nbCarteMain(main)
    return 1 #Toutes les cartes ont 1 d'attaque sauf le soldat
    
def pointDefense(carte) : 
    # Pre-condition : la carte est de type Carte
    # Post-condition : Aucune
    # Resultat : retourne le nombre de point de defense de la carte EN FONCTION DE SON MODE 
    role = roleCarte(carte)

    if role in ["Archer", "Soldat"] : #Archer et Soldat ont le même nombre de points de défense
        if estVerticale(carte) :
            return 2
        return 1

    if role == "Garde":
        if estVerticale(carte) :
            return 3
        return 2

    if role == "Roi1" : #Le nombre de points de défenses du Roi1 ne dépend pas de sa posture 
        return 4

    if role == "Roi2" :
        if estVerticale(carte) :
            return 5
        return 4
    
    
def pointDegat(carte) : 
    # Pre-condition : la carte est de type Carte
    # Post-condition : Aucune
    # Resultat : retourne le nombre de point de dégat subits de la carte
    return carte["pointDegatSubit"]
    
def capture(carte,joueur) : 
    # Pre-condition : la carte est de type Carte. le joueur est de type Joueur
    # Post-condition : Aucune
    # Resultat : la carte devient capturée. La carte est placée dans le Royaume du joueur entrée en parametre
    roy = joueur.royaume(joueur)
    royaume.entrerRoyaume(roy, carte)
    return 0
    
def setPointDegat(carte,nouvDegat) :
    # Pre-condition : La carte est de type Carte, nouvDegat est de type Int. 
    # Post-condition : Aucune
    # Resultat : Modifie la carte donnée en parametre. pointDegats(carte) de la carte modifiée est egal à nouvDegat. 
    carte['pointDegatSubit'] = nouvDegat
    return 0
    
def roleCarte(carte):
    # Pre-condition : carte est de type Carte
    # Post-condition : Renvoi un string parmis ces valeurs : Garde, Archer, Soldat, Roi
    # Resultat : Renvoi le rôle de la carte entrée en paramètre
        
    return carte['role']
    
def estAPortee(carte,cible) : 
    # Pre-condition : carte et cible sont toutes deux des Carte présentent sur le champ de bataille
    # Post-condition : 
    # Resultat : Renvoie True si la cible est à portée de la carte, False sinon
    pos_attaquant = carte['positionCarte']
    role_attaquant = carte ['role']
    pos_defenseur = cible['positionCarte'] 
    role_defenseur = cible['role']

    if role_attaquant == "Roi1" :
        if pos_attaquant in ['F1','F2','F3'] :
            if pos_defenseur in ['F1','F2','F3']:
                return True
            elif pos_attaquant=='F1' and pos_defenseur =='A1':
                return True
            elif pos_attaquant=='F2' and pos_defenseur =='A2':
                return True
            elif pos_attaquant=='F3' and pos_defenseur=='A3':
                return True
            else :
                return False
        if pos
    pass
    
    