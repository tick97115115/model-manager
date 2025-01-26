import pytest
from os.path import join, dirname

# This is the same as using the @pytest.mark.anyio on all test functions in the module
pytestmark = pytest.mark.anyio

async def test_something():
    safesensors_file = join(dirname(dirname(__file__)), 'Ken_Ashcorp_k3n_illus-000008_1205058.safetensors')
    from model_manager.utils.model import async_extract_header_from_safesensors
    result = await async_extract_header_from_safesensors(safesensors_file)
    assert isinstance(result, str)