from fastapi import FastAPI



app = FastAPI()

@app.get("/", tags=["Test page"])
async def test_masseg() -> dict:
    return {"message": "Welcome to my test page of the site!"}
