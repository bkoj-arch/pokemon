import json
import sys
import random

class Bdd():
    pokedex="bdd/pokedex.json"
    types="bdd/types.json"
    dresseurs="bdd/dresseurs.json"
    def __init__(self):

        with open(Bdd.pokedex,"r") as f:
            self.pokedex=json.load(f)
        with open(Bdd.types,"r") as f:
            self.types=json.load(f)
        with open(Bdd.dresseurs,"r") as f:
            self.dresseurs=json.load(f)

    def create_joueur(self,nom):
        joueur={
            "nom":nom,
            "pokemons":[]
        }
        for i in range(3):
            joueur["pokemons"].append(self.get_random_poke())
        self.dresseurs.append(joueur)
        return joueur

    def get_joueur(self,nom):
        for j in self.dresseurs:
            if j["nom"]==nom:
                return j
        return False
    

    def update_joueur(self,liste_joueur):

        for j in liste_joueur:
            for d in self.dresseurs:
                if d["nom"] == j.nom:
                    pokes=[]

                    for poke in j.pokemons:
                        poke=self.pokedex[poke.id-1]
                        pokes.append(poke)
                    d["pokemons"]=pokes



    def get_random_poke(self):
        return random.choice(self.pokedex)
    
    def save(self):
        with open(Bdd.dresseurs,"w") as f:
            json.dump(self.dresseurs, f)

