#!/usr/bin/python

import subprocess
import sys

brightness_status = subprocess.run("brightnessctl i | grep Current",
                                   shell=True,
                                   capture_output=True
                                   ).stdout.decode("utf-8")

brightness_status = brightness_status.split()
brightness_status = int(brightness_status[-1][1:-2])


if sys.argv[1] == "+":
    subprocess.run("brightnessctl set +10%",shell=True)


elif sys.argv[1] == "-":

    if brightness_status < 11:
        subprocess.run("brightnessctl set 1%",shell=True)

    else:
        subprocess.run("brightnessctl set 10%-",shell=True)
