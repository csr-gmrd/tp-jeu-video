import random
def create_team(personnages_db):
    equipe = []
    # tant que l'équipe n'est pas complète 
    while not equipe_est_complete(equipe):

    #   obtenir la liste des personnages disponibles
        liste_des_personnages_dispo = get_personnages_disponible(personnages_db, equipe)
    #   afficher la liste des personnages dispo 
        afficher_personnages_dispo(liste_des_personnages_dispo)
    #   demander le numéro du personnages 
        numéro_du_personnage = demander_personnage(liste_des_personnages_dispo)
    #   ajoute le personnage choisis a l'équipe 
        equipe.append(personnages_db[numéro_du_personnage -1])

    return equipe



def demander_personnage(liste_des_personnages_dispo):
    personnage_demander = input (f"donner le numéro du personnage choisit")
    return demander_personnage 

def afficher_personnages_dispo(liste_des_personnages_dispo):
    print("voici la liste des personnages disponible")
    #pour chaque personnage dans la liste des personnages disponible 
    #   afficher le personnage
    for personnage in liste_des_personnages_dispo :
        print(personnage)



def equipe_est_complete(equipe):
    taille_equipe = len(equipe)
    if taille_equipe >= 3:
        return True 
    else:
        return False

def get_personnages_disponible(personnages, equipe):
    
    liste_personnage_dispo=[]
    #pour chaque personnage dans personnages
    for personnage in personnages: 
    #   regarder si le personnage est dans l'équipe 
        # element in collection
        est_dans_equipe = personnage in equipe 
    #   si il n'est pas dans l'équipe 
        if not est_dans_equipe: 
    #       alors on le rajoute dans la liste des personnages disponible 
            liste_personnage_dispo.append(personnage)
    #return liste des personnages dispo 
    return liste_personnage_dispo


#proposant le menu principal et gérant les interactions.
#afficher le menu principal
def afficher_main_menu():
        print("1. Démarrer une partie")
        print("2. Afficher les personnages disponibles")
        print("3. Quitter le jeu")

def equipe_en_vie(equipe):
    # Verifier que au moins un perso est en vie

    # pour chaque perso dans equipe
    for perso in equipe:
    # regarde le perso en vie ?
    # si en vie renvoie true
        if perso["HP"] > 0:
            return True

    return False


def monstre_aleatoire():
    # chercher monstre dans DB
    from db_init import liste_monstres 
    random.choice(liste_monstres)
    # selectionner monstre aleatoire ( random.choice(liste_monstre) )


def lancer_vague(equipe):
    vague = 1 
    # Tant que equipe vivante
    while equipe_en_vie(equipe): 
    #   Choix aleatoire monstre
        monstre  = monstre_aleatoire()
    #   Combat jusqu'a mort
        combat(equipe, monstre)
        vague = vague + 1
    return vague

def combat(equipe, lancer_vague):
    #tant que l'équipe est en vie
    while equipe_en_vie(equipe): 
        #lancer vague
        return lancer_vague


def lancer_combat():
    pseudo = ask_pseudo()
    team = create_team()
    score = lancer_vague(team)
    display_score(score)
    save_score(ask_pseudo, score)

def display_score(score):
    #afficher le score du joueur a la fin de la partie
    print(f"Score trop uhq stylé: {score}")


def main():#demander le choix de l'utilisateur
    afficher_main_menu()
    choice = input("Entrez votre choix: ")
    if choice == "1":
        lancer_combat()
    #   1. Lancer un combat
    #       -demander le pseudo
    #       -créer une équipe 

#       -lancer les vagues de monstre
# code pour lancer la première vague de monstres
#       -jusqu'a ce que l'équipe ne soit plus en vie
#       -afficher le score du joueur 
#       -enregistrer le score en base de donnée 
#   2. Afficher les personnages disponibles
#   3. Quitter le jeu

def ask_pseudo():
    pseudo = str(input ("Entrer votre peseudo"))
    return pseudo

def afficher_pseudo(pseudo):
    print(f"Voici le pseudo:  {pseudo}")

