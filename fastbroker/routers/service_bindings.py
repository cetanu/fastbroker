from fastapi import Body
from fastapi.routing import APIRouter

from fastbroker.components import api_version, originating_identity, accepts_incomplete, instance_id, \
    ServiceInstanceProvisionRequest, ServiceInstanceProvisionResponse, Error, \
    ServiceInstanceAsyncOperation, plan_id, service_id, AsyncOperation, \
    operation_id, LastOperationResource, binding_id

router = APIRouter()


@router.get(
    '/service_instances/{instance}/service_bindings/{binding}/last_operation',
    tags=['ServiceBindings'],
    summary='get the last requested operation state for service binding',
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
def service_binding_get_last_operation(
        x_broker_api_version: str = api_version,
        instance: str = instance_id,
        binding: str = binding_id,
        service: str = service_id,
        plan: str = plan_id,
        operation: str = operation_id,
):
    pass


@router.put(
    '/service_instances/{instance}/service_bindings/{binding}',
    tags=['ServiceBindings'],
    summary='generate a service binding',
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
def service_binding_provision(
        x_broker_api_version: str = api_version,
        x_broker_api_originating_identity: str = originating_identity,
        instance: str = instance_id,
        binding: str = binding_id,
        accept_incomplete: bool = accepts_incomplete,
        request_body: ServiceInstanceProvisionRequest = Body(None),
):
    pass


@router.delete(
    '/service_instances/{instance}/service_bindings/{binding}',
    tags=['ServiceBindings'],
    summary='deprovision a service binding',
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
def service_binding_delete(
        x_broker_api_version: str = api_version,
        x_broker_api_originating_identity: str = originating_identity,
        instance: str = instance_id,
        binding: str = binding_id,
        service: str = service_id,
        plan: str = plan_id,
        accept_incomplete: bool = accepts_incomplete,
        request_body: ServiceInstanceProvisionRequest = Body(None)
):
    pass


@router.get(
    '/service_instances/{instance}/service_bindings/{binding}',
    tags=['ServiceBindings'],
    summary='get a service binding',
    responses={
        200: {
            'model': {},
            'description': 'OK'
        },
        404: {
            'model': Error,
            'description': 'Not Found'
        },
    }
)
def service_binding_delete(
        x_broker_api_version: str = api_version,
        x_broker_api_originating_identity: str = originating_identity,
        instance: str = instance_id,
        binding: str = binding_id,
        service: str = service_id,
        plan: str = plan_id,
):
    pass
