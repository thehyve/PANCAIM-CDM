from datetime import datetime
from enum import Enum
from typing import Dict, Optional, Union

import pandas as pd
from sqlalchemy import Column

from pancaim_cdm.semantic_mapping.unmapped_value import UNMAPPED_VALUE


class SemanticMapper:
    """
    Collection of semantic mappings for a given target model field.

    Attributes
    ----------
    field: Column
        PANCAIM CDM column definition (e.g. Person.sex). This
        parameter is needed to check if the column is nullable.
    semantic_mappings: dict[str, Enum]
        Dictionary of source value : target value mappings.
    date_formats: dict[str, Enum]
        Dictionary of source date format : target date format mappings
        (only applicable to date fields).
    """

    def __init__(self,
                 field: Column,
                 semantic_mappings: Optional[Dict[Optional[str],
                                                  Union[Enum, int, str, None]]] = None,
                 date_formats: Optional[Dict[str, Enum]] = None):
        self.field_name = field.name
        self.nullable = field.nullable
        self.placeholder_value = UNMAPPED_VALUE if self._map_to_placeholder(field) else None
        self.semantic_mappings = semantic_mappings
        self.date_formats = date_formats

    @staticmethod
    def _clean_value(value) -> Optional[str]:
        # return null values (nan, None, '') as None
        # return non-null values as string (stripped of spaces)
        if pd.isnull(value):
            return None
        value = str(value).strip()
        return value if value != '' else None

    @staticmethod
    def _format_datetime(date: str, input_format: str, output_format: str) \
            -> Optional[str]:
        # Parse input datetime and return using specified output format.
        # Input and output format should use supported datetime syntax,
        # see: https://strftime.org/
        try:
            date = str(date)
            valid_date = datetime.strptime(date, input_format)
            return valid_date.strftime(output_format)
        except ValueError:
            return None

    @staticmethod
    def _map_to_placeholder(field: Column) -> bool:
        if str(field.type) == 'TEXT':
            raw_col_name = field.name + '_raw_value'
            if raw_col_name in field.table.columns:
                return True
        return False

    def lookup(self, source_value: Optional[str]) -> Union[None, str, int]:
        """
        Map source value to target value.

        Parameters
        ----------
        source_value: str
            Value to map.

        Returns
        -------
        Mapped value (typically string or integer), or None.
        """
        source_value = self._clean_value(source_value)
        # try to map the value (applies to all field types)
        mapping_available = False
        mapped_value = None
        if source_value in self.semantic_mappings:
            mapping_available = True
            mapped_value = self.semantic_mappings.get(source_value)
            mapped_value = mapped_value.value if isinstance(mapped_value, Enum) else mapped_value
        # date field
        if self.field_name.endswith('date'):
            if mapping_available:
                date_value = mapped_value
            else:
                date_value = source_value
            if date_value is None:
                return date_value
            for input_format, output_format in self.date_formats.items():
                output_format = str(output_format.value)
                formatted_date = self._format_datetime(date_value, input_format, output_format)
                if formatted_date is not None:
                    return formatted_date
            return self.placeholder_value
        # controlled term field (non-nullable)
        if self.placeholder_value and not self.nullable:
            if mapping_available and mapped_value is not None:
                return mapped_value
            return self.placeholder_value
        # controlled term field (nullable)
        if self.placeholder_value and self.nullable:
            if mapping_available:
                return mapped_value
            return None if source_value is None else self.placeholder_value
        # other fields (e.g. numeric)
        return mapped_value
