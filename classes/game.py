import random
from classes.bdd import Bdd
from classes.pokemon import Pokemon
from classes.dresseur import Dresseur


# class game. contient tout le jeu, et la fonction run() qui lance la boucle du jeu
class Game():
    def __init__(self):

        # creation instance bdd
        # a la création bdd récupère TOUTES les données des bdds json
        self.bdd=Bdd()

        # Game a une liste de joueurs
        self.joueurs=[]

        self.winner=None
        self.loser=None

    # premiere fonction appelée, initialise les attributs  
    def start(self):
        print("[ INIT GAME CLASS ]")
        tmp=[]  

        # pour deux joueurs     
        i=0      
        while i<2:

            # on demande un nom
            user=input("joueur"+str(i+1)+"   Quel est votre nom ? ")

            # recupération du dictionnaire du joueur
            dresseur=self.bdd.get_joueur(user)

            # si il existe
            if dresseur != False:

                # on l'ajoute a la liste tmp (liste de dico)
                tmp.append(dresseur)
                i+=1
            else:

                # sinon on lui demande si il veut le creer
                rep="1"
                while rep.lower() not in ["y","n",""]:
                    rep=input(" Le joueur n'existe pas, voulez vous le creer (Y/n) ? ")
                
                if rep.lower() == "n":
                    print(" Impossible de jouer sans user")
                else:
                    print(" Creation user ... ")

                    # on creer un joueur avec le nom tapé et des pokemons aléatoires
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

    # la fonction appelée a chaque fois que le jeu se termine
    # enregistrement des joueurs dans la BDD dresseurs.json
    def end(self):
        print("\n")
        print(self.winner.nom, " GAGNE !! bravo ")
        print(self.winner.nom, " a encore ",len(self.winner.pokemons), " pokemons" )
        self.bdd.update_joueur(self.joueurs)
        self.bdd.save()

    # pour demander a un joueur un nom pour le changement de pokemon
    def change(self,joueur):

        # on lui montre ses pokemons et on recupère une liste des noms des pokemons vivants
        n=joueur.show_pokemons()
        
        noms=""
        for name in n:
            noms+=name+" / "
    
        # si la longueur de la liste de noms de pokemons vivants récupérés est egal a zero
        if len(n) == 0:

            # il a perdu
            return False
        else:
            
            # on lui demande de rentrer un nom de pokemon
            new_poke="1"
            while new_poke.lower() not in n and new_poke!="":
                new_poke=input(" Choisir un nouveau pokemon "+noms+" : ")
            
            if new_poke=="":
                new_poke=n[0]

            # on return le nom du pokemon
            return new_poke

    # boucle principale
    def run(self):
        
        # fonction principale du jeu, elle la boucle main()
        print("")
        print("COMBAT ! ")
        print("")


        # meme principe que bataillenavale.py
        # cette variable sert d'index pour parcourir et alterner de joueur pendant la partie
        # joueurs[i]  sera le joueur en train de faire son tour
        # joueurs[i-1]  sera l'adversaire de ce tour
        # on change i a chaque fin de tour
        i=0

        # tant qu'aucun joueur n'a gagné (quand personne ne fuit ou un joueur n'a plus de pokemons)
        while self.win() == False :


            # si le pokemon du joueur est K.O
            if self.joueurs[i].active_poke.is_dead():

                print("Pokemon K.O")
                print("Changement de pokemons")

                # l'adversaire recupere le pokemon du joueur                
                self.joueurs[i-1].pokemons.append(self.joueurs[i].active_poke)
                
                # le joueur pert son pokemon
                self.joueurs[i].pokemons.remove(self.joueurs[i].active_poke)
                
                # le compteur des pokemons vivants est décrémenté (il sert de verification pour la victoire totale )
                self.joueurs[i].nb_poke_alive-=1


                print("Il vous reste:",self.joueurs[i].nb_poke_alive," pokemons encore debout ! ")


                # on demande un nom de pokemon a l'user pour qu'il puisse changer de pokemon
                new_poke=self.change(self.joueurs[i])
                

                # si il a put taper un nom de pokemon vivant
                if new_poke!=False:

                    # il change de pokemon actif
                    self.joueurs[i].change_pokemon(new_poke)
                else:
                    
                    # sinon ca veut dire qu'il n'a plus de pokemons vivants, il a perdu
                    print("Vous n'avez plus de pokemons qui peut se battre, vous avez perdu :( ")
                    self.winner=self.joueurs[i-1]

            # si il n'y a pas de gagnants
            # !pas beau!
            if self.winner == None:

                # recupération des pokemons actif des joueurs
                adv=self.joueurs[i-1].active_poke
                dre=self.joueurs[i].active_poke

                # affichage des statistiques
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

                    # il change de pokemon ( meme fonction que pour le K.O d'un pokemon )
                    new_poke=self.change(self.joueurs[i])
                    self.joueurs[i].change_pokemon(new_poke)
                    i+=1
                
                elif rep in ["r","run","fuite"]:
                    
                    # 1 chance sur 4 de fuire (0-25/100)
                    print("Vous essayez de fuir...")
                    chance=random.randrange(0,100)
                    if chance<=25:
                        print("Vous fuyez...")
                        
                        # on a un gagnant
                        # on finit la partie
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

        # si on quitte la boucle le jeu est terminé
        self.end()

    # verifie le nombre de pokemon morts pour chaque joueur pendant cette partie
    def win(self):
        for j in self.joueurs:
            if j.nb_poke_alive <= 0:

                # on a un perdant
                self.loser = j
                return True
        return False