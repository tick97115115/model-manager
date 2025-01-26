from fastapi import FastAPI

extra_networks = FastAPI()

# Read
@extra_networks.get("/extra-networks-page")
async def endpoint_extra_networks_page():
    return {"message": "Extra Networks Page"}

@extra_networks.get("/extra-networks")
async def endpoint_extra_networks():
    return {"message": "Extra Networks"}

# Create
@extra_networks.post("/extra-networks/download")
async def endpoint_download():
    return {"message": "Download"}

# Update
@extra_networks.put("/extra-networks/update")
async def endpoint_update():
    return {"message": "Update"}

# Delete
@extra_networks.delete("/extra-networks/delete")
async def endpoint_delete():
    return {"message": "Delete"}