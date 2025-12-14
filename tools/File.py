import json

from glom import PathAccessError
from typing import Any, Optional, Dict, Union
from pathlib import Path

from pygments.token import string_to_tokentype

from Main import classG_log

def dictG_loadFile(strT_fileName: str, strT_dataDir: str = "./data") -> Optional[Any]:

    strT_filePath = Path(strT_dataDir) / f"{strT_fileName.lower()}.json"

    try:
        with open(strT_filePath, "r") as fileT_file:
            listT_data = json.load(fileT_file)
            return listT_data

    except PathAccessError:
        classG_log.noneG_LogError(f"File {strT_filePath} does not exist.")
        return None

    except FileNotFoundError:
        classG_log.noneG_LogError(f"File {strT_filePath} does not have permission.")
        return None

    except json.JSONDecodeError as err:
        classG_log.noneG_LogError(f"JSON parsing error: {err}")
        return None

    except Exception as err:
        classG_log.noneG_LogError(f"Unexpected error: {type(err).__name__}: {err}")
        return None


def noneG_saveFile(strT_fileName: str, dictT_newData: Dict[Any, Any], keyT_key: Union[str, int, float], strT_dataDir: str = "./data") -> None:
    strT_filePath = Path(strT_dataDir) / f"{strT_fileName.lower()}.json"
    dictT_fileData = {}

    try:
        if strT_filePath.exists() and strT_filePath.stat().st_size > 0:
            with open(strT_filePath, "r", encoding="utf-8") as fileT_file:
                dictT_fileData = json.load(fileT_file)

        dictT_fileData[str(keyT_key)] = dictT_newData

        with open(strT_filePath, "w", encoding="utf-8") as fileT_file:
            json.dump(dictT_fileData, fileT_file, indent=4, ensure_ascii=False)

    except json.JSONDecodeError as err:
        classG_log.noneG_LogError(f"JSON parsing error: {err}")
    except Exception as err:
        classG_log.noneG_LogError(f"Unexpected error: {type(err).__name__}: {err}")
