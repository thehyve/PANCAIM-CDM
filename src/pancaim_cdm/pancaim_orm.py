from dataclasses import dataclass
from types import SimpleNamespace

from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

CDM_SCHEMA = 'cdm_schema'


# These table classes are used to have only one place where the table
# and field names are captured. If a name of a table or field needs to
# change, it can be done so by updating the field string and not the
# variable name. That way the ETL repos using this CDM will not have to
# be updated in case of a name change.
@dataclass
class Table:
    name: str
    fields: SimpleNamespace


_person = Table(
    name='person',
    fields=SimpleNamespace(
        pancaim_id='pancaim_id',
        sex='sex',
        pancaim_id_raw_value='pancaim_id_raw_value',
        sex_raw_value='sex_raw_value'
    )
)


class Person(Base):
    __tablename__ = _person.name
    __table_args__ = {'schema': CDM_SCHEMA}

    pancaim_id = Column(Integer, primary_key=True, name=_person.fields.pancaim_id)
    sex = Column(Text, nullable=False, name=_person.fields.sex)
    pancaim_id_raw_value = Column(Text, name=_person.fields.pancaim_id_raw_value)
    sex_raw_value = Column(Text, name=_person.fields.sex_raw_value)
