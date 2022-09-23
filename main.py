# For tutorial on FastAPI
# See https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

# move endpoints for world api to module world_api
from api_world import world_router

# create an instance of class FastAPI named "app"
app = FastAPI()

# define function that handles "GET" request with endpoint "/"
@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello there"}

# provide endpoints for world api
app.include_router(world_router)

