from typing import Set, List, Dict

from sqlalchemy.sql.schema import Table, Column

from pancaim_cdm import pancaim_orm as cdm
from pancaim_cdm.pancaim_orm import CDM_SCHEMA

# Column name suffix indicating it holds raw source data values
RAW_VALUE_SUFFIX = "raw_value"

# Only tables from the CDM schema should be exported
TABLES_TO_EXPORT: List[Table] = [
    table for table in cdm.Base.metadata.tables.values() if table.schema == CDM_SCHEMA
]

# Complete list of columns to be exported
COLUMNS_TO_EXPORT: List[Column] = [
    column
    for table in TABLES_TO_EXPORT
    for column in table.columns
    if not column.name.endswith(RAW_VALUE_SUFFIX)
]

# Maximum number of slots per category that will be in the final JSON
MAX_SLOTS: Dict = {
    'person': 1,
    'body_measurement': 1,
    'lab': 15,
    'lab2': 25,
    'prognosis': 1,
    'surgery': 3,
    'therapy': 2,
    'tumor': 10,
}

# Name of the field that has the date for each table
DATE_FIELDS: Dict = {
    'person': 'date_of_interview',
    'body_measurement': 'body_measurement_date',
    'lab': 'lab_date',
    'lab2': 'lab2_date',
    'prognosis': 'prognosis_date',
    'surgery': 'date_of_surgery',
    'therapy': 'date_start_adjuvant_chemotherapy',
    'tumor': 'tumor_date',
}


# controlled_term_cols: Set[str] = {
#     f"{cdm.Person.__tablename__}.{cdm.Person.sex.name}",
#     f"{cdm.Person.__tablename__}.{cdm.Person.vital_status.name}",
#     f"{cdm.Surgery.__tablename__}.{cdm.Surgery.surgery_purpose.name}",
#     f"{cdm.Surgery.__tablename__}.{cdm.Surgery.surgical_technique.name}",
# }
