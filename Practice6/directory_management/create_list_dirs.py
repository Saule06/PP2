import os
from pathlib import Path

nested_path = Path("test_dir/level1/level2")
nested_path.mkdir(parents=True, exist_ok=True)
print(f"Directory create : {nested_path}")


print("\nItems in current directory")
for item in nested_path.iterdir():
    print(f"Item: {item}")

print("\nSearchin for .txt in files: ")
for txt_file in nested_path.glob("*.txt"):
    print(f"found: {txt_file}")