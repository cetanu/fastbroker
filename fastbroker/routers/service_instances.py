from fastapi import Body
from fastapi.routing import APIRouter

from fastbroker.components import api_version, originating_identity, accepts_incomplete, instance_id, \
    ServiceInstanceProvisionRequest, Catalog, ServiceInstanceProvisionResponse, Error, \
    ServiceInstanceAsyncOperation, ServiceInstanceUpdateRequest, plan_id, service_id, AsyncOperation, \
    ServiceInstanceResource, operation_id, LastOperationResource, binding_id

router = APIRouter()


@router.put(
    '/service_instances/{instance}',
    tags=['ServiceInstances'],
    summary='provision a service instance',
    responses={
        200: {
            'model': ServiceInstanceProvisionResponse,
            'description': 'OK'
        },
        201: {
            'model': ServiceInstanceProvisionResponse,
            'description': 'Created'
        },
        202: {
            'model': ServiceInstanceAsyncOperation,
            'description': 'Accepted'
        },
        400: {
            'model': Error,
            'description': 'Bad Request'
        },
        409: {
            'model': Error,
            'description': 'Conflict'
        },
    }
)
def service_instance_provision(
        x_broker_api_version: str = api_version,
        x_broker_api_originating_identity: str = originating_identity,
        instance: str = instance_id,
        accept_incomplete: bool = accepts_incomplete,
        request_body: ServiceInstanceProvisionRequest = Body(None),
):
    pass


@router.patch(
    '/service_instances/{instance}',
    tags=['ServiceInstances'],
    summary='update a service instance',
    responses={
        200: {
            'model': {},
            'description': 'OK'
        },
        202: {
            'model': ServiceInstanceAsyncOperation,
            'description': 'Accepted'
        },
        400: {
            'model': Error,
            'description': 'Bad Request'
        },
    }
)
def service_instance_update(
        x_broker_api_version: str = api_version,
        x_broker_api_originating_identity: str = originating_identity,
        instance: str = instance_id,
        accept_incomplete: bool = accepts_incomplete,
        request_body: ServiceInstanceUpdateRequest = Body(None)
):
    pass


@router.delete(
    '/service_instances/{instance}',
    tags=['ServiceInstances'],
    summary='deprovision a service instance',
    responses={
        200: {
            'model': {},
            'description': 'OK'
        },
        202: {
            'model': AsyncOperation,
            'description': 'Accepted'
        },
        400: {
            'model': Error,
            'description': 'Bad Request'
        },
        410: {
            'model': Error,
            'description': 'Gone'
        },
    }
)
def service_instance_delete(
        x_broker_api_version: str = api_version,
        x_broker_api_originating_identity: str = originating_identity,
        instance: str = instance_id,
        service: str = service_id,
        plan: str = plan_id,
        accept_incomplete: bool = accepts_incomplete,
        request_body: ServiceInstanceProvisionRequest = Body(None)
):
    pass


@router.get(
    '/service_instances/{instance}',
    tags=['ServiceInstances'],
    summary='get a service instance',
    responses={
        200: {
            'model': ServiceInstanceResource,
            'description': 'OK'
        },
        404: {
            'model': Error,
            'description': 'Not Found'
        },
    }
)
def service_instance_get(
        x_broker_api_version: str = api_version,
        x_broker_api_originating_identity: str = originating_identity,
        instance: str = instance_id,
        service: str = service_id,
        plan: str = plan_id,
):
    pass


@router.get(
    '/service_instances/{instance}/last_operation',
    tags=['ServiceInstances'],
    summary='get the last requested operation state for service instance',
    responses={
        200: {
            'model': LastOperationResource,
            'description': 'OK'
        },
        400: {
            'model': Error,
            'description': 'Bad Request'
        },
        410: {
            'model': Error,
            'description': 'Gone'
        },
    }
)
def service_instance_get_last_operation(
        x_broker_api_version: str = api_version,
        instance: str = instance_id,
        service: str = service_id,
        plan: str = plan_id,
        operation: str = operation_id,
):
    pass
