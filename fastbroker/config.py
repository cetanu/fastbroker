from enum import Enum
from pydantic import BaseModel


class DatabaseTypes(str, Enum):
    in_memory = "in_memory"
    dynamo_db = "dynamo_db"
    mysql = "mysql"
    mongo = "mongo"


class DatabaseConfig(BaseModel):
    type: DatabaseTypes


class FastBrokerConfig(BaseModel):
    database: DatabaseConfig
