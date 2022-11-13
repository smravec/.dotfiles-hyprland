#!/usr/bin/python

import subprocess

eww_status = subprocess.run("eww windows | grep playlist_selector",
                            shell=True,
                            capture_output=True).stdout.decode("utf-8")
#Checks if window is opened
if eww_status[0] == "*":
    subprocess.run("eww close playlist_selector",shell=True)

else:
    subprocess.run("eww open playlist_selector",shell=True)
