import subprocess

# Specify the path to the wheel file
wheel_file_path = r"package5\dist\ops-1.0.0-py3-none-any.whl"

# Install the package using pip
subprocess.run(["pip", "install", "-U", "pip"])
subprocess.run(["pip", "install", "-U", wheel_file_path])

# Display the installed packages
subprocess.run(["pip", "list"])


import package5

print(f"{package5          =}")
print(f"{package5.__file__ =}")
print(dir(package5))
print()

import ops

print(f"{ops          =}")
print(f"{ops.__file__ =}")
print(dir(ops))
