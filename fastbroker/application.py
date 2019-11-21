import os
import json
import uvicorn
from fastapi import FastAPI
from starlette.responses import UJSONResponse

from fastbroker import __versionstr__
from fastbroker.data import db_mapping
from fastbroker.config import FastBrokerConfig
from fastbroker.routers import catalog, service_instances, service_bindings


def build_app():
    api = FastAPI(
        title="FastBroker",
        description="An Open Service Broker built on FastAPI",
        version=__versionstr__,
        default_response_class=UJSONResponse,
    )

    api.include_router(catalog.router, prefix="/v2")
    api.include_router(service_instances.router, prefix="/v2")
    api.include_router(service_bindings.router, prefix="/v2")

    return api


# TODO: remove "example"
config_location = os.getenv("FASTBROKER_CONFIG", "example_config.json")
with open(config_location) as f:
    config = FastBrokerConfig(**json.load(f))

app = build_app()
db = db_mapping[config.database.type]


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80)
