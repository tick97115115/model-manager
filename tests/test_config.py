import pytest
from src.model_manager.config import Settings, save_settings, load_settings

# This is the same as using the @pytest.mark.anyio on all test functions in the module
pytestmark = pytest.mark.anyio

@pytest.fixture
def settings():
    return Settings()

def test_load_settings(settings):
    load_settings()

def test_save_settings(settings):
    save_settings(settings)

