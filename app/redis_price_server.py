import redis
import datetime
import pandas as pd

r = redis.Redis(host="redis_price", port=6379, decode_responses=True)

def get_all_redis_hash(df):
    """
    Set the price of today, in redis server, as card id : date : price
    :param df: pandas DataFrame with card id and price from scryfall
    """
    today_date = datetime.date.today()
    for _ in df['id']:
        price = float(df.loc[df['id'] == _]['usd'].values)
        r.hset(_, today_date, price)

def get_price_list_from_redis(card_id):
    """"
    From a card id, give the list of price from redis.
    Return a DataFrame with dates as index and 'price' as column
    """
    df = pd.DataFrame.from_dict(app.redis_price_server.r.hgetall(card_id),
                                orient="index", columns=['price'])
    df['price'] = df['price'].astype('float', copy=False)
    df.index.name = 'date'

    return df