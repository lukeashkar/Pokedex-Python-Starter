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
        #loop through entire list
        for pokemon in data:
        #check if user input inside of the name of the pokemon
            if f in pokemon["name"][lang].lower():
                #append into list if it is
                z.append(pokemon["name"][lang])
                print(z)
            #if nothing is in the list return invalid search or smt



name()
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

