import urllib

# variables
count = 0
pokemon_website = "http://assets.pokemon.com/assets/cms2/img/pokedex/full/"
img_type = ".png"

for x in range(1,151):
    #print pokemon_website + str(x) + img_type
    urllib.urlretrieve(pokemon_website + str(x) + img_type, str(x) + img_type)