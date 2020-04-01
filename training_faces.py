import os as Machine

BASE_DIRECTORY = Machine.path.dirname(Machine.path.abspath(__file__))
IMAGE_DATABASE_DIRECTORY = Machine.path.join(BASE_DIRECTORY, "model")
print(BASE_DIRECTORY, IMAGE_DATABASE_DIRECTORY)