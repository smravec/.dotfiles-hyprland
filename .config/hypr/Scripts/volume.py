#!/usr/bin/python

import subprocess
import sys

volume_status = subprocess.run("pulsemixer --get-volume",
                                   shell=True,
                                   capture_output=True
                                   ).stdout.decode("utf-8")

volume_status = volume_status.split()
volume_status = int(volume_status[0])


if sys.argv[1] == "+":
    subprocess.run("pulsemixer --change-volume +10",shell=True)


elif sys.argv[1] == "-":

    if volume_status < 11:
        subprocess.run("pulsemixer --set-volume 1",shell=True)

    else:
        subprocess.run("pulsemixer --change-volume -10",shell=True)
