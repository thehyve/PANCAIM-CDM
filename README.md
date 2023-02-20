# PANCAIM-CDM
PANCAIM Common Data Model

### Installing for developers

The `pancaim-cdm` package is already included as a dependency in site-specific ETLs developed 
within PANCAIM. To install the package locally for development purposes, do the following:
```bash
git clone https://github.com/thehyve/PANCAIM-CDM.git
cd pancaim-cdm

# install in editable mode (including test dependencies)
pip install -e '.[TEST]'
```

### Updating the data model

The data model in `src/pancaim_cdm/pancaim_orm.py` specifies table and field names and properties.
You can update the data model using the 
[SQLAlchemy ORM syntax](https://docs.sqlalchemy.org/en/14/orm/quickstart.html).

Make sure to update the model version at the top of `src/pancaim_cdm/pancaim_orm.py`!

### Updating the controlled values

The allowed values for the data model fields are in `src/pancaim_cdm/semantic_mapping`.

This includes:
- `controlled_terms` for specific fields.
- a `date_format` shared between all date fields.
- a placeholder value in `unmapped_value.py`, used when a source value in a non-nullable field 
  cannot be mapped.

### Updating the general mapping logic

How controlled terms, date formats, and the default unmapped value are used is controlled in the 
`SemanticMapper` class - see: `src/pancaim_cdm/semantinc_mapping/semantic_mapper.py`.

### Updating the export configuration settings

The export configuration structure and constraints are defined in the  
`ExportConfig` class - see: `src/pancaim_cdm/export/export_config_model.py`.

### Testing changes

Simply execute the following from the project root to detect and execute tests in the `tests` 
folder:

```bash
python -m pytest
```

### Creating a new package release

Update the package version in `setup.cfg`.
Major and minor version should match the PANCAIM model version;
micro versions are used for changes that are independent of the model (e.g. bug fixes).

After committing your changes, execute the following from the project root:

```bash
# remove previous release folder
rm -rf dist

# create the new release
pip install --quiet build
python -m build
```

Create a new PANCAIM CDM release on GitHub and manually add the files generated in 
the `dist/` folder to the release assets. 

To update the dependent PANCAIM ETLs:
Add the `.whl` file to the `dependencies` folder of each repository,
and update the `requirements.txt` files accordingly.


### Review existing controlled terms
For your convenience, we provide a command to generate an overview of current controlled terms,
making it unnecessary to navigate into the code structure.

Run the following command from the project root:

```bash
python ./show_controlled_terms.py
```

All current controlled terms will be printed to the screen in a CSV-compatible format.
