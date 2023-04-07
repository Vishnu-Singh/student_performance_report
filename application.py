from fastapi import FastAPI
import uvicorn
from dotenv import dotenv_values

config = dotenv_values(".env")
app = FastAPI()

@app.get("/")
async def index():
    return "Welcome to Student Performance Report Service"

if __name__ == "__main__":
    uvicorn.run(app=app,host=config.get("HOST"),port=int(config.get("PORT")))