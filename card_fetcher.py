import urllib.request
import json
import pandas as pd

def get_set(set):
    """Search for card in a set (3 letter string)
    Return a panda dataframe with card name, price in usd, rarity and set
    """

    contents = urllib.request.urlopen(
        'https://api.scryfall.com/cards/search?q=e%3A'+set).read()
    df = json.loads(contents)
    df = pd.DataFrame.from_dict(df["data"])
    df = df[['name', 'set', 'usd', 'rarity']]
    df['usd'] = df['usd'].astype('float', copy=False)

    return df


def get_random_prices():
    """Go search 50 random cards
    Return a panda dataframe with price in euro and rarity"""

    list_price = []
    list_rarity = []
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
