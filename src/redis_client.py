import redis.asyncio as redis
from src.config import config



# redis_client = redis.Redis(host=config.env_data.REDIS_HOST,
#     # password=config.env_data.REDIS_PASSWORD,
#     port=config.env_data.REDIS_PORT,
#     db=0
# )

redis_client = redis.Redis(
    host=config.env_data.REDIS_HOST,
    password=config.env_data.REDIS_PASSWORD,
    port=config.env_data.REDIS_PORT,
    db=0,
    ssl=True,
    ssl_ca_certs="/.redis/root.crt",
)