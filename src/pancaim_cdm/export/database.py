"""Database operations module."""

from __future__ import annotations

import logging
from getpass import getpass
from typing import Union

from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import URL, Engine
from sqlalchemy.exc import SQLAlchemyError

from pancaim_cdm import pancaim_orm as cdm
from pancaim_cdm.export.export_models import ExportConfig

logger = logging.getLogger(__name__)


class Database:
    """
    Handler for all interactions with the database.

    Parameters
    ----------
    uri : str
        Database URI for creating the SQLAlchemy engine.
    cdm_schema : str
        Name of the CDM schema.

    Attributes
    ----------
    engine : sqlalchemy.engine.base.Engine
        Database engine.
    """

    def __init__(self, uri: URL, cdm_schema: str):
        self.engine: Engine = create_engine(
            uri,
            execution_options={"schema_translate_map": {cdm.CDM_SCHEMA: cdm_schema}},
        )

    @classmethod
    def from_config(cls, config: ExportConfig) -> Database:
        """
        Create an instance of Database from a configuration file.

        Parameters
        ----------
        config : ExportConfig
            Contents of the configuration file.

        Returns
        -------
        Database
        """
        db_config = config.database
        password = db_config.password.get_secret_value()
        url = URL.create(
            drivername=db_config.drivername,
            host=db_config.host,
            port=db_config.port,
            database=db_config.database_name,
            username=db_config.username,
            password=password,
            query=db_config.query,
        )
        if not password and not Database._can_connect_without_password(url):
            url = url.set(password=getpass("Database password:"))
        return cls(uri=url, cdm_schema=config.cdm_schema)

    @staticmethod
    def _can_connect_without_password(uri: URL) -> bool:
        logger.info("Attempting to connect without password")
        logger.disabled = True
        can_connect = Database.can_connect(uri)
        logger.disabled = False
        return can_connect

    @staticmethod
    def can_connect(uri: Union[str, URL]) -> bool:
        """
        Check whether a connection can be established for the given URI.

        Parameters
        ----------
        uri : str or SQLAlchemy URL
            Database URI including database name.

        Returns
        -------
        bool
            Returns True if connection to database could be established.
        """
        try:
            create_engine(uri).connect()
        except SQLAlchemyError as e:
            logger.error(e, exc_info=True)
            return False
        else:
            return True

    def get_reflected_metadata(self, schema: str) -> MetaData:
        metadata = MetaData(bind=self.engine)
        metadata.reflect(schema=schema, resolve_fks=True)
        return metadata
