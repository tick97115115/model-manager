from fastapi import FastAPI
from .checkpoints import checkpoints
from .extra_networks import extra_networks

local = FastAPI()

local.mount("/local", checkpoints)
local.mount("/local", extra_networks)
