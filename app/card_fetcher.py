import urllib.request
import json
import pandas as pd

STANDARD_SET_LIST = ['m19', "dom", "rix", "xln", "grn"]


def get_all_card_from_search(url):
    """
    During a search, will pull other cards and add them to the
    "data" list from scryfall. Returns it if there is no other card
    """

    temp_dic = urllib.request.urlopen(url).read()
    temp_dic = json.loads(temp_dic)
    if temp_dic["has_more"]:
        temp_dic["data"].extend(
            get_all_card_from_search(temp_dic["next_page"]))
        return temp_dic["data"]
    else:
        return temp_dic["data"]


def get_set(set):
    """
    Search for card in a set (3 letter string)
    Return a panda dataframe with card name, price in usd, rarity and set
    """

    temp_list = get_all_card_from_search('https://api.scryfall.com/cards/search?q=e:'+set)
    df = pd.DataFrame.from_dict(temp_list)
    df = df[['name', 'set', 'usd', 'rarity', 'id']]
    df['usd'] = df['usd'].astype('float', copy=False)

    return df


def get_all_standard():
    """
    Search for all card in Standard and return a Dataframe
    """
    df = pd.DataFrame()
    for magics_set in STANDARD_SET_LIST:
        df = pd.concat([df, get_set(magics_set)])

    return df


def get_random_prices():
    """
    Go search 50 random cards
    Return a panda dataframe with price in euro and rarity
    """

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


def write_json_from_df(df):
    temp_json = df.to_json(orient='table')
    with open("truc.txt", 'w+') as temp:
        temp.write(temp_json)
