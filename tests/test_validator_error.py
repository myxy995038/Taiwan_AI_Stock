from AI_ENGINE.utils.validator import *

try:

    validate_score(120)

except Exception as e:

    print(type(e).__name__)

    print(e)