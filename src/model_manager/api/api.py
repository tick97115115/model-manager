from fastapi import FastAPI
from .v1 import v1

api = FastAPI()

api.mount("/api", v1)
