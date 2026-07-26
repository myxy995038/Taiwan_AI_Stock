import time

from AI_ENGINE.utils.timer import Timer


print("=" * 60)

print("Manual Timer")

timer = Timer("Sleep")

timer.start()

time.sleep(2)

elapsed = timer.stop()

print(f"Elapsed = {elapsed:.3f} sec")

print()

print("Context Manager")

with Timer("Context Sleep"):

    time.sleep(1)

print("=" * 60)