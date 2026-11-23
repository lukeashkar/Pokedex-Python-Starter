import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def allpokemon():
    for pokemon in range(len(data)):
        print(data[pokemon]["name"])

# Add a language choice feature and print the pokemons name based on the user input
lang = input("what language do you want( english, japanese, chinese, or french)")
for pokemon in range(len(data)):
    print(data[pokemon]["name"][lang])

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
y= input("what type of pokemon do you want to search for(examples are dragon, water, and fire)")
for cooltype in data[pokemon]["type"]:
            for item in (data):
                if y.title() in item["type"]:
                    print(item["name"][lang])
  
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def name():
        z=[]
        f = input("what pokemon are you searching for-")
        f = f.lower()
        for pokemon in data:
            if f in pokemon["name"][lang].lower():
                z.append(pokemon["name"][lang])
                print(z)
name()
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!


import json
moves= open("./moves.json",encoding="utf8")
poke_moves = json.load(moves)

def move():
    movelist= []
    pirate_token= input("what pokemon do you want to see the possible moves they can learn-")
    for pokemon in data:
         if pirate_token["type"] == poke_moves["type"]:
              movelist.append(poke_moves["ename"][lang])
              print(movelist)




move()