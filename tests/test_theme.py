from AI_ENGINE.feature import ThemeFeature

engine = ThemeFeature()

result = engine.run(

    [

        "AI",

        "光通訊",

        "CPO",

    ]

)

print("=" * 60)

print(result)

print()

print(result.primary)

print(result.names)

print("=" * 60)