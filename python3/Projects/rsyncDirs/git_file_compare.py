import filecmp
import os

from git import Repo

# pip install GitPython


Repo.clone_from(
    "https://github.com/sonu489/batch25jan2020.git",
    "C:/Users/Amma/udhay",
    branch="master",
)
Repo.clone_from(
    "https://sonu489@bitbucket.org/sonu489/batch25jan2020-new.git",
    "C:/Users/Amma/udhay",
    branch="master",
)

path = "C:/Users/Amma/udhay"

comparision = filecmp.dircmp(path + "batch25jan2020", path + "batch25jan2020-new")
common_files = ", ".join(comparision.common)
left_only_files = ", ".join(comparision.left_only)
right_only_files = ", ".join(comparision.right_only)

with open(path + "folder_diff.txt", "w") as folder_report:
    folder_report.write("Common Files: " + common_files)
