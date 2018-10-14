import redis
import datetime

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def get_all_redis_hash(df):
    """
    Set the price of today, in redis server, as card id : date : price
    :param df: pandas DataFrame with card id and price from scryfall
    """
    today_date = datetime.date.today()
    for _ in df['id']:
        price = float(df.loc[df['id'] == _]['usd'].values)
        r.hset(_, today_date, price)

