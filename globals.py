import redis
from api42 import Api
import config

r = redis.Redis(host=config.redis_host, port=config.redis_port, db=0, password=config.redis_password)
api = Api(config.key, config.secret)
