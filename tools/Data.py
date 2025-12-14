from typing import List, Dict, Any

from Main import classG_log

def listG_searchTopKeys(dictT_data: Dict[Any, Any]) -> List[str] | None:
    try:
        if not isinstance(dictT_data, dict):
            classG_log.noneG_LogError("Invalid data submitted")
            return None
        return [str(key).upper() for key in dictT_data.keys()]
    except Exception as err:
        classG_log.noneG_LogError(f"Unexpected error: {type(err).__name__}: {err}")
        return None

def valueG_searchValuesOnKey(dictT_data: dict, strT_key: str) -> str | int | float | dict | list | None:
    try:
        return dictT_data.get(strT_key.upper())
    except KeyError:
        classG_log.noneG_LogError(f"Key {strT_key} is missing in data")
        return None
    except Exception as err:
        classG_log.noneG_LogError(f"Unexpected error: {type(err).__name__}: {err}")
        return None

def listG_saveValueInDataOnKey(dictT_data: dict, strT_key: str, valueT_value: str | int | float | dict | list) -> dict | None:
    try:
        dictT_data[strT_key.upper()] = valueT_value
        return dictT_data
    except KeyError:
        classG_log.noneG_LogError(f"Key {strT_key} is missing in data")
    except Exception as err:
        classG_log.noneG_LogError(f"Unexpected error: {type(err).__name__}: {err}")
        return None