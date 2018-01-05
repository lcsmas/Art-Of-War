#coding:utf-8
# === === Joueur === === #
    
def creerJoueur(indice,nom) : 
    #Pre-condition : indice est un int = 0 ou 1 
    #                nom est un str 
    #Post-condition :Aucune
    #resultat : Crée un element de Type Joueur ayant le nom entré en parametre. Il crée aussi un Royaume vide, un champ de bataille vide, une réserve vide, un cimetiere vide, une main (contenant le Roi). Il crée aussi une pioche. Tous ses elements seront assignés aux joueurs. La fonction renverra le Joueur créé
    Joueur = {}
    Joueur["Nom"]=nom
    Joueur["ChampBataille"]=creerChampbataille()
    Joueur["Cimetiere"]=creerCimetiere()
    Joueur["Reserve"]=creerreserve()
    Joueur["Royaume"]=creerRoyaume()
    Joueur["Main"]=creerMain()
    Joueur["Pioche"]=creerpioche()
    return Joueur

def nom(joueur):
    # Pre-condition : joueur de type Joueur
    # Post-condition : Aucune
    # Resultat : Renvoi le nom du joueur entré en paramètre
    
    return joueur["Nom"]

def champBataille(joueur) :
    # Pre-condition : Le joueur doit être de la partie, il est de type Joueur
    # Post-condition : Aucune
    # Resultat : retourne le champ de bataille du joueur entré en paramètre
    
    return joueur["ChampBataille"]

def main(joueur) : 
    # Pre-condition : Le joueur doit être de la partie, il est de type Joueur
    # Post-condition : Aucune
    # Resultat : retourne la main du joueur entré en paramètre
    
    return joueur["Main"]

def royaume(joueur) :
    # Pre-condition : Le joueur doit être de la partie, il est de type Joueur
    # Post-condition : Aucune
    # Resultat : Renvoi le royaume du joueur
    
    return joueur["Royaume"]

def pioche(joueur) :
    # Pre-condition : Le joueur doit être de la partie, il est de type Joueur
    # Post-condition : Aucune
    # Resultat : Retourne la pioche du joueur entré en paramètre
    
    return joueur["Pioche"]

def reserve(joueur) :
    # Pre-condition : Le joueur doit être de la partie, il est de type Joueur
    # Post-condition : Aucune
    # Resultat : Retourne la reserve du joueur entré en paramètre
    
    return joueur["Reserve"]

def cimetiere(joueur) :
    # Pre-condition : Le joueur doit être de la partie, il est de type Joueur
    # Post-condition : Aucune
    # Resultat : Retourne le cimetiere du joueur entré en paramètre
    
    return joueur["Cimetiere"]

def reinitDegat(joueur) : 
    #Pre-condition : le joueur est de Type Joueur
    #Post-condition : les unités posées sur le champ de bataille (front et arriere), les unités en réserve et 
    #les unités dans le royaume ont leur point de degat subis remis à 0
    #Resultat : Ne renvoie rien mais modifie les unites du cdb de la reserve et du royaume
    royaume = royaume(joueur)
    for role in royaume.keys():
    	#parcourera tout les rôles du royaume, arrêt : quand il a tout parcouru
    	for carte in role:
    		#parcourera toute la liste de carte du role
    		setPointDegat(carte,0)
    reserve = reserve(joueur)
    for carte in reserve :
    	setPointDegat(carte,0)
    champDeBataille = champBataille(joueur)
    for ligne in champDeBataille :
    	for position in ligne.keys() :
    		setPointDegat(carte,0)
    return 0