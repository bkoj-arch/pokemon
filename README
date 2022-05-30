####### combat de pokemons

*** Combat de pokemons entre 2 joueurs a distance ***

Chaque joueur est enregistré et ses pokemons sauvegardés jusqu'a la prochaine partie

C'est juste le combat de pokemons, ou les statistiques des pokemons ne sont pas vraiment importante

Nous utilisons cette BDD de pokemons: https://github.com/fanzeyi/pokemon.json/blob/master/pokedex.json

pour les forces et faiblesse:https://github.com/filipekiss/pokemon-type-chart/blob/master/types.json

Quand deux pokemons se battent, on regarde les forces et les faiblesses. 
Si le type du pokemon attaqué et dans les faiblesses du pokemon attaquant, on applique la resolution des dégats avec "Sp. ATTACK"





[ UN COMBAT DE POKEMON ]

Il y a deux joueurs, chaque joueur possède au depart 3 pokemons aléatoires.

un pokemon pour chaque joueur est choisit aléatoirement
Le combat commence et il se déroule tour par tour

le joueur qui a le pokemon le plus rapide commence ("SPEED")

le tour du j1:
On lui montre les statistiques de son pokemon actif et de celles de son adversaire. ("NOM","PV","TYPE"...)

on lui propose 3 choix: 

attaquer, changer de pokemons, fuir

  - attaquer:
    Le pokemon actif du joueur attaque le pokemon adverse,
    on soustrait aux "HP" du pokemon adverse l'"ATTACK" du pokemon attaquant

    si le pokemon attaqué est dans les faiblesses du pokemon attanquant on soustrait "SP.DEFENSE" du pokemon attaqué a l"ATTACK" du pokemon attanquant


  - changer de pokemons
    On montre la liste des pokemons disponibles du joueur.
    Il peut changer de pokemon actif
  

  - fuir
    Le joueur a 1 chance sur 4 de fuir le combat.
    les joueurs gardent leurs pokemons restant dans une BDD
    la partie est terminé si il fuit

un pokemon est K.O quand ses "HP" sont a 0
quand un pokemon est K.O on ne peut plus l'utiliser pour combattre

Puis c'est au tour du joueur 2 et il fait la meme chose.

Le combat continue tant qu'il restent 2 pokemons en combat et qu'aucun joueur n'a fuit le combat.

La partie est terminé quand un joueur n'a plus de pokemon qui peut se battre





[ BDD ]

un joueur a une entrée dans une BDD JSON dès qu'il joue,("joueur":"pokemons") 
on demandera un nom de joueur a chaque lancement du programme. (au 2 joueurs)

Si le joueur n'a pas d'entrée dans la BDD:
On en crée une. avec 3 pokemons aléatoires

Si le joueur a déjà une entrée dans la BDD:
On recupère ses pokemons dans la BDD, les "HP" de tout les pokemons sont au maximum 

Quand le pokemon d'un joueur bat un autre pokemon, le pokemon battu est enlevé des pokemons du joueur adverse et ajouté aux pokemons du joueur qui l'a battu

Il ne peut pas etre utilisé cette partie puisqu'il est K.O

Donc si un joueur bat totalement un autre joueur, il récupère ses 3 pokemons et commencera la prochaine partie avec 6 pokemons

Si un joueur n'a plus aucun pokemon c'est GAME OVER et on le supprime de la BDD




[ A DISTANCE ]

trouver un moyen de jouer a distance avec 2 client et 1 serveur


                    [  BDDs  ]
                        |
[ CLIENT 1 ]     -> [ serveur ]    <-   [ CLIENT 2 ]


--------------------------------------------------------



[ CLIENT 1 ]     <->    [ CLIENT 2 ]
    |                       |
    |_______________________|
               |
               v
            [ serveur  BDD ]





Il faudrait communiquer seulement les actions des clients entre eux
Il faut respecter le tour de chaque joueurs

Pour commencer, le serveur ne peut gerer qu'une partie en cours a la fois 



possibilités:
python http classe : https://docs.python.org/fr/3/library/http.html

python socket : https://docs.python.org/fr/3/howto/sockets.html



ssh?
ftp?















https://raw.githubusercontent.com/vsoch/pokemon/master/pokemon/database/pokemons.json