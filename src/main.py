import os
from fastapi import FastAPI

app = FastAPI(title="SolarApp API", version="0.1.0")


@app.get("/")
def root() -> dict[str, str]:
    return {"name": "SolarApp", "status": "ok"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": os.getenv("APP_ENV", "lab")}
