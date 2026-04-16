import shutil
import os
from pathlib import Path

source = "sample.txt"

destination = "sample_backup.txt"


if Path(source).exists():
    shutil.copy(source , destination)
    print(f"Backup created : {destination}")


file_to_delete = "to_be_deleted.txt"
Path(file_to_delete).touch()

if Path(file_to_delete).exists():
    os.remove(file_to_delete)
    print(f"File {file_to_delete} deleted")