from dagster import Definitions
from astrocat.assets.bronze_assets import test_asset_1, test_asset_2
from astrocat.jobs.bronze_jobs import asset_job_1, asset_job_2
from astrocat.jobs.config_jobs import (
    create_astrocat_config_schema,
    create_astrocat_config_table,
)


defs = Definitions(
    assets=[test_asset_1, test_asset_2],
    jobs=[
        create_astrocat_config_schema,
        create_astrocat_config_table,
        asset_job_1,
        asset_job_2,
    ],
)
