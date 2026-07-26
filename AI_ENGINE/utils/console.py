"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

console.py

Console Output Framework
==========================================================
"""

from datetime import datetime

LINE = "=" * 60
SUBLINE = "-" * 60


# ----------------------------------------------------------
# Banner
# ----------------------------------------------------------

def banner(title="Taiwan AI Stock System", version=None):

    print()
    print(LINE)
    print(f"🚀 {title}")

    if version:
        print(version)

    print(LINE)


# ----------------------------------------------------------
# Section
# ----------------------------------------------------------

def section(title):

    print()
    print(SUBLINE)
    print(f"📌 {title}")
    print(SUBLINE)


# ----------------------------------------------------------
# Status
# ----------------------------------------------------------

def success(msg):

    print(f"✅ {msg}")


def warning(msg):

    print(f"⚠️ {msg}")


def error(msg):

    print(f"❌ {msg}")


def info(msg):

    print(f"ℹ️ {msg}")


# ----------------------------------------------------------
# Finish
# ----------------------------------------------------------

def finish(name, elapsed=None):

    print(SUBLINE)

    if elapsed is not None:
        print(f"⏱ {name} : {elapsed:.3f} sec")

    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# ----------------------------------------------------------
# Blank Line
# ----------------------------------------------------------

def blank():

    print()