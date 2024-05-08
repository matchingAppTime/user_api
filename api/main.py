from fastapi import FastAPI
from mangum import Mangum

from api.routers import user

app = FastAPI()
app.include_router(user.router)

handler = Mangum(app)