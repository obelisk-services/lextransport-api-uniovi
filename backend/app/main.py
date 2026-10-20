#!/usr/bin/env python3

from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
#from fastapi_db.database import create_db_and_tables 
#from fastapi_radar import Radar
from .routers import api_router as api
import os
import typer

enable_docs = os.getenv("ENABLE_DOCS", "false").lower() in ("1", "true", "yes")

app = FastAPI(
    title="API de Mercurio",
    version="0.1",
    description="API para la gestion de caucuiones ",
    docs_url="/docs" if enable_docs else None,
    redoc_url="/redoc" if enable_docs else None,
    openapi_url="/openapi.json" if enable_docs else None,
)

@app.get("/")
async def root():
    return {"message": "Uniovi API version 0.1"}

app.include_router(api.router)

cli = typer.Typer()
if __name__ == "__main__":
    cli()