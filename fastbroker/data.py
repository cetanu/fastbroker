from fastbroker.config import DatabaseTypes


class BaseDatastore:
    def get_service_instance(
        self, instance_id: str, service_id: str, plan_id: str
    ) -> dict:
        raise NotImplementedError()  # pragma: no cover

    def create_service_instance(
        self, instance_id: str, service_id: str, plan_id: str, parameters: dict
    ) -> None:
        raise NotImplementedError()  # pragma: no cover

    def delete_service_instance(
        self, instance_id: str, service_id: str, plan_id: str
    ) -> None:
        raise NotImplementedError()  # pragma: no cover

    def upsert_service_instance(
        self, instance_id: str, service_id: str, plan_id, parameters: dict
    ) -> None:
        raise NotImplementedError()  # pragma: no cover

    def update_service_instance(
        self, instance_id: str, service_id: str, plan_id: str, parameters: dict
    ) -> None:
        raise NotImplementedError()  # pragma: no cover

    def get_service_binding(
        self, instance_id: str, binding_id: str, service_id: str, plan_id: str
    ) -> dict:
        raise NotImplementedError()  # pragma: no cover

    def bind_service_instance(
        self,
        instance_id: str,
        binding_id: str,
        service_id: str,
        plan_id: str,
        parameters: dict,
        credentials: dict,
    ) -> None:
        raise NotImplementedError()  # pragma: no cover

    def unbind_service_instance(
        self, instance_id: str, binding_id: str, service_id: str, plan_id: str
    ) -> None:
        raise NotImplementedError()  # pragma: no cover


class InMemoryDatastore(BaseDatastore):
    def __init__(self):
        self.data = dict()

    def get_service_instance(
        self, instance_id: str, service_id: str = None, plan_id: str = None
    ) -> dict:
        instance = self.data[instance_id]
        if service_id is not None:
            assert instance["service_id"] == service_id
        if plan_id is not None:
            assert instance["plan_id"] == plan_id
        return instance

    def create_service_instance(
        self, instance_id: str, service_id: str, plan_id: str, parameters: dict
    ) -> None:
        self.data[instance_id] = {
            "instance_id": instance_id,
            "service_id": service_id,
            "plan_id": plan_id,
            "parameters": parameters,
        }

    def delete_service_instance(
        self, instance_id: str, service_id: str, plan_id: str
    ) -> None:
        self.data.pop(instance_id, None)

    def get_service_binding(
        self,
        instance_id: str,
        binding_id: str,
        service_id: str = None,
        plan_id: str = None,
    ) -> dict:
        binding = self.data[binding_id]
        if service_id is not None:
            assert binding["service_id"] == service_id
        if plan_id is not None:
            assert binding["plan_id"] == plan_id
        return binding

    def bind_service_instance(
        self,
        instance_id: str,
        binding_id: str,
        service_id: str,
        plan_id: str,
        parameters: dict,
        credentials: dict,
    ) -> None:
        self.data[binding_id] = {
            "instance_id": instance_id,
            "binding_id": binding_id,
            "service_id": service_id,
            "plan_id": plan_id,
            "parameters": parameters,
            "credentials": credentials,
        }

    def unbind_service_instance(
        self, instance_id: str, binding_id: str, service_id: str, plan_id: str
    ) -> None:
        self.data.pop(binding_id, None)

    update = create_service_instance
    upsert = create_service_instance


db_mapping = {DatabaseTypes.in_memory: InMemoryDatastore}
