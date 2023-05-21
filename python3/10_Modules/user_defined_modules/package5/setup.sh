#!/bin/bash

# Define the folders to be deleted
foldersToDelete="build dist ops.egg-info"

# Loop through each folder and delete it along with its contents
for folder in $foldersToDelete; do
    if [ -d "$folder" ]; then
        echo "Deleting $folder folder..."
        rm -rf "$folder"
    fi
done

echo "Cleanup completed."

# Build the wheel file
python setup.py bdist_wheel
