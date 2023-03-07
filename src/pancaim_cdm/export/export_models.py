import pytest
from typing import Optional, Dict, Union, List

from pydantic import (
    BaseModel,
    validator,
    SecretStr,
    DirectoryPath,
    StrictInt,
    StrictStr,
)


class _DataBase(BaseModel):
    drivername: Optional[str]
    host: str
    port: int
    database_name: str
    username: str
    password: Optional[SecretStr]
    query: Optional[Dict[str, str]]

    @validator("drivername", always=True)
    def missing_drivername(cls, drivername):
        # Set postgresql as the default driver
        return drivername or "postgresql"

    @validator("password", always=True)
    def missing_password(cls, password):
        if password is None:
            password = SecretStr("")
        return password


class ExportConfig(BaseModel):
    """Data schema and validator of the export config properties."""

    database: _DataBase
    cdm_schema: str
    export_folder: DirectoryPath
