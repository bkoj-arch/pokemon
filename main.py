
from classes.pokemon import Pokemon
from classes.dresseur import Dresseur


def change(joueur):
  n=joueur.show_pokemons()
  noms=""

  for name in n:
    noms+=name+" / "
  new_poke=""

  while new_poke.lower() not in n:
    new_poke=input(" Choisir un nouveau pokemon "+noms+" : ")
  
  return new_poke

# a recuperer dans la bdd dresseurs.json
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




joueurs=[]


# creer les instances de Pokemon et Joueurs

for j in [joueur1,joueur2]:
    joueur=Dresseur(j["nom"])
    for poke in j["pokemons"]:
        poke=Pokemon(poke)
        joueur.add_pokemon(poke)
    joueurs.append(joueur)




print("")

print(" Selection aléatoire des pokemons ")
print("")

for j in joueurs:
    j.random_poke()
    print(j.nom)
    j.active_poke.show_stats()
    print("")


print("")
print("COMBAT ! ")
print("")

# determination du pokemon le plus rapide

if joueurs[0].active_poke.speed < joueurs[1].active_poke.speed:
  tmp=joueurs[0]
  joueurs[0]=joueurs[1]
  joueurs[1]=tmp


i=0







while True:
  
  
  if joueurs[i].active_poke.is_dead():
    print("Pokemon K.O")
    print("Changement de pokemons")
    
    new_poke=change(joueurs[i])
    
    joueurs[i].change_pokemon(new_poke)


  adv=joueurs[i-1].active_poke
  dre=joueurs[i].active_poke



  print("\n"*10)
  adv.show_stats()
  print("\n"*4)
  print(" A vous de jouer!")
  print(joueurs[i].nom)
  dre.show_stats()
  
  rep=input(" Que voulez vous faire ? (A/C/R): ").lower()

  if rep in ["a","attack","attaque"]:
    joueurs[i].attaque(adv)
    i+=1
  
  elif rep in ["c","change","changer"]:
    new_poke=change(joueurs[i])
    joueurs[i].change_pokemon(new_poke)
    i+=1
  
  # if adv.is_dead():
  #   print("Pokemon K.O")


  
  
  if i==2:
    i=0