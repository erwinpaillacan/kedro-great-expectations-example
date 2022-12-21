import logging
from typing import Any, Dict

import great_expectations as ge
from kedro.framework.hooks import hook_impl
from kedro.io import DataCatalog


logger = logging.getLogger(__name__)


class DataValidationHooks:
    def __init__(self):
        self.dataset_expectation_mapping = None
        self.context_root_dir = None

    @hook_impl
    def after_catalog_created(self, catalog: DataCatalog):
        self.dataset_expectation_mapping = catalog.load(
            "params:great_expectations.checkpoint_mapper"
        )
        self.context_root_dir = catalog.load(
            "params:great_expectations.context_root_dir"
        )

    @hook_impl
    def before_dataset_saved(self, dataset_name: str, data: Any) -> None:
        """Validate outputs data from a node based on using great expectation
        if an expectation suite is defined in ``dataset_expectation_mapping``.
        """
        self._run_validation(dataset_name, data)

    def _run_validation(self, dataset_name: str, data: Any):
        """
        It runs a validation checkpoint on the data, using the expectation suite specified in the
        mapping

        Args:
          dataset_name (str): The name of the dataset you want to validate.
          data (Any): The data to be validated.
        """
        if dataset_name in self.dataset_expectation_mapping:

            expectation_context = ge.data_context.DataContext(
                context_root_dir=self.context_root_dir
            )
            checkpoint_name = self.dataset_expectation_mapping[dataset_name]

            expectation_context.run_checkpoint(
                checkpoint_name=checkpoint_name,
                batch_request={
                    "runtime_parameters": {"batch_data": data},
                    "batch_identifiers": {
                        "default_identifier_name": "pandas_dataframe"
                    },
                },
            )
