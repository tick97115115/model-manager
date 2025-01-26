from fastapi import FastAPI

checkpoints = FastAPI()

# Read
@checkpoints.get("/checkpoints-page")
async def endpoint_extra_networks_page():
    return {"message": "Extra Networks Page"}

@checkpoints.get("/checkpoints")
async def endpoint_checkpoints():
    return {"message": "Extra Networks"}

# Create
@checkpoints.post("/checkpoints/download")
async def endpoint_download():
    return {"message": "Download"}

# Update
@checkpoints.put("/checkpoints/update")
async def endpoint_update():
    return {"message": "Update"}

# Delete
@checkpoints.delete("/checkpoints/delete")
async def endpoint_delete():
    return {"message": "Delete"}