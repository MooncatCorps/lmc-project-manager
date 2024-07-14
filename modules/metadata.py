from typing import Any, Optional

def get(key: str, data: dict) -> Optional[Any]:
    mut_data = data

    for k in key.split('.'):
        if k not in mut_data:
            return None

        mut_data = mut_data[k]
    
    return mut_data

def contains(key: str, data: dict) -> bool:
    return get(key, data) is None
