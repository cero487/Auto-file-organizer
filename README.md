# AutoFile Organizer

A lightweight, zero-dependency Python command-line utility designed to automatically clean up and organize messy directories (such as a `Downloads` folder) by sorting files into categorized subfolders based on their extensions.

## Features
- **Zero External Dependencies:** Built completely using Python's standard library (`pathlib`, `shutil`, `os`, `sys`), meaning it runs out of the box without requiring `pip install`.
- **Smart Categorization:** Automatically groups files into designated subfolders (`Images`, `Documents`, `Archives`, `Code`, `Media`, and `Others`).
- **Collision Safe:** Automatically handles duplicate file names by appending an incremental counter (e.g., `file_1.png`) instead of overwriting existing files.
- **Flexible Targeting:** Can target any custom folder path on your system via command-line arguments or default to the local directory.

## Requirements
- Python 3.x installed on your machine.

## Usage

Run the script from your terminal, passing the target directory path as an argument:

```bash
python Folder_organizer.py "C:\path\to\your\messy\folder"