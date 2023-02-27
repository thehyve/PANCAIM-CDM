import json
import sys

from pancaim_cdm.export.write import CustomJSONEncoder


if __name__ == "__main__":
    data = {
        'Person': {'item 0': {'pancaim_id': 1234,
                              'field2': None,
                              'another_field': 'data'},
                   },
        'Lab': {'item 0': {'lab_id': 'lorem',
                           'date': 'ipsum'},
                'item 1': {'lab_id': 'dolor',
                           'date': 'sit'},
                },
        'Surgery': {},
        'Tumor': {'item 0': {'tumor_id': 'amet',
                             'date': 'consecteur'},
                  'item 1': {'tumor_id': 'adipiscing',
                             'date': 'elit'},
                  }
    }

    json.dump(data, sys.stdout, cls=CustomJSONEncoder)

    exit()
