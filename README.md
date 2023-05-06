# Minimal example Kedro with GE v3.0 API (Python 3.10)

If you have conda you can use the make file to install the environment.
```bash
make install
conda activate kedro-ge-example
```

Download this data <https://kedro-org.github.io/kedro/companies.csv>
and save it in `data/01_raw`

Then you can execute:

```bash
kedro run
```

The folder `data/08_reporting/great_expectations` you will find a great expectations report

In `conf/base/parameters/great_expectations_hook.yml` you can find some parameters of the hook.
The validation works with in memory datasets [you can try commenting the catalog entry of `preprocessed_companies`]