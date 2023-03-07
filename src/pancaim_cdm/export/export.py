"""Independent module for exporting CDM tables"""

import logging
from contextlib import contextmanager
from typing import List, ContextManager, Dict, Union, Callable

from sqlalchemy import update, or_
from sqlalchemy.engine import Engine
from sqlalchemy.schema import CreateSchema, DropSchema
from sqlalchemy.sql.schema import Table, Column

from pancaim_cdm.export.database import Database
from pancaim_cdm.export.export_models import ExportConfig
from pancaim_cdm import pancaim_orm as cdm
from pancaim_cdm.export.write import ExportWriter

logger = logging.getLogger(__name__)


def export_cdm_tables(config: ExportConfig) -> None:
    """
    Export all tables in the CDM schema to output files.

    Columns that contain the raw values are excluded from the export.
    Any existing files in the export folder will be overwritten.

    Certain data can be masked/excluded from export, depending on what
    is specified in the config.

    Parameters
    ----------
    config : ExportConfig
        Config instance containing all information on how the data
        export should be performed.

    Returns
    -------
    None
    """
    db = Database.from_config(config)

    export_writer = ExportWriter(export_root=config.export_folder)
    export_writer.export_tables(
        export_schema=cdm.CDM_SCHEMA,
        db=db,
    )
