
import random
class Dresseur():
    def __init__(self,nom):
        self.nom=nom
        self.pokemons=[]
        self.active_poke=None

    def add_pokemon(self,poke):
        self.pokemons.append(poke)
    
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
    
    def random_poke(self):
        
        self.active_poke=random.choice(self.pokemons)

    def attaque(self,poke):
        poke.take_damage(self.active_poke)

    def change_pokemon(self,poke):
        for p in self.pokemons:
            if p.name.lower()==poke.lower():
                self.active_poke=p
                
                return True
        return False