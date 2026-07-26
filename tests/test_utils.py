from AI_ENGINE.utils import *

print("=" * 60)

banner("Utils Test")

section("Timer")

timer = Timer("Sleep")

timer.start()

timer.stop()

section("Validator")

print(validate_score(80))

section("DataFrame")

print(has_column)

section("Excel")

print(save_excel)

print("=" * 60)