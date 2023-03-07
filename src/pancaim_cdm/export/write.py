import logging
import json
import time
from pathlib import Path
from typing import List, Dict

from datetime import date, datetime

from sqlalchemy import Table
from sqlalchemy.engine import Engine

from pancaim_cdm.export.constants import RAW_VALUE_SUFFIX
from pancaim_cdm.export.database import Database
from pancaim_cdm.export.constants import MAX_SLOTS
from pancaim_cdm.export.constants import DATE_FIELDS

from pancaim_cdm.pancaim_orm import Person

logger = logging.getLogger(__name__)


def get_columns_to_export(table: Table) -> List[str]:
    """Get all non-raw value column names of table."""
    return [
        c.name
        for c in table.columns
        if not c.name.lower().endswith(RAW_VALUE_SUFFIX)
    ]


def json_custom_default(obj):
    """Will stringify dates, and keep everything else the same"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


class ExportWriter:
    def __init__(self, export_root: Path):
        self._time_string = time.strftime("%Y-%m-%dT%H%M%S")
        self._export_root = export_root

    @property
    def export_dir(self) -> Path:
        """Directory containing the output."""
        return self._export_root / self._time_string

    def export_tables(self, export_schema: str, db: Database) -> None:
        """Export all tables in export_schema to output files."""
        self.export_dir.mkdir()
        tables: List[Table] = db.get_reflected_metadata(export_schema).tables.values()

        person_table = db.get_reflected_metadata(export_schema).tables[f'{export_schema}.{Person.__tablename__}']           # is there a better way to refer to person table name?

        # get ids to query
        ids_to_query = self.get_ids_to_query(db.engine, person_table)

        for cur_id in ids_to_query:
            f_path = self.export_dir / f"{cur_id}.json"
            data = dict()

            for table in tables:
                columns_to_export = get_columns_to_export(table)                        # removes raw_value columns
                table_data = self.save_table_to_list_of_dicts(db.engine, table, columns_to_export, cur_id)
                data[table.name] = table_data
            self.write_json_to_file(data, f_path)

    @staticmethod
    def get_ids_to_query(engine: Engine, table: Table) -> List:
        """Will query Person table to get all unique pancaim_ids"""
        sql = f"SELECT DISTINCT {Person.pancaim_id.name} FROM {table.fullname};"

        with engine.connect() as conn:
            results = conn.execute(sql)

        ids_to_query = [cur_entry[Person.pancaim_id.name] for cur_entry in results.mappings()]

        return ids_to_query

    @staticmethod
    def save_table_to_list_of_dicts(engine: Engine, table: Table, columns: List[str], cur_id: int) -> List[Dict]:
        """Export DB table to a list of dictionaries where each dictionary is a row/entry from the table"""
        logger.info(f"Exporting {table.name} to dictionary.")
        columns = ", ".join(columns)
        sql = f"SELECT {columns} FROM {table.fullname} WHERE {Person.pancaim_id.name} = {cur_id} ORDER BY {DATE_FIELDS[table.name]} DESC LIMIT {MAX_SLOTS[table.name]}"                  # descending order = most recent first

        with engine.connect() as conn:
            results = conn.execute(sql)

        results = [dict(entry) for entry in results.mappings()]         # convert RowMappings to dicts
        conn.close()
        return results

    @staticmethod
    def write_json_to_file(data: Dict, path: Path) -> None:
        """Dumps dictionary to a file."""
        with open(path, 'w') as f:
            json.dump(data, f, default=json_custom_default, indent=4)
