import argparse
import importlib
import sys


def main():
    parser = argparse.ArgumentParser("Say hello to the world")
    parser.add_argument("command", type=str, help="Which command to run")

    args = parser.parse_args()
    try:
        module = importlib.import_module(f"hello_world.commands.{args.command}")
    except ModuleNotFoundError:
        print("Invalid command")
        sys.exit(1)

    getattr(module, "Command")().run()
