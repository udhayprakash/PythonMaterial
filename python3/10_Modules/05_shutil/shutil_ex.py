import shutil
import os

if not os.path.exists("target_dir"):
    os.mkdir("target_dir")

target_dir_path = "target_dir"
source_dir_path = "."

for file in os.listdir(source_dir_path):
    if os.path.splitext(file)[1] == ".py":
        print(file)
        shutil.copy(file, os.path.join(target_dir_path, file))
