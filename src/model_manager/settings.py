from pydantic_settings import BaseSettings
from pydantic import Field
from os.path import join, dirname, exists
import json

settings_file = join(dirname(__file__), '.settings.json')

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
    # if file content broken makes it un deserializable
    try:
        with open(settings_file, 'r', encoding='utf-8') as f:
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
    with open(settings_file, 'w', encoding="utf-8") as f:
        f.write(settings.model_dump_json(indent=2))

def init() -> Settings:
    initial_check_pass: bool = False
    settings: Settings

    while not initial_check_pass:
        # check if settings file exists
        if not exists(settings_file):
            print("settings file not found, creating new one.")
            settings = Settings()
            save_settings(settings)
            continue

        # check if settings are correct
        try:
            settings = load_settings()
            check_settings(settings)
        except LoadSettingsError:
            settings = Settings()
            save_settings(settings)
            print("Load settings failed, replace \".settings.json\" with default values.")
            input("Please edit \".settings.json\" then Press enter to continue...")
            continue
        except LoraFolderNotFound:
            print("Lora folder not found")
            input("please check \"lora_folder\" value in \".settings.json\" then Press enter to continue...")
            continue
        except DatabaseNotFound:
            print("Database not found")
            input("please check \"db_uri\" value in \".settings.json\" then Press enter to continue...")
            continue

        initial_check_pass = True
    
    return settings
