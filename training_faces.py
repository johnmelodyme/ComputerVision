import os as Machine

BASE_DIRECTORY = Machine.path.dirname(Machine.path.abspath(__file__))
IMAGE_DATABASE_DIRECTORY = Machine.path.join(BASE_DIRECTORY, "model")
# print(IMAGE_DATABASE_DIRECTORY)

for root, dirs, files in Machine.walk(IMAGE_DATABASE_DIRECTORY):
      for file in files:
            if file.endswith("jpg") or file.endswith("png"): # Prefered (.png)
                  path = Machine.path.join(root, file)
                  label = Machine.path.basename(Machine.path.dirname(path)).replace(" ","-").upper()
                  print(label, path)