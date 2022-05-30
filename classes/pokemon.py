import random
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

        self.etat=True

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

    def is_dead(self):
        if self.hp <=0:
            self.hp=0
            self.etat=False
            return True
        return False

    def take_damage(self,poke):
        dmg=int(poke.attack/self.defense*(random.randrange(15,25)))
        print(poke.name, " ATTAQUE ",self.name , " avec ",dmg," degats")
        self.hp-=dmg