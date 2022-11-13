#!/usr/bin/python

import subprocess

icons = ["󰤨","󰤭"]

#Get current wifi card status
battery_status = subprocess.run("iw wlp170s0 link | grep SSID",
                                shell = True,
                                capture_output=True).stdout.decode("utf-8")

#if returned string is 0 means there is not any active connection
if len(battery_status) != 0:
    print(icons[0])
else:
    print(icons[1])
