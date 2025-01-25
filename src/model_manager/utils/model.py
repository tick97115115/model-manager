import struct
from typing import Any, Coroutine
from anyio import Path, open_file

async def extract_header_from_safesensors(file: str) -> Coroutine[Any, Any, str]:
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
        