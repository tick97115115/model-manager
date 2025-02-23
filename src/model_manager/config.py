from pydantic_settings import BaseSettings
from pydantic import Field
from os.path import join, dirname, exists
import json

config_file = join(dirname(__file__), '.settings.json')

class Settings(BaseSettings):
    db_uri: str = Field(default=join(dirname(__file__), 'db.sqlite3'))
    lora_folder: str = ""
    proxy: str | None = Field(default=None)
    api_key: str | None = Field(default=None)

class LoadSettingsError(Exception):
    def __init__(self, msg: str = ''):
        self.msg = msg

    def __str__(self):
        return self.msg

class DatabaseNotFound(Exception):
    def __init__(self, msg: str = ''):
        self.msg = msg

    def __str__(self):
        return self.msg

class LoraFolderNotFound(Exception):
    def __init__(self, msg: str = ''):
        self.msg = msg

    def __str__(self):
        return self.msg

def load_settings():
    # if file doest exists
    if not exists(path=config_file):
        raise FileNotFoundError()
    
    # if file content broken makes it un deserializable
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            f_str = f.read()
            data = json.loads(f_str)
            # if settings option value (like lora_folder) can't be found
            settings = Settings(**data)
            return settings
    except:
        raise LoadSettingsError("Load settings failed")

def check_settings(settings: Settings):
    # check if lora_folder exists
    if not exists(settings.lora_folder):
        raise LoraFolderNotFound
    
    # check database
    if not exists(settings.db_uri):
        raise DatabaseNotFound(msg="database doesn't exists")

def save_settings(settings: Settings):
    check_settings(settings)

    with open(config_file, 'w', encoding="utf-8") as f:
        f.write(settings.model_dump_json(indent=2))

