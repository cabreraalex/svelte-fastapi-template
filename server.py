import random
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/home", StaticFiles(directory="frontend/public", html=True), name="home")

@app.get("/")
async def home():
    return RedirectResponse(url='home')


@app.get("/rand")
async def randomInt():
    return random.randint(0, 1000)
