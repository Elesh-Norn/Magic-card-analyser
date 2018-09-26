import redis, datetime, pandas as pd
import card_fetcher
r = redis.Redis(host="localhost",
                port=6379, decode_responses=True)

def get_all_redis_hash(df):
    today_date = datetime.date.today()
    for _ in df['id']:
        price = float(df.loc[df['id'] == _]['usd'].values)
        r.hset(_, today_date, price)
