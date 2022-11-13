#!/usr/bin/python

import subprocess

icons = ["󰕾","󰖁"]

#Get current volume status
volume_status = subprocess.run("pulsemixer --get-mute",
                                shell = True,
                                capture_output=True).stdout.decode("utf-8")

#if returned string is 0 means the volume is not muted
if int(volume_status) == 0:
    print(icons[0])
else:
    print(icons[1])
