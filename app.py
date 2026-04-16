import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
""" names = {}
 """
for index, pokemon in enumerate(data): 
    print(index, ":",pokemon["name"])

""" def pokemon_names(json):
    for pokemon_name in pokemon_names:
        if pokemon_name in items.json:
 """
# Add a language choice feature and print the pokemons name based on the user input
""" Language = input("Enter a language: English, French, Chinese, Japanese")
if Language == "English":
    for index, pokemon in enumerate(data): 
        print(pokemon["name"]["english"])
elif Language == "French":
    for index, pokemon in enumerate(data): 
        print(pokemon["name"]["french"])
elif Language == "Chinese":
    for index, pokemon in enumerate(data): 
        print(pokemon["name"]["chinese"])
else:
    for index, pokemon in enumerate(data): 
        print(pokemon["name"]["japanese"])
 """
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
Type = int(input("Enter a type of pokemon:"))
print(pokemon[Type])
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

#Based on user input, show all moves that pokemon  could learn based on type. For example, if Charizard is fire/fyling, show all fire and flying moves.
