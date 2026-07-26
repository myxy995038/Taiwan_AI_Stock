"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

config.py

Project Configuration Center
==========================================================
"""

from pathlib import Path
from dataclasses import dataclass


# ----------------------------------------------------------
# Project Root
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ----------------------------------------------------------
# Paths
# ----------------------------------------------------------

@dataclass(frozen=True)
class ProjectPaths:

    ROOT: Path = PROJECT_ROOT

    DATA_DIR: Path = PROJECT_ROOT / "data"

    REPORT_DIR: Path = PROJECT_ROOT / "reports"

    HISTORY_DIR: Path = PROJECT_ROOT / "history"

    LOG_DIR: Path = PROJECT_ROOT / "logs"

    BACKUP_DIR: Path = PROJECT_ROOT / "backup"

    DOC_DIR: Path = PROJECT_ROOT / "docs"

    NOTEBOOK_DIR: Path = PROJECT_ROOT / "notebook"

    MODEL_DIR: Path = PROJECT_ROOT / "AI_ENGINE" / "model"

    TEST_DIR: Path = PROJECT_ROOT / "tests"


PATHS = ProjectPaths()


# ----------------------------------------------------------
# Auto Create Folder
# ----------------------------------------------------------

def initialize_project():

    folders = [
        PATHS.DATA_DIR,
        PATHS.REPORT_DIR,
        PATHS.HISTORY_DIR,
        PATHS.LOG_DIR,
        PATHS.BACKUP_DIR,
        PATHS.DOC_DIR,
        PATHS.MODEL_DIR,
        PATHS.TEST_DIR,
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)


# 專案啟動時自動建立資料夾
initialize_project()