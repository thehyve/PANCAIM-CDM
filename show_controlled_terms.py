#!/usr/bin/env python3

import importlib
import inspect
import sys
from enum import Enum
from pathlib import Path


def _format_value(value: Enum) -> str:
    # extract value from Enum type values
    value = value.value
    # in case the target value contains a comma
    if type(value) is str and ',' in value:
        value = f'"{value}"'
    return value


def show_controlled_terms() -> None:
    target_path = './src/pancaim_cdm/semantic_mapping/controlled_terms'
    target_module = '.'.join(target_path.split('/')[1:])
    # get directory names iteratively
    tables = [table.name for table in Path(target_path).glob('*') if table.is_dir()]
    # remove hidden folders
    tables = [table for table in tables if not table.startswith(('_', '.', '~'))]
    print(f'table,field,controlled term')
    for table in tables:
        # import modules iteratively
        import_module = importlib.import_module(f'{target_module}.{table}')
        # discard everything that is not an Enum object
        enums = [cls for name, cls in import_module.__dict__.items()
                 if inspect.isclass(cls) and issubclass(cls, Enum)]
        for enum in enums:
            field = enum.__name__
            for controlled_term in enum:
                print(f'{table},{field},{_format_value(controlled_term)}')


if __name__ == "__main__":
    sys.exit(show_controlled_terms())
