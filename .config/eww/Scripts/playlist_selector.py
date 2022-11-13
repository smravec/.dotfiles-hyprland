#!/usr/bin/python

import subprocess
import sys

mpc_status = subprocess.run("mpc | grep -o off | wc -l",
                            shell=True,
                            capture_output=True).stdout.decode("utf-8")

#Check if this is the first startup if not clear all the loaded songs
if int(mpc_status) > 2:
    subprocess.run("mpc random",shell=True)
    subprocess.run("mpc repeat",shell=True)

else:
    subprocess.run("mpc clear",shell=True)

subprocess.run(f"mpc load {sys.argv[1]}",shell=True)
subprocess.run(f"mpc play",shell=True)
subprocess.run("eww close playlist_selector",shell=True)
