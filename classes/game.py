import random
from classes.bdd import Bdd
from classes.pokemon import Pokemon
from classes.dresseur import Dresseur

class Game():
    def __init__(self):

        self.bdd=Bdd()
        self.joueurs=[]

        self.winner=None
        self.loser=None
    
    def start(self):
        print("[ INIT GAME CLASS ]")

        tmp=[]       
        i=0
        while i<2:
            user=input("joueur"+str(i+1)+"   Quel est votre nom ? ")

            dresseur=self.bdd.get_joueur(user)
            if dresseur != False:
                tmp.append(dresseur)
                i+=1
            else:
                rep="1"
                while rep.lower() not in ["y","n",""]:
                    rep=input(" Le joueur n'existe pas, voulez vous le creer (Y/n) ? ")
                
                if rep.lower() == "n":
                    print(" Impossible de jouer sans user")
                else:
                    print(" Creation user ... ")
                    tmp.append(self.bdd.create_joueur(user))
                    i+=1

        # creer les instances de Pokemon et Joueurs
        for j in tmp:
            joueur = Dresseur(j["nom"])
            for poke in j["pokemons"]:
                poke=Pokemon(poke)
                joueur.add_pokemon(poke)
            joueur.nb_poke_alive=len(joueur.pokemons)
            self.joueurs.append(joueur)
    
        print("")
        print(" Selection aléatoire des pokemons ")
        print("")

        for j in self.joueurs:
            j.random_poke()
            j.active_poke.show_stats()

        # determination du pokemon le plus rapide
        if self.joueurs[0].active_poke.speed < self.joueurs[1].active_poke.speed:
            tmp = self.joueurs[0]
            self.joueurs[0] = self.joueurs[1]
            self.joueurs[1] = tmp



    def end(self):
        print("\n")
        print(self.winner.nom, " GAGNE !! bravo ")
        print(self.winner.nom, " a encore ",len(self.winner.pokemons), " pokemons" )
        self.bdd.update_joueur(self.joueurs)
        self.bdd.save()

    def change(self,joueur):
        n=joueur.show_pokemons()
        noms=""
       
        for name in n:
            noms+=name+" / "
        new_poke="1"

        if len(n) == 0:
            return False
        else:
            while new_poke.lower() not in n and new_poke!="":
                new_poke=input(" Choisir un nouveau pokemon "+noms+" : ")
            
            if new_poke=="":
                new_poke=n[0]
            return new_poke

    def run(self):
        
        print("")
        print("COMBAT ! ")
        print("")

        i=0
        while self.win() == False :

            if self.joueurs[i].active_poke.is_dead():
                print("Pokemon K.O")
                print("Changement de pokemons")
                
                self.joueurs[i-1].pokemons.append(self.joueurs[i].active_poke)
                self.joueurs[i].pokemons.remove(self.joueurs[i].active_poke)
                self.joueurs[i].nb_poke_alive-=1


                print("Il vous reste:",self.joueurs[i].nb_poke_alive," pokemons encore debout ! ")

                new_poke=self.change(self.joueurs[i])
                

                if new_poke!=False:
                    self.joueurs[i].change_pokemon(new_poke)
                else:
                    print("Vous n'avez plus de pokemons qui peut se battre, vous avez perdu :( ")
                    self.winner=self.joueurs[i-1]

            
            if self.winner == None:
                adv=self.joueurs[i-1].active_poke
                dre=self.joueurs[i].active_poke

                print("\n"*10)
                adv.show_stats()
                print("\n"*4)
                print(" A vous de jouer!")
                print(self.joueurs[i].nom)
                dre.show_stats()
                
                rep=input(" Que voulez vous faire ? (A/C/R): ").lower()

                print("")
                if rep in ["a","attack","attaque",""]:
                    self.joueurs[i].attaque(adv)
                    i+=1
                
                elif rep in ["c","change","changer"]:
                    new_poke=self.change(self.joueurs[i])
                    self.joueurs[i].change_pokemon(new_poke)
                    i+=1
                
                elif rep in ["r","run","fuite"]:             
                    print("Vous essayez de fuir...")
                    chance=random.randrange(0,100)
                    if chance<=25:
                        print("Vous fuyez...")

                        self.winner=self.joueurs[i-1]
                        self.end()
                        return False

                    else:
                        print("Vous restez dans le combat...")
                
                else:
                    print("")
                    print("Je n'ai pas compris...")
                    print("")
                
            
                if i==2:
                    i=0

        self.end()

    def win(self):
        for j in self.joueurs:
            if j.nb_poke_alive <= 0:
                self.loser = j
                return True
        return False