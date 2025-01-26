from fastapi import FastAPI
from .local import local

v1 = FastAPI()

v1.mount("/v1", local)