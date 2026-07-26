# ==============================================================================
# AI_ENGINE/utils/convert.py
# Taiwan AI Stock System
# V10 Ultimate Enterprise
#
# 型別安全轉換工具
# ==============================================================================

from __future__ import annotations

from typing import Any, Optional
import math

# ==============================================================================
# Number Convert
# ==============================================================================

def safe_int(value: Any, default: int = 0) -> int:
    """
    安全轉換為 int

    Parameters
    ----------
    value : Any
    default : int

    Returns
    -------
    int
    """
    try:
        if value is None:
            return default

        if isinstance(value, bool):
            return int(value)

        if isinstance(value, str):
            value = value.replace(",", "").strip()

        return int(float(value))

    except Exception:
        return default


# ------------------------------------------------------------------------------

def safe_float(value: Any, default: float = 0.0) -> float:
    """
    安全轉換為 float
    """
    try:

        if value is None:
            return default

        if isinstance(value, bool):
            return float(value)

        if isinstance(value, str):
            value = value.replace(",", "").strip()

        return float(value)

    except Exception:
        return default


# ------------------------------------------------------------------------------

def safe_str(value: Any, default: str = "") -> str:
    """
    安全轉換為字串
    """
    try:

        if value is None:
            return default

        return str(value)

    except Exception:
        return default


# ------------------------------------------------------------------------------

def safe_bool(value: Any) -> bool:
    """
    安全轉換為 bool
    """

    if isinstance(value, bool):
        return value

    if value is None:
        return False

    if isinstance(value, str):

        txt = value.lower().strip()

        return txt in [
            "true",
            "1",
            "yes",
            "y",
            "t"
        ]

    try:

        return bool(value)

    except Exception:

        return False


# ==============================================================================
# Numeric
# ==============================================================================

def is_number(value: Any) -> bool:
    """
    是否為數字
    """

    try:

        float(value)

        return True

    except Exception:

        return False


# ------------------------------------------------------------------------------

def is_nan(value: Any) -> bool:
    """
    是否為 NaN
    """

    try:

        return math.isnan(float(value))

    except Exception:

        return False


# ------------------------------------------------------------------------------

def is_empty(value: Any) -> bool:
    """
    是否為空值
    """

    if value is None:
        return True

    if isinstance(value, str):

        if value.strip() == "":
            return True

    return False


# ==============================================================================
# Percentage
# ==============================================================================

def safe_percentage(
    value: Any,
    default: float = 0.0
) -> float:
    """
    百分比字串轉 float

    Example
    -------
    15%
        ↓
    15.0
    """

    try:

        if value is None:
            return default

        if isinstance(value, str):

            value = value.replace("%", "")

            value = value.replace(",", "")

            value = value.strip()

        return float(value)

    except Exception:

        return default


# ==============================================================================
# Round
# ==============================================================================

def round2(value: Any) -> float:
    """
    四捨五入到小數二位
    """

    return round(safe_float(value), 2)


# ------------------------------------------------------------------------------

def round4(value: Any) -> float:
    """
    四捨五入到小數四位
    """

    return round(safe_float(value), 4)


# ==============================================================================
# Clip
# ==============================================================================

def clip(
    value: Any,
    minimum: float,
    maximum: float
) -> float:
    """
    限制數值範圍
    """

    value = safe_float(value)

    return max(
        minimum,
        min(
            value,
            maximum
        )
    )


# ==============================================================================
# Default
# ==============================================================================

def default_if_none(
    value: Any,
    default: Any
) -> Any:
    """
    None 則回傳預設值
    """

    if value is None:

        return default

    return value


# ==============================================================================
# End
# ==============================================================================