import pytest
import os
import glob
import filecmp
from typing import Dict

from pancaim_cdm.export.export import export_cdm_tables
from pancaim_cdm.export.export_models import ExportConfig

from pancaim_cdm import pancaim_orm as cdm

pytestmark = pytest.mark.usefixtures("create_min_database")


@pytest.fixture()
def default_export_config(postgresql) -> Dict:
    return {
        'database': {
            'drivername': 'postgresql',
            'host': postgresql.info.host,
            'port': postgresql.info.port,
            'database_name': postgresql.info.dbname,
            'username': postgresql.info.user,
            'password': postgresql.info.password,
        },
        'cdm_schema': cdm.CDM_SCHEMA,
        'export_folder': './export_test',
    }


def test_export_json(default_export_config: Dict, test_results_dir):
    """Will use filecmp to compare the content of the export test, and test_files provided"""
    if not os.path.exists(default_export_config['export_folder']):
        os.mkdir(default_export_config['export_folder'])

    export_config = ExportConfig(**default_export_config)
    export_cdm_tables(export_config)

    # get files to compare against
    test_files = glob.glob(os.path.join(test_results_dir, '*.json'))
    test_files = {os.path.basename(n): n for n in test_files}               # convert to dict: filename:file_path

    # this function does not know the name of the folder where the results of this test are located. So just select most recently created folder
    export_folder = [n for n in glob.glob(os.path.join(default_export_config['export_folder'], '*')) if os.path.isdir(n)]       # list dir in the export_dir
    export_folder = max(export_folder, key=os.path.getctime)                                                                    # this is the latest dir in the export_dir

    for cur_filename in test_files.keys():
        test_file = os.path.join(test_results_dir, cur_filename)
        exported_file = os.path.join(export_folder, cur_filename)

        assert filecmp.cmp(test_file, exported_file)
