from astrocat.utils.test_utils import test
from dagster import asset


@asset
def test_asset_1():
    return test()


@asset
def test_asset_2():
    return test()
