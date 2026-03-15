from fastapi import FastAPI, HTTPException
from src.redis_client import redis_client
from src.user_models import User

app = FastAPI()

@app.get("/redis-test")
async def redis_test():
    await redis_client.set("test", "hello")
    value = await redis_client.get("test")
    return {"redis_value": value}

@app.post("/add")
async def add_user(data: User):
    redis_key = f"user:{data.id}"
    await redis_client.set(redis_key, data.model_dump_json())
    return {"status": "user added", "user": data}


@app.get("/get_user/{user_id}")
async def get_user(user_id: int):
    redis_key = f"user:{user_id}"
    user_data = await redis_client.get(redis_key)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data