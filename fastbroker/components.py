import jsonschema
from fastapi import Header, Query, Path
from pydantic import BaseModel, Schema, StrictBool, validator
from typing import List
from enum import Enum


class Error(BaseModel):
    type: str
    description: str
    instance_usable: StrictBool = Schema(None)
    update_repeatable: StrictBool = Schema(None)


instance_id = Path(
    default=..., title="Instance Id", description="instance id of instance"
)

binding_id = Path(
    default=..., title="Binding Id", description="Binding id of service binding"
)

accepts_incomplete = Query(
    default=None,
    title="Accepts Incomplete",
    description="Asynchronous operations supported",
)

service_id = Query(
    default=...,
    title="Service Id",
    description="id of the service associated with the instance",
)

plan_id = Query(
    default=...,
    title="Plan Id",
    description="id of the plan associated with the instance",
)

operation_id = Query(
    default=...,
    title="Operation Id",
    description="a provided identifier for the operation",
)

api_version = Header(
    default="2.13",
    title="X-Broker-API-Version",
    description="version number of the Service Broker API that the Platform will use",
)

originating_identity = Header(
    default=None,
    title="X-Broker-API-Originating-Identity",
    description="identity of the user that initiated the request from the Platform",
)


class ModeEnum(str, Enum):
    read = "r"
    readwrite = "rw"


class ProtocolEnum(str, Enum):
    tcp = "tcp"
    udp = "udp"
    all = "all"


class DeviceTypeEnum(str, Enum):
    shared = "shared"


class StateEnum(str, Enum):
    in_progress = "in progress"
    failed = "failed"
    succeeded = "succeeded"


class LastOperationResource(BaseModel):
    state: StateEnum
    description: str = Schema(None)
    instance_usable: StrictBool = Schema(None)
    update_repeatable: StrictBool = Schema(None)


class AsyncOperation(BaseModel):
    operation: str


class ServiceRequest(BaseModel):
    context: dict = Schema(None)
    service_id: str
    plan_id: str
    parameters: dict = Schema(None)


class ServiceInstancePreviousValues(BaseModel):
    service_id: str = Schema(None)
    organization_id: str = Schema(None)
    space_id: str = Schema(None)


class ServiceInstanceUpdateRequest(ServiceRequest):
    previous_values: ServiceInstancePreviousValues


class ServiceInstanceProvisionRequest(ServiceRequest):
    organization_guid: str
    space_guid: str


class ServiceInstanceAsyncOperation(AsyncOperation):
    dashboard_url: str = Schema(None)


class ServiceInstanceProvisionResponse(BaseModel):
    dashboard_url: str = Schema(None)


class ServiceInstanceResource(BaseModel):
    service_id: str = Schema(None)
    plan_id: str = Schema(None)
    dashboard_url: str = Schema(None)
    parameters: dict = Schema(None)


class ServiceBindingVolumeMountDevice(BaseModel):
    volume_id: str
    mount_config: dict = Schema(None)


class ServiceBindingVolumeMount(BaseModel):
    driver: str
    container_dir: str
    mode: ModeEnum
    device_type: DeviceTypeEnum
    device: ServiceBindingVolumeMountDevice


class ServiceBindingEndpoint(BaseModel):
    host: str
    ports: List[str]
    protocol: ProtocolEnum = ProtocolEnum.tcp


class ServiceBindingResponse(BaseModel):
    credentials: str = Schema(None)
    syslog_drain_url: str = Schema(None)
    route_service_url: str = Schema(None)
    volume_mounts: List[ServiceBindingVolumeMount] = Schema(None)
    endpoints: List[ServiceBindingEndpoint] = Schema(None)


class ServiceBindingResource(ServiceBindingResponse):
    parameters: dict = Schema(None)


class ServiceBindingResourceObject(BaseModel):
    app_guid: str = Schema(None)
    route: str = Schema(None)


class ServiceBindingRequest(ServiceRequest):
    app_guid: str = Schema(None)
    bind_resource: ServiceBindingResourceObject


class CatalogObject(BaseModel):
    name: str
    id: str
    description: str
    bindable: StrictBool
    metadata: dict = Schema(None)


class MaintenanceInfo(BaseModel):
    version: str
    description: str = Schema(None)


class SchemaParameters(BaseModel):
    parameters: dict

    @validator("parameters")
    def json_schema(cls, v):
        jsonschema.draft4_format_checker.check(v)


class ServiceBindingSchema(BaseModel):
    create: SchemaParameters = Schema(None)


class ServiceInstanceSchema(BaseModel):
    create: SchemaParameters = Schema(None)
    update: SchemaParameters = Schema(None)


class Schemas(BaseModel):
    service_instance: ServiceInstanceSchema = Schema(None)
    service_binding: ServiceBindingSchema = Schema(None)


class DashboardClient(BaseModel):
    id: str = Schema(None)
    secret: str = Schema(None)
    redirect_uri: str = Schema(None)


class Plan(CatalogObject):
    maintenance_info: MaintenanceInfo = Schema(None)
    free: StrictBool = True
    schemas: Schemas


class Service(CatalogObject):
    tags: List[str]
    requires: List[str] = Schema(None)
    dashboard_client: DashboardClient = Schema(None)
    plan_updateable: StrictBool = Schema(None)
    plans: List[Plan]


class Catalog(BaseModel):
    services: List[Service]
