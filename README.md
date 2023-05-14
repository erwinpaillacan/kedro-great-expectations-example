# Minimal example Kedro with GE v3.0 API (Python 3.10)

If you have conda you can use the make file to install the environment.
```bash
make install
conda activate kedro-ge-example
```

Then you can execute:

```bash
(kedro-ge-example) kedro run
```

The file `data/08_reporting/great_expectations/data_docs/local_site/index.html` will contain a html great expectations report. 

In `conf/base/parameters/great_expectations_hook.yml` you can find some parameters of the hook.
The validation also works with in memory datasets [you can try commenting the catalog entry of `preprocessed_companies`]


There is a sample notebook in `notebooks/great_expectations_starter.ipynb` to create expectations:

```bash
(kedro-ge-example) kedro jupyter notebook
```