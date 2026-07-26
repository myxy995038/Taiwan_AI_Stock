"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

environment.py

System Startup & Environment Check
==========================================================
"""

import sys
import time
import importlib

from AI_ENGINE.logger import logger
from AI_ENGINE.constants import (
    SYSTEM_NAME,
    VERSION,
    PYTHON_VERSION,
)
from AI_ENGINE.config import PATHS


# ----------------------------------------------------------
# Required Packages
# ----------------------------------------------------------

REQUIRED_PACKAGES = [
    "pandas",
    "numpy",
    "openpyxl",
    "matplotlib",
    "sklearn",
    "requests",
]


# ----------------------------------------------------------
# Banner
# ----------------------------------------------------------

def print_banner():

    print("=" * 60)
    print(f"🚀 {SYSTEM_NAME}")
    print(f"Version : {VERSION}")
    print("=" * 60)


# ----------------------------------------------------------
# Check Python
# ----------------------------------------------------------

def check_python():

    version = f"{sys.version_info.major}.{sys.version_info.minor}"

    if version != PYTHON_VERSION:
        logger.warning(f"Python Version : {version}")

    else:
        logger.info(f"Python Version : {version}")


# ----------------------------------------------------------
# Check Package
# ----------------------------------------------------------

def check_packages():

    logger.info("Checking Packages...")

    for package in REQUIRED_PACKAGES:

        try:

            importlib.import_module(package)

            logger.info(f"✔ {package}")

        except Exception:

            logger.error(f"✘ {package}")


# ----------------------------------------------------------
# Check Folder
# ----------------------------------------------------------

def check_folder():

    logger.info("Checking Project Folder...")

    folders = [
        PATHS.DATA_DIR,
        PATHS.REPORT_DIR,
        PATHS.HISTORY_DIR,
        PATHS.LOG_DIR,
        PATHS.MODEL_DIR,
    ]

    for folder in folders:

        if folder.exists():

            logger.info(f"✔ {folder.name}")

        else:

            logger.error(f"✘ {folder.name}")


# ----------------------------------------------------------
# Startup
# ----------------------------------------------------------

def startup():

    start = time.perf_counter()

    print_banner()

    check_python()

    check_packages()

    check_folder()

    elapsed = time.perf_counter() - start

    logger.info(f"Startup Time : {elapsed:.2f} sec")