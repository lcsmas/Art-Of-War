#coding:utf-8
# === === Champs Bataille === === #
import front
import arriere
import carte
def creerChampBataille():
    # Pre-condition : Le joueur entré en paramètre ne doit pas avoir de champ de bataille existant
    # Post-condition : Aucune
    # Resultat : Crée un champ de bataille vide. Crée un front et un arriere, les associent au champ créé et renvoie le champ.
    return {"front" : front.creerFront(),"arriere" : arriere.creerArriere()}
    
    
def redresseCartes(champ):
    # Pre-condition : le champ est de type ChampBataille
    # Post-condition : Aucune
    # Resultat : Toutes les cartes du champ de bataille sont verticales. Le champ de bataille est donc modifié et renvoyé. 
    front = front.getCartes(front(champ))
    arriere = arriere.getCartes(arriere(champ))
    for i in range (0,3) :
        carte.setModeVerticaleCarte(front[i])
        arriere.setModeVerticaleCarte(arriere[i])
    return champ

def estVide(champ) :
    # Pre-condition : le champ est de type ChampBataille
    # Post-condition : Aucune
    # Resultat : Retourne True si aucune carte n'est placée sur le champs de bataille, false sinon
    return front.estVide(front(champ)) and arriere.estVide(arriere(champ))
    

def obtenirCarte(champ,pos) :
    # Pre-condition : La position (pos de type String) entrée en paramètre doit correspondre à une position du plateau et une carte doit se trouver à cet emplacement. champ est de type ChampBataille
    # Post-condition : Aucune
    # Resultat : Renvoie la carte se trouvant à cette position SANS l'enlever
    if pos[0] == "A":
        if not(arriere.emplacementVide(arriere(champ),pos)) :
            return arriere(champ)[pos]
        else :
            raise ValueError("L'emplacement est vide")
    elif pos[0] == "F":
        if not(front.emplacementVide(front(champ),pos)) :
            return front(champ)[pos]
        else :
            raise ValueError("L'emplacement est vide")
    else :
        raise ValueError("Position invalide dans l'argument de la fonction obtenirCarte()")

def nbCarteChampBataille(champ):
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Indique le nombre de carte présente dans le champ de bataille
    return arriere.nbCarteArriere(arriere(champ)) + front.nbCarteFront(front(champ)) 

def front(champ):
    # Pre-condition : le champ est de type ChampBataille
    # Post-condition : Aucune
    # Resultat : retourne le front du champ entré en paramètre
    return champ["front"]

def arriere(champ):
    # Pre-condition : le champ est de type ChampBataille
    # Post-condition : Aucune
    # Resultat : retourne l'arriere du champ entré en paramètre
    return champ["arriere"]

def touteHorizontale(champ):
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Retourne True si toutes les cartes du champ de bataille sont horizontales, retourne False sinon
    cartesFront = front.getCartes(front(champ))
    cartesArriere = arriere.getCartes(arriere(champ))
    for i in range(0,3):
        if cartesFront[i] != "Vide" :
            if carte.estVerticale(cartesFront[i]) :
                return False
        if cartesArriere[i] != "Vide" :
            if carte.estVerticale(cartesArriere[i]) :
                return False
    return True

def estVidePosition(champ,pos):
    # Pre-condition : pos est un string
    # Post-condition : Aucune
    # Resultat : Retourne True si la position contient une carte (en utilisant les fonction estVideFront et estVideArriere)
    if pos[0] == "A":
        return not(arriere.emplacementVide(arriere(champ),pos))
    if pos[0] == "F":
        return not(front.emplacementVide(front(champ),pos))

def verifArriere(champ,pos):
    # Pre-condition : Soit String (chaine de caractère) correspondant la position de la carte cible.
    # Post-condition : Aucune
    # Resultat : Retourne True si l'Arriere situé derrière la carte cible est occupé, retourne False sinon (ou si la carte cible donnée en paramètre n'est pas au front).
    if pos[0] == "A":
        return False
    return not(arriere.emplacementVide(arriere(champ),"A" + num)

def retirerCarte(champ, pos):
    #Retire la carte placé sur pos du champ
    if pos[0] == "A":
        arriere(champ)["A" + pos[1]] = "Vide"
    else :
        front(champ)["F" + pos[1]] = "Vide"
    return champ
    
def avancerCarte(champ,pos):
    # Pre-condition : La position donnée en paramètres est precedemment occupée par une carte au front et une autre carte se situe derriere elle
    # Post-condition : Aucune
    # Resultat : Modifie le champ de bataille dans lequel la carte (située à l'arriere) est envoyée au front. La fonction retourne aussi ce champ.
    if pos[0] == "A":
        raise ValueError('La position doit être un front et pas un arriere')
    if arriere(champ)["A" + pos[1]] == :
        raise ValueError('Aucune carte ne se situe derrière' + pos)
    front(champ)["F" + pos[1]] = arriere(champ)["A" + pos[1]]
    return champ
    
   
