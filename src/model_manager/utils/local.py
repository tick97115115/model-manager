from typing import List
from anyio import Path, open_file

def remove_safetensors_suffix(input_string: str) -> str:
    # Check if the string ends with ".safetensors"
    if input_string.endswith(".safetensors"):
        # Remove the ".safetensors" suffix
        return input_string[:-len(".safetensors")]
    # If it doesn't end with ".safetensors", return the original string
    return input_string

async def get_info_json_relate_to_safetensors_file(safetensors_file: Path) -> Path:
    info_json_path_str = remove_safetensors_suffix(safetensors_file.__str__()) + ".info.json"
    info_json_path = Path(info_json_path_str)
    if info_json_path.exists():
        return info_json_path
    raise FileNotFoundError(f"info.json file not found for {safetensors_file}")

async def get_api_info_json_relate_to_safetensors_file(safetensors_file: Path) -> Path:
    info_json_path_str = remove_safetensors_suffix(safetensors_file.__str__()) + ".api_info.json"
    info_json_path = Path(info_json_path_str)
    if info_json_path.exists():
        return info_json_path
    raise FileNotFoundError(f"api_info.json file not found for {safetensors_file}")

async def get_preview_img_relate_to_safetensors_file(safetensors_file: Path) -> Path:
    safetensors_file_folder = safetensors_file.parent
    safetensors_file_name = remove_safetensors_suffix(safetensors_file.name)
    search_pattern = Path.joinpath(safetensors_file_folder, f"{safetensors_file_name}.preview.*")
    async for entry in safetensors_file_folder.iterdir():
        if entry.match(search_pattern.__str__()):
            return entry

    raise FileNotFoundError(f"preview image file not found for {safetensors_file}")

async def get_file_ctime(file: Path) -> float:
    st = await file.stat()
    return st.st_birthtime

class CardNode:
    def __init__(self, safetensors_file: Path):
        self.safetensors_file = safetensors_file

    async def get_info_json(self) -> Path:
        return await get_info_json_relate_to_safetensors_file(self.safetensors_file)

    async def get_api_info_json(self) -> Path:
        return await get_api_info_json_relate_to_safetensors_file(self.safetensors_file)

    async def get_preview_img(self) -> Path:
        return await get_preview_img_relate_to_safetensors_file(self.safetensors_file)
    
    async def get_ctime(self) -> float:
        return await get_file_ctime(self.safetensors_file)

