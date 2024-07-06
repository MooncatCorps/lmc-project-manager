from typing import Any, Optional

def contains(key: str, data: dict) -> bool:
    mut_data = data

    for k in key.split('.'):
        if not k in mut_data:
            return False

    return True

def get(key: str, data: dict) -> Optional[Any]:
    mut_data = data

    for k in key.split('.'):
        if k not in mut_data:
            return None

        mut_data = mut_data[k]
    
    return mut_data


