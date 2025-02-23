import os
import struct
from typing import Any, Coroutine, List
from anyio import Path, open_file

async def async_extract_header_from_safetensors(file: str) -> str:
    async with await open_file(file, 'rb') as f:
        # Read 8 bytes from the file (64-bit = 8 bytes)
        header_length = await f.read(8)

        # Unpack the bytes into an unsigned little-endian 64-bit integer
        if len(header_length) == 8:
            uint64_value: int = struct.unpack('<Q', header_length)[0]
            # return uint64_value
            await f.seek(8)
            header_data = await f.read(uint64_value)
            header_str = header_data.decode('utf-8')
            return header_str
        else:
            raise ValueError("Not enough data to read a 64-bit integer.")

def find_files_with_string(directory, search_string) -> List[str]:
    """
    Find files in the specified directory that contain the search string in their names.
    Does not search sub-directories.

    :param directory: The directory to search in.
    :param search_string: The string to search for in file names.
    :return: A list of file paths that match the search string.
    """
    matching_files: List[str] = []
    # List all files in the directory (not sub-directories)
    for filename in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        # Check if it's a file (not a directory) and contains the search string
        if os.path.isfile(file_path) and search_string in filename:
            matching_files.append(file_path)
    return matching_files


