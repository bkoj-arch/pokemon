import random
from classes.pokemon import Pokemon
from classes.dresseur import Dresseur

class Game():
    def __init__(self):
        joueur1={
                "nom":"Sacha",
                "pokemons":[
                    {
                "id": 25,
                "name": {
                "english": "Pikachu",
                "japanese": "ピカチュウ",
                "chinese": "皮卡丘",
                "french": "Pikachu"
                },
                "type": [
                "Electric"
                ],
                "base": {
                "HP": 35,
                "Attack": 55,
                "Defense": 40,
                "Sp. Attack": 50,
                "Sp. Defense": 50,
                "Speed": 10
                }
                },
                {
                    "id": 26,
                    "name": {
                    "english": "Raichu",
                    "japanese": "ライチュウ",
                    "chinese": "雷丘",
                    "french": "Raichu"
                    },
                    "type": [
                    "Electric"
                    ],
                    "base": {
                    "HP": 60,
                    "Attack": 90,
                    "Defense": 55,
                    "Sp. Attack": 90,
                    "Sp. Defense": 80,
                    "Speed": 110
                    }
                },
                {
                    "id": 27,
                    "name": {
                    "english": "Sandshrew",
                    "japanese": "サンド",
                    "chinese": "穿山鼠",
                    "french": "Sabelette"
                    },
                    "type": [
                    "Ground"
                    ],
                    "base": {
                    "HP": 50,
                    "Attack": 75,
                    "Defense": 85,
                    "Sp. Attack": 20,
                    "Sp. Defense": 30,
                    "Speed": 40
                    }
                }
                    ]
                }

        joueur2={
            "nom":"Regis",
            "pokemons":[
                {
            "id": 45,
            "name": {
            "english": "Vileplume",
            "japanese": "ラフレシア",
            "chinese": "霸王花",
            "french": "Rafflesia"
            },
            "type": [
            "Grass",
            "Poison"
            ],
            "base": {
            "HP": 75,
            "Attack": 80,
            "Defense": 85,
            "Sp. Attack": 110,
            "Sp. Defense": 90,
            "Speed": 50
            }
            },
            {
                "id": 46,
                "name": {
                "english": "Paras",
                "japanese": "パラス",
                "chinese": "派拉斯",
                "french": "Paras"
                },
                "type": [
                "Bug",
                "Grass"
                ],
                "base": {
                "HP": 35,
                "Attack": 70,
                "Defense": 55,
                "Sp. Attack": 45,
                "Sp. Defense": 55,
                "Speed": 25
                }
            },
            {
                "id": 47,
                "name": {
                "english": "Parasect",
                "japanese": "パラセクト",
                "chinese": "派拉斯特",
                "french": "Parasect"
                },
                "type": [
                "Bug",
                "Grass"
                ],
                "base": {
                "HP": 60,
                "Attack": 95,
                "Defense": 80,
                "Sp. Attack": 60,
                "Sp. Defense": 80,
                "Speed": 30
                }
            }
                ]
            }

        self.tmp=[joueur1,joueur2]
 
        self.joueurs=[]
        self.winner=None
        self.loser=None
    
    def start(self):
        print("[ INIT GAME CLASS ]")

        # creer les instances de Pokemon et Joueurs
        for j in self.tmp:
            joueur=Dresseur(j["nom"])
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
            tmp=self.joueurs[0]
            self.joueurs[0]=self.joueurs[1]
            self.joueurs[1]=tmp

    def end(self):
        print("\n")
        print(self.winner.nom, " GAGNE !! bravo ")
        print(self.winner.nom, " a encore ",len(self.winner.pokemons), " pokemons" )

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