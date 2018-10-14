from App.redis_price_server import get_all_redis_hash
import schedule
from App.card_fetcher import get_all_standard

schedule.every().day.at("15:00").do(
    get_all_redis_hash(get_all_standard())
)