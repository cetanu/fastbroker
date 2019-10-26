import uvicorn
from fastapi import FastAPI
from starlette.responses import UJSONResponse

from fastbroker import __versionstr__
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


app = build_app()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80)
