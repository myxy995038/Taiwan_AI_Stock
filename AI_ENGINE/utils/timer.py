"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

timer.py

Performance Timer
==========================================================
"""

import time
from AI_ENGINE.logger import logger


class Timer:
    """
    Enterprise Timer
    """

    def __init__(self, name="Task", auto_log=True):

        self.name = name
        self.auto_log = auto_log

        self.start_time = None
        self.end_time = None

    # ----------------------------

    def start(self):

        self.start_time = time.perf_counter()

    # ----------------------------

    def stop(self):

        self.end_time = time.perf_counter()

        elapsed = self.elapsed()

        if self.auto_log:

            logger.info(
                f"{self.name} Finished ({elapsed:.3f} sec)"
            )

        return elapsed

    # ----------------------------

    def elapsed(self):

        if self.start_time is None:

            return 0

        if self.end_time is None:

            return time.perf_counter() - self.start_time

        return self.end_time - self.start_time

    # ----------------------------

    def reset(self):

        self.start_time = None
        self.end_time = None

    # ----------------------------
    # Context Manager
    # ----------------------------

    def __enter__(self):

        self.start()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.stop()