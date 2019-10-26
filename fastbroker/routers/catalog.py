from fastapi.routing import APIRouter
from fastbroker.components import api_version, Catalog

router = APIRouter()


@router.get(
    '/catalog',
    tags=['Catalog'],
    summary='get the catalog of services that the service broker offers',
    response_model=Catalog
)
def catalog(x_broker_api_version=api_version):
    pass
