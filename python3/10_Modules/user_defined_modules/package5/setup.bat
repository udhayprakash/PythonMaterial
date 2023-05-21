@echo off

REM Define the folders to be deleted
set "foldersToDelete=build dist ops.egg-info"

REM Loop through each folder and delete it along with its contents
for %%F in (%foldersToDelete%) do (
    if exist %%F (
        echo Deleting %%F folder...
        rmdir /s /q %%F
    )
)

echo Cleanup completed.

REM Build the wheel file
python setup.py bdist_wheel
