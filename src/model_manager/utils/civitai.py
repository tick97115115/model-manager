from httpx import AsyncClient
from gospeed_api.index import AsyncGospeedClient as AsyncGopeedClient
from civitai_api.api import CivitaiAPI as AsyncCivitaiClient



class CivitAI:
    def __init__(self, api_key: str, gopeed_address: str, proxy) -> None:
        self.api_key = api_key
        self.async_httpx_client = AsyncClient(headers={"Authorization": f"Bearer {api_key}"} ,proxy=proxy)
        self.async_gopeed_client = AsyncGopeedClient(api_key, proxy)
        self.async_civitai_client = AsyncCivitaiClient(api_key, proxy)
