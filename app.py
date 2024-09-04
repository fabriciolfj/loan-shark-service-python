import asyncio
import logging
import os
from contextlib import asynccontextmanager

import yaml
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from listener.risk_listener import RiskListener


@asynccontextmanager
async def lifespan(app: FastAPI):
    listener = RiskListener()
    listener_task = asyncio.create_task(listener.receive())
    logging.info("Kafka RiskListener started.")
    try:
        yield
    finally:
        await listener.stop()
        await listener_task
        logging.info("Kafka RiskListener stopped.")

app = FastAPI(debug=True, openapi_url='/api/openapi.json', docs_url='/api/docs', lifespan=lifespan)

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, 'oas.yaml')

oas_doc = yaml.safe_load(open(filename, 'r'))

app.openapi = lambda: oas_doc

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from controller import loan_controller