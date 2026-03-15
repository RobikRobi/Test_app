import os
import redis.asyncio as redis

redis_url = os.getenv("REDIS_URL")

redis_client = redis.from_url(
    redis_url,
    encoding="utf-8",
    decode_responses=True
)