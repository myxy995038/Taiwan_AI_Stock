from AI_ENGINE.utils.filesystem import *

print("=" * 60)

print("Project Size")

print(project_size(), "MB")

print()

print("Human Size")

print(human_size(project_size() * 1024 * 1024))

print()

print("Files")

for f in list_files("."):

    print(f)

print()

print("Remove __pycache__")

print(clean_pycache())

print("=" * 60)