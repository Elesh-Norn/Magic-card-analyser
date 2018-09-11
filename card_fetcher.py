import urllib.request
import json
import pandas as pd

def get_random_prices():

    list_price = []
    list_rarity= []
    for n in range(50):

        contents = urllib.request.urlopen(
            'https://api.scryfall.com/cards/random'
        ).read()
        contents = json.loads(contents)

        if "eur" in contents:
            list_price.append(float(contents["eur"]))
            list_rarity.append(contents['rarity'])
        else:
            continue
    df = pd.DataFrame({'Price': list_price, 'Rarity': list_rarity})

    return df
