from pathlib import Path
import os

def can_read(path: Path) -> bool:
    return path.exists() and os.access(path, os.R_OK)

def can_write(path: Path) -> bool:
    return path.exists() and os.access(path, os.W_OK)

def can_execute(path: Path) -> bool:
    return path.exists() and os.access(path, os.X_OK)

