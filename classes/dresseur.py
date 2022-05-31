import random

# classe dresseur, les instances sont créées a partir des dicos dans dresseurs.json 
class Dresseur():
    def __init__(self,nom):
        self.nom=nom
        self.pokemons=[]
        self.active_poke=None
        self.nb_poke_alive=None

    # ajouter un pokemon a la liste des pokemons
    def add_pokemon(self,poke):
        self.pokemons.append(poke)
    
    # afficher les stats de tous les pokemons du dresseur
    # renvoie les noms des pokemons qui ne sont pas K.O
    def show_pokemons(self):
        noms=[]
        print("")
        print("Dresseur: ",self.nom )
        for p in self.pokemons:            
            p.show_stats()
            if p.etat==True:
                noms.append(p.name.lower())
            print("")
        
        return noms
    
    # choisir un pokemon aléatoire dan sa liste de pokemons
    def random_poke(self):
        self.active_poke=random.choice(self.pokemons)

    # attaquer un pokemon adverse
    def attaque(self,poke):
        poke.take_damage(self.active_poke)

    # changer de pokemon actif (celui qui se bat)
    # en fonction d'un nom de pokemon
    def change_pokemon(self,poke):
        for p in self.pokemons:
            if p.name.lower()==poke.lower():
                self.active_poke=p
                return True
        return False
