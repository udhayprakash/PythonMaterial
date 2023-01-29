#!/usr/bin/python3
"""
Purpose:
    Command-line utility for synchronizing two local directories
    .
    |-- dst/
    |   |-- foo
    |-- src/
        |-- bar
        |-- baz
        |-- foo
"""
import argparse
import os
import shutil


def is_dry_run() -> bool:
    parser = argparse.ArgumentParser(
        description="command line program for synchronizing two local directories"
    )

    parser.add_argument("-dr", "--dry-run", help="To make dry run", action="store_true")
    args = parser.parse_args()
    print("DRY RUN =", args.dry_run)
    return args.dry_run


class RSync(object):
    def __init__(self):
        pass

    def create_folder_structure(self):
        os.makedirs("dst", exist_ok=True)
        open("dst/foo", "w").close()

        os.makedirs("src", exist_ok=True)
        open("src/bar", "w").close()
        open("src/baz", "w").close()
        open("src/foo", "w").close()

        # clean-up
        if os.path.exists("dst/bar"):
            os.remove("dst/bar")
        if os.path.exists("dst/baz"):
            os.remove("dst/baz")

    def sync_dirs(self, source_dir, destin_dir, dry_run=True):
        print("\nDRY_RUN=", dry_run)
        for each_file in os.listdir(source_dir):
            src_file = os.path.join(source_dir, each_file)
            dst_file = os.path.join(destin_dir, each_file)
            print(
                """Syncing ...
                SOURCE FILE PATH      - {0}
                DESTINATION FILE PATH - {1}""".format(
                    src_file, dst_file
                )
            )
            if not dry_run:
                shutil.copyfile(src_file, dst_file)


if __name__ == "__main__":
    # setup
    DRY_RUN = is_dry_run()
    r = RSync()
    r.create_folder_structure()
    r.sync_dirs("src", "dst", DRY_RUN)
