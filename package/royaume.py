#coding:utf-8
# === === Royaume === === #
    
def creerRoyaume() :
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de Type Royaume
    return {"Archer":[],"Soldat":[],"Garde":[],"Effondre":False}

def extraireRoyaume(royaume,role) :
    # Pre-condition : royaume est de type Royaume, role est de type String. Au moins une carte avec Role = role se trouve dans le royaume. 
    # Post-condition : Aucune
    # Resultat : renvoie une carte ayant Role = role. Le royaume est donc modifié car la carte a été retirée du royaume
    #Vérif pas si ya vraiment une carte du role demandé

    carte=royaume[role][0]
    del royaume[0]
    return carte


def entrerRoyaume(royaume,carte) : 
    # Pre-condition : royaume est de type Royaume, carte est de type Carte 
    # Post-condition : Aucune
    # Resultat : Ajoute la carte entrée en paramètre dans le royaume. Le royaume est modifié et renvoyé 
    royaume[roleCarte(carte)].append(carte)
    return 0

def nbCarteRoyaume(royaume) : 
    # Pre-condition : royaume est de type Royaume 
    # Post-condition : Aucune
    # Resultat : Retourne le nombre de citoyens (cartes) dans le royaume placé en paramètre
    nb= 0
    for i in royaume.keys():
        if i!= "Effondre"
            nb = nb + nbCarteRoleRoyaume(royaume,i)
    return nb
    
def nbCarteRoleRoyaume(royaume,role) : 
    # Pre-condition : royaume est de type Royaume, role est un String
    # Post-condition : Aucune
    # Resultat : Retourne le nombre de citoyens (cartes) ayant le role donné dans le royaume placé en paramètre 
    return len(royaume[role])
    

def estEffondre(royaume) :  
    # Pre-condition : Aucune
    # Post-condition :
    # Resultat : Renvoie True si le royaume est effondré et False sinon 
    return royaume["Effondre"]

def effondre(royaume) :
    # Pre-condition : Aucune
    # Post-condition :
    # Resultat : Modifie l'état d'éffondrement du Royaume du joueur passé en paramètre. Le royaume est modifié et renvoyé 
    royaume["Effondre"]=True
    return royaume

def descriptionRoyaume(royaume) : 
    # Pre-condition : royaume est de type Royaume
    # Post-condition :
    # Resultat : renvoie un string qui est une description du royaume donné en parametre. La chaine de caratere contiendra les Roles des cartes ainsi que le nombre des cartes. Finalement elle comprend le total. Par exemple la chaine de caractere pourra renvoyer "Roi : 0, Soldat : 2, Archer : 3, Garde : 1, Total : 6"
    description= []
    for i in royaume.keys():
        if i!= "Effondre"
            description = description + [str(i)":"nbCarteRoleRoyaume(royaume,i)]
    return ",".join(description)

    