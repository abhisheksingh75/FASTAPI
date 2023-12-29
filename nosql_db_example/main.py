from fastapi import FastAPI
from routes.route import router
import certifi
ca = certifi.where()

app = FastAPI()

app.include_router(router)