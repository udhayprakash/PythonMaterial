import os
import subprocess
from security import safe_command


def execute_command(cmd):
    result = os.system(cmd)  # returns 0 if command executed successfully, else 1
    print(f"result:{result}")


execute_command("ping google.com")  # 0
execute_command("ipconfig")  # 0
execute_command("ipconfigjhg")  # 1


def get_execution_result(cmd):
    p = safe_command.run(subprocess.Popen, cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, err = p.communicate()

    output = output.decode("utf-8")
    err = err.decode("utf-8")

    print(f"\noutput:{output}")
    print(f"err   :{err}")


get_execution_result("ping google.com")
get_execution_result("ipconfig")
get_execution_result("ipconfigjhg")
