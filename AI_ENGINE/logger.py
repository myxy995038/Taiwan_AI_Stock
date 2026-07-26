"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

logger.py

System Logger
==========================================================
"""

from pathlib import Path
import logging

from AI_ENGINE.config import PATHS


# 建立 logs 資料夾（保險起見）
PATHS.LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = PATHS.LOG_DIR / "system.log"


# 建立 Logger
logger = logging.getLogger("TaiwanAI")

# 避免重複加入 Handler（Jupyter / 重複 import 時很重要）
if not logger.handlers:

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)