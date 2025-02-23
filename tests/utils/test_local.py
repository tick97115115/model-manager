import pytest
from os.path import join, dirname
from anyio import Path
from src.model_manager.utils.local import CardNode

# This is the same as using the @pytest.mark.anyio on all test functions in the module
pytestmark = pytest.mark.anyio

async def test_get_card_node():
    lora = r"D:\AI_Drawer\webui_forge\webui\models\Lora\playing with own hair_XL_illustrious_V1.0.safetensors"
    lora_node = CardNode(Path(lora))
    preview_img = await lora_node.get_preview_img()
    assert preview_img.exists()

    api_info_json = await lora_node.get_api_info_json()
    assert api_info_json.exists()

    info_json = await lora_node.get_info_json()
    assert info_json.exists()