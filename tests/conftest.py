import os
import glob
import pytest
from typing import List, Dict
from pydantic import FilePath

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, drop_database
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker

from pancaim_cdm import pancaim_orm as cdm

import pandas as pd


def create_cdm_tables(connection: Connection, schemas: List[str]) -> None:
    """Create all schemas and CDM tables."""
    for schema in schemas:
        connection.execute(f"CREATE SCHEMA IF NOT EXISTS {schema};")
    cdm.Base.metadata.create_all(bind=connection)


def load_records_to_db(session: Session, orm_objects: List) -> None:
    session.add_all(orm_objects)
    session.commit()


@pytest.fixture()
def test_data_dir() -> str:
    """Returns the path to the test_data dir"""
    cur_dir = os.path.dirname(__file__)
    return os.path.join(cur_dir, 'resources', 'test_data')


@pytest.fixture()
def test_results_dir() -> str:
    """Returns the path to the test_results dir"""
    cur_dir = os.path.dirname(__file__)
    return os.path.join(cur_dir, 'resources', 'test_results')


@pytest.fixture()
def synth_data_files(test_data_dir) -> Dict[str, str]:
    """Returns a dict with synthetic data files (csv) to load to tables. key=table_name, value=file_path"""
    files = {}
    for cur_file in glob.glob(os.path.join(test_data_dir, '*.csv')):
        if cur_file.endswith('person.csv') or cur_file.endswith('Person.csv'):
            files['Person'] = cur_file
        elif cur_file.endswith('surgery.csv') or cur_file.endswith('Surgery.csv'):
            files['Surgery'] = cur_file
    return files


@pytest.fixture()
def load_synth_data_to_cdm(synth_data_files: Dict[str, str]) -> List:
    """Reads synthetic CSV data and converts to a list of records (cdm objects)"""
    records = []

    for cur_table, cur_path in synth_data_files.items():
        cur_table_records = pd.read_csv(cur_path, index_col=None).to_dict(orient='records')         # => list of dicts. each row of data is a list element, and columns are dict keys.

        for cur_record in cur_table_records:        # cur_record is dict, with keys=table_fields.
            records.append(create_record(cur_table, cur_record))

    return records


def create_record(table_name: str, record):
    """Converts a dicionary into a cdm object"""
    if table_name == 'Person':
        cur_table = getattr(cdm, 'Person')
    elif table_name == 'Surgery':
        cur_table = getattr(cdm, 'Surgery')

    d = {}
    for field, value in record.items():
        cur_table_field = getattr(cur_table, field)
        cur_table_field_key = getattr(cur_table_field, 'key')

        d[cur_table_field_key] = value

    if table_name == 'Person':
        return cdm.Person(**d)
    elif table_name == 'Surgery':
        return cdm.Surgery(**d)


@pytest.fixture()
def db_session(postgresql):
    """Session for SQLAlchemy."""
    connection_str = f'postgresql+psycopg2://{postgresql.info.user}:@{postgresql.info.host}:{postgresql.info.port}/{postgresql.info.dbname}'

    engine = create_engine(connection_str, echo=False, poolclass=NullPool)
    with engine.connect() as conn:
        create_cdm_tables(conn, schemas=[cdm.CDM_SCHEMA])
        yield sessionmaker(bind=engine, expire_on_commit=False)


@pytest.fixture()
def create_min_database(db_session, load_synth_data_to_cdm) -> None:
    s = db_session()
    load_records_to_db(s, load_synth_data_to_cdm)
