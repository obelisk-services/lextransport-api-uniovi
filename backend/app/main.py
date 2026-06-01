#!/usr/bin/env python3

from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
#from fastapi_db.database import create_db_and_tables 
#from fastapi_radar import Radar
from .routers import api_router as api
import typer

app = FastAPI(title="API de Uniovi", version="0.1", description="API para la obtención de contratos")

@app.get("/")
async def root():
    return {"message": "Uniovi API version 0.1"}

app.include_router(api.router)

if __name__ == "__main__":
    cli()