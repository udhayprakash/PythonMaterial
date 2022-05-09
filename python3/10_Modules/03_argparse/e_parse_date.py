"""
Purpose: parse the dates with argparse
"""
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument(
    "-s",
    "--start",
    # type=datetime.date,
    type=lambda d: datetime.datetime.strptime(d, "%Y-%m-%d").date(),
    help="Set a start date",
)

# args = parser.parse_args(["-s", "2022-01-01"])
args = parser.parse_args()
print(args)  # Namespace(start=datetime.date(2022, 9, 12))
print(args.start)  # 2022-09-12

# py e_parse_date.py -s 2022-09-12
