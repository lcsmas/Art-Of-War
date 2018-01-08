#coding:utf-8
# === === Reserve === === #



def creerReserve() :
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de type Reserve   
    return []

def premiereCarteReserve(reserve) :
    # Pre-condition : reserve est de type Reserve
    # Post-condition : Aucune
    # Resultat : Retourne la premiere carte de la reserve du joueur
    
    return reserve[0]

def nbCarteReserve(reserve) : 
    # Pre-condition : la reserve est de type Reserve
    # Post-condition : Aucune
    # Resultat : Indique le nombre de carte présente dans la réserve
    
    return len(reserve)

def envoiReserve(reserve,carte): 
    # Pre-condition : la reserve est de type Reserve et la carte de type Carte 
    # Post-condition : Aucune
    # Resultat : la carte donnée est envoyée à la reserve !! EN FIN DE FILE !! La réserve est modifiée et renvoyée
    
    return reserve+[carte]
    
def estPleineReserve(reserve):
    #Pre-condition : La fonction prend en paramètre une réserve.
    #Post-Condition : Aucune 
    #Resultat : La fonction retourne True si la reserve est pleine (5 cartes), retourne false sinon
    
    return nbCarteReserve(reserve)>=5