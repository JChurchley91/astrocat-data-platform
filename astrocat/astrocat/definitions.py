from dagster import Definitions
from astrocat.assets.bronze_assets import test_asset_1, test_asset_2
from astrocat.jobs.bronze_jobs import asset_job_1, asset_job_2


defs = Definitions(assets=[test_asset_1, test_asset_2], jobs=[asset_job_1, asset_job_2])
