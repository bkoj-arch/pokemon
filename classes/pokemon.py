import random


# class Pokemon
# Création des attributs en fonction d'un dictionnaire récupéré dans pokedex.json 
class Pokemon():
    def __init__(self,dico_poke):
        self.id=dico_poke["id"]
        self.name=dico_poke["name"]["french"]
        self.type=dico_poke["type"]
        self.hp_max=dico_poke["base"]["HP"] 
        self.hp=self.hp_max
        self.attack=dico_poke["base"]["Attack"]
        self.defense=dico_poke["base"]["Defense"]
        self.spDefense=dico_poke["base"]["Sp. Defense"]
        self.speed=dico_poke["base"]["Speed"]

        # K.O ou Vivant
        self.etat=True

    # afficher des details sur les pokemons
    def show_stats(self):
        print(self.name)
        print("PV:    ",self.hp,"/",self.hp_max)
        types=""
        for t in self.type:
            types+=t+ " / "
        
        print("Type:  ",types,"    ;   ","Attack:   ",self.attack)

        # if self.etat:
        #     etat= "Vivant"
        # else:
        #     etat= "K.O"
        etat="vivant" if self.etat == True else "K.O"

        print("Etat: ",etat)

    # verifie si le pokemon est K.O (quand ses HP se retrouvent en dessous de 0)
    def is_dead(self):
        if self.hp <=0:
            self.hp=0
            self.etat=False
            return True
        return False

    # c'est un pokemon qui recoit des degats
    def take_damage(self,poke):

        # calcul des dégats reçus, ici on peut ajouter la gestion des types
        dmg=int(poke.attack/self.defense*(random.randrange(15,25)))
        print(poke.name, " ATTAQUE ",self.name , " avec ",dmg," degats")

        # les HP du pokemons diminuent en fonction des dégats calculés
        self.hp-=dmg