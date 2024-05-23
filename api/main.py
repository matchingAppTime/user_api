from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

from api.routers import user

app = FastAPI()
app.include_router(user.router)

handler = Mangum(app)
app.add_middleware(
    CORSMiddleware,
    # TODO web ios adr のオリジンがわかれば記載
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[""]
)