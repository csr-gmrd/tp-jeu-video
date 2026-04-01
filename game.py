# lancement du combat
    # demander de créer une équipe a partir des personnages disponible 
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

def demander_personnage(liste_des_personnages_dispo):
    liste_des_personnages_dispo = str(input("entrer le personnage que vous voulez dans votre équipe"))


def afficher_personnages_dispo(liste_des_personnages_dispo):
    print("voici la liste des personnages disponible")
    #pour chaque personnage dans la liste des personnages disponible 
    #   afficher le personnage
    for personnage in liste_des_personnages_dispo :
        print(personnage)

# quand l'équipe est choisie, lancer la partie

        #lancer la première vague

# combat commence par le joueur a chaque début de partie 

    # tour de l'équipe du joueur

    # quand le tour est finis c'est au tour des mobs

    # tour des mobs 

    #fin du tour des mobs

    # vérifier si l'équipe du joueur est encore en vie

        # SI l'équipe est toujours en vie continuer la manche

        # SI l'équipe n'est plus en vie arrêter la partie

    # répété ça jusqu'a ce que soit le joueur n'est plus de personnage vivant ou si il n'y a plus de monstre vivant 

# si le joueur perd, relancer la partie

# si les monstres meurt lancer le prochain 















































































