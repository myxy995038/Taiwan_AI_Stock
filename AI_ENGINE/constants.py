"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

constants.py

System Global Constants

Author : 志真
Python : 3.11
==========================================================
"""

# ==========================================================
# System Information
# ==========================================================

SYSTEM_NAME = "Taiwan AI Stock System"

SYSTEM_SHORT_NAME = "TAIS"

VERSION = "V10 Ultimate Enterprise"

AUTHOR = "志真"

BUILD_YEAR = 2026

PYTHON_VERSION = "3.11"

# ==========================================================
# Folder
# ==========================================================

DATA_DIR = "data"

REPORT_DIR = "reports"

HISTORY_DIR = "history"

LOG_DIR = "logs"

BACKUP_DIR = "backup"

DOC_DIR = "docs"

MODEL_DIR = "AI_ENGINE/model"

# ==========================================================
# Excel
# ==========================================================

DEFAULT_REPORT_NAME = "台股AI量化系統"

REPORT_EXTENSION = ".xlsx"

CSV_ENCODING = "utf-8-sig"

# ==========================================================
# Learning
# ==========================================================

LEARNING_HISTORY_FILE = "history/learning_history.csv"

PERFORMANCE_FILE = "history/performance_history.csv"

WEIGHT_HISTORY_FILE = "history/weight_history.csv"

MODEL_FILE = "AI_ENGINE/model/AI_WEIGHT.pkl"

# ==========================================================
# Score
# ==========================================================

MAX_SCORE = 150

BUY_SCORE = 90

WATCH_SCORE = 75

SELL_SCORE = 50

# ==========================================================
# Portfolio
# ==========================================================

MAX_POSITION = 10

DEFAULT_POSITION = 5

MAX_SINGLE_POSITION = 0.20

# ==========================================================
# Risk
# ==========================================================

DEFAULT_STOP_LOSS = 0.08

DEFAULT_TAKE_PROFIT = 0.20

MAX_RISK_PER_TRADE = 0.02

# ==========================================================
# Dashboard
# ==========================================================

SHEET_DASHBOARD = "Dashboard"

SHEET_AI = "AI Learning"

SHEET_REPORT = "AI Report"

SHEET_HISTORY = "History"

# ==========================================================
# AI
# ==========================================================

AI_ENGINE_NAME = "Ultimate Learning Engine"

AI_MODEL_VERSION = "V10"

DEFAULT_THEME_BONUS = 5

MAX_THEME_BONUS = 20

# ==========================================================
# Date
# ==========================================================

DATE_FORMAT = "%Y-%m-%d"

TIME_FORMAT = "%H:%M:%S"

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# ==========================================================
# API
# ==========================================================

FINMIND_URL = "https://api.finmindtrade.com/api/v4/data"

USER_AGENT = "Taiwan_AI_Stock_System"

TIMEOUT = 30









# ==========================================================
# Debug
# ==========================================================

DEBUG = True

VERBOSE = True


# ==========================================================
# Theme Score
# ==========================================================

THEME_SCORE = {

    "AI": 20,

    "半導體": 15,

    "光通訊": 15,

    "CPO": 10,

    "PCB": 10,

    "軍工": 15,

    "航運": 5,

    "金融": -10,

}




# ==========================================================
# Feature Columns
# 統一所有 AI 因子名稱
# ==========================================================

FACTOR_COLUMNS = [

    "money_score",

    "liquidity_score",

    "trend_score",

    "momentum_score",

    "institution_score",

    "trade_score",

    "revenue_score",

    "theme_score",

    "priority_score",

]