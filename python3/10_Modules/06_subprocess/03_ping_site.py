#!/usr/bin/python
"""
Purpose:
"""
import os
import subprocess
from security import safe_command


def ping_website(site_name):
    output = os.system(f"ping {site_name}")
    print(f"output: {output}")


def get_time_delays(site_name):
    p = safe_command.run(subprocess.Popen, f"ping {site_name}", stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, error = p.communicate()
    if error:
        print(f"error:{error}")
    else:
        output = output.decode("utf-8")
        print(f"output:{output}")


if __name__ == "__main__":
    # ping_website('wikipedia.org')
    get_time_delays("wikipedia.org")
