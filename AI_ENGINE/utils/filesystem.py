"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

filesystem.py

Enterprise File System Utilities
==========================================================
"""

from pathlib import Path
import shutil


# ----------------------------------------------------------
# Folder
# ----------------------------------------------------------

def ensure_dir(path):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def remove_folder(path):
    path = Path(path)

    if path.exists():
        shutil.rmtree(path)


# ----------------------------------------------------------
# File
# ----------------------------------------------------------

def file_exists(path):

    return Path(path).exists()


def remove_file(path):

    path = Path(path)

    if path.exists():

        path.unlink()


def copy_file(src, dst):

    shutil.copy2(src, dst)


# ----------------------------------------------------------
# List
# ----------------------------------------------------------

def list_files(folder, pattern="*"):

    folder = Path(folder)

    return sorted(folder.glob(pattern))


# ----------------------------------------------------------
# Human Readable Size
# ----------------------------------------------------------

def human_size(size):

    units = ["B", "KB", "MB", "GB", "TB"]

    size = float(size)

    for unit in units:

        if size < 1024:

            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"


# ----------------------------------------------------------
# Folder Size
# ----------------------------------------------------------

def folder_size(folder, ignore=None):

    folder = Path(folder)

    if ignore is None:
        ignore = []

    total = 0

    for file in folder.rglob("*"):

        # 檔案不存在
        if not file.exists():
            continue

        # 忽略指定資料夾
        skip = False

        for item in ignore:
            if item in file.parts:
                skip = True
                break

        if skip:
            continue

        # 只計算檔案大小
        if file.is_file():

            try:
                total += file.stat().st_size

            except OSError:
                continue

    return round(total / 1024 / 1024, 2)


# ----------------------------------------------------------
# Project Size
# ----------------------------------------------------------

from AI_ENGINE.config import PATHS

def project_size():

    return folder_size(
        PATHS.ROOT,
        ignore=[
            ".venv",
            "__pycache__",
            ".git",
            ".ipynb_checkpoints",
        ],
    )


# ----------------------------------------------------------
# Clean Pycache
# ----------------------------------------------------------

from AI_ENGINE.config import PATHS

def clean_pycache(root=None):

    if root is None:
        root = PATHS.ROOT

    root = Path(root)

    count = 0

    for folder in root.rglob("__pycache__"):

        shutil.rmtree(folder)

        count += 1

    return count


# ----------------------------------------------------------
# Clean Temp
# ----------------------------------------------------------

def clean_temp():

    remove_folder("temp")


# ----------------------------------------------------------
# Tree
# ----------------------------------------------------------

def project_tree(root=".", depth=2):

    root = Path(root)

    for path in sorted(root.rglob("*")):

        level = len(path.relative_to(root).parts)

        if level > depth:
            continue

        indent = "    " * (level - 1)

        print(f"{indent}{path.name}")