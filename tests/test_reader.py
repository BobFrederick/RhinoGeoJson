from geojsontools import *
import pytest

#TODO test multiple urls.
@pytest.fixture
def url():
    "returns test url"
    return r'https://opendata.arcgis.com/datasets/674f80b8edee4bf48551512896a1821d_0.geojson'

def test_imports():
    """ test package imports """
    assert geometry is not None
    assert reader is not None

def test_from_url(url):
    """ Tests loading data from url """
    data = reader.Reader(url).data
    assert len(data) > 0

#TODO test url validation