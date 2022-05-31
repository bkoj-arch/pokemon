import json
import sys
import random

class Bdd():

    # fichiers vers les bdds
    pokedex="bdd/pokedex.json"
    types="bdd/types.json"
    dresseurs="bdd/dresseurs.json"

    def __init__(self):

        # recupération des bdd json dans des dictionnaires python
        # !! ce sont des listes de dictionnaires !!
        # pendant le jeu, on utilise que ces dictionnaires
        # quand on quitte on enregistre les dicos dans les fichiers
        with open(Bdd.pokedex,"r") as f:
            self.pokedex=json.load(f)
        with open(Bdd.types,"r") as f:
            self.types=json.load(f)
        with open(Bdd.dresseurs,"r") as f:
            self.dresseurs=json.load(f)

    # Ajouter un joueur a la liste des joueurs
    def create_joueur(self,nom):
        joueur={
            "nom":nom,
            "pokemons":[]
        }

        # on lui ajoute 3 pokemons aléatoire
        for i in range(3):
            joueur["pokemons"].append(self.get_random_poke())
        
        # on rajoute le joueur au dico
        self.dresseurs.append(joueur)
        return joueur

    # recupération d'un joueur en fonction d'un nom
    def get_joueur(self,nom):
        for j in self.dresseurs:
            if j["nom"]==nom:
                return j
        return False
    
    # avant de save dans les fichiers
    # on modifie les pokemons d'un joueur en fonction de ceux qu'ils a gagné/perdu
    # pendant la partie
    # liste_joueur est une liste d'instances de la classe joueur des joueurs de la partie
    def update_joueur(self,liste_joueur):

        # parcourt des joueurs de la partie
        for j in liste_joueur:

            # parcourt des dictionnaires des joueurs
            for d in self.dresseurs:

                # on trouve le bon dico on fonction du nom du joueur
                if d["nom"] == j.nom:

                    # on lui rajoute les pokemons gagnés
                    # on va les chercher dans le pokedex donc leur HP est au max
                    pokes=[]
                    for poke in j.pokemons:
                        poke=self.pokedex[poke.id-1]
                        pokes.append(poke)
                    d["pokemons"]=pokes

    # renvoie un pokemon aléatoire dans le pokedex
    def get_random_poke(self):
        return random.choice(self.pokedex)
    
    # on sauvegarde les joueurs dans la bdd dresseur.json
    # on apellera update_joueur() avant
    def save(self):
        with open(Bdd.dresseurs,"w") as f:
            json.dump(self.dresseurs, f)

