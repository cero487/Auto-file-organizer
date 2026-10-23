import os
import shutil
from pathlib import Path
import sys

from sympy import false

Directory_map = {
    "Images": [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".json", ".sql"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Media": [".mp4", ".mkv", ".avi", ".mp3", ".wav"],
}

def organize_directory(target_dir):
    path = Path(target_dir).resolve()

    if not path.exists():
        print(f"Error: {target_dir} does not exist")
        return
    print(f"Scanning directory: {path}")
    files_moved = 0

    for item in path.iterdir():
        if item.is_dir() or item.name.startswith("."):
            continue
        file_extension = item.suffix.lower()
        moved = False

        for category, extensions in Directory_map.items():
            if file_extension in extensions:
                category_dir = path / category
                category_dir.mkdir(exist_ok=True)

                destination = category_dir / item.name

                if destination.exists():
                    base = item.stem
                    suffix = item.suffix
                    counter = 1
                    while destination.exists():
                        destination = category_dir / f"{base}_{counter}{suffix}"
                        counter += 1

                shutil.move(str(item), str(destination))
                print(f"Moved: {item.name} -> {category}/")
                files_moved += 1
                moved = True
                break
        if not moved:
            others_dir = path / "Others"
            others_dir.mkdir(exist_ok=True)
            destination = others_dir / item.name
            if not destination.exists():
                shutil.move(str(item), str(destination))
                print(f"Moved: {item.name} -> Others/")
                files_moved += 1
    print(f"\nOrganization complete! Total files moved: {files_moved}\n")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    organize_directory(target)