# ==============================================================================
# AI_ENGINE/utils/list_utils.py
# Taiwan AI Stock System
# V10 Ultimate Enterprise
#
# List Utility Library
# ==============================================================================

from __future__ import annotations

from typing import Any, Iterable, List, Optional
import random

# ==============================================================================
# Basic
# ==============================================================================

def unique(items: Iterable[Any]) -> List[Any]:
    """
    移除重複元素，保持原順序
    """
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# ------------------------------------------------------------------------------

def remove_none(items: Iterable[Any]) -> List[Any]:
    """
    移除 None
    """
    return [x for x in items if x is not None]


# ------------------------------------------------------------------------------

def remove_empty(items: Iterable[Any]) -> List[Any]:
    """
    移除 None、''、空白字串
    """
    result = []

    for item in items:

        if item is None:
            continue

        if isinstance(item, str):

            if item.strip() == "":
                continue

        result.append(item)

    return result


# ==============================================================================
# Flatten
# ==============================================================================

def flatten(items: Iterable) -> List[Any]:
    """
    將巢狀 List 攤平成一維
    """

    result = []

    for item in items:

        if isinstance(item, (list, tuple, set)):

            result.extend(flatten(item))

        else:

            result.append(item)

    return result


# ==============================================================================
# Chunk
# ==============================================================================

def chunk(items: List[Any], size: int) -> List[List[Any]]:
    """
    將 List 切成固定大小
    """

    if size <= 0:
        return [items]

    return [
        items[i:i+size]
        for i in range(0, len(items), size)
    ]


# ==============================================================================
# Safe
# ==============================================================================

def first(items: List[Any], default=None):
    """
    第一個元素
    """

    if len(items) == 0:
        return default

    return items[0]


# ------------------------------------------------------------------------------

def last(items: List[Any], default=None):
    """
    最後一個元素
    """

    if len(items) == 0:
        return default

    return items[-1]


# ==============================================================================
# Sort
# ==============================================================================

def sort_asc(items: List[Any]) -> List[Any]:
    """
    小到大排序
    """

    return sorted(items)


# ------------------------------------------------------------------------------

def sort_desc(items: List[Any]) -> List[Any]:
    """
    大到小排序
    """

    return sorted(
        items,
        reverse=True
    )


# ==============================================================================
# Top N
# ==============================================================================

def top_n(
    items: List[Any],
    n: int = 10
) -> List[Any]:
    """
    取前 N 個
    """

    return items[:n]


# ------------------------------------------------------------------------------

def bottom_n(
    items: List[Any],
    n: int = 10
) -> List[Any]:
    """
    取最後 N 個
    """

    if n <= 0:
        return []

    return items[-n:]


# ==============================================================================
# Search
# ==============================================================================

def contains(
    items: Iterable[Any],
    value: Any
) -> bool:
    """
    是否包含元素
    """

    return value in items


# ==============================================================================
# Random
# ==============================================================================

def random_choice(
    items: List[Any],
    default=None
):
    """
    隨機選一個
    """

    if len(items) == 0:

        return default

    return random.choice(items)


# ------------------------------------------------------------------------------

def random_sample(
    items: List[Any],
    n: int = 5
) -> List[Any]:
    """
    隨機抽樣
    """

    if len(items) <= n:

        return items.copy()

    return random.sample(
        items,
        n
    )


# ==============================================================================
# Statistics
# ==============================================================================

def count(items: Iterable[Any]) -> int:
    """
    元素數量
    """

    return len(list(items))


# ------------------------------------------------------------------------------

def frequency(
    items: Iterable[Any]
):
    """
    統計各元素出現次數
    """

    freq = {}

    for item in items:

        freq[item] = freq.get(item, 0) + 1

    return freq


# ==============================================================================
# Filter
# ==============================================================================

def filter_none(
    items: Iterable[Any]
):
    """
    過濾 None
    """

    return [x for x in items if x is not None]


# ------------------------------------------------------------------------------

def filter_positive(
    items: Iterable
):
    """
    保留大於0
    """

    return [
        x
        for x in items
        if isinstance(x, (int, float))
        and x > 0
    ]


# ==============================================================================
# End
# ==============================================================================