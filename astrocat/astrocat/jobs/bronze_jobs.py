from dagster import define_asset_job

asset_job_1 = define_asset_job(
    name="test_asset_job_1", description="test_asset_1 job", selection="test_asset_1"
)

asset_job_2 = define_asset_job(
    name="test_asset_job_2", description="test_asset_2 job", selection="test_asset_2"
)
