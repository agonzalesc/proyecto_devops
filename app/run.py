from fastapi import FastAPI
from app.routes import router
from app.metrics import setup_metrics

app = FastAPI()
app.include_router(router)
setup_metrics(app)
