#!/usr/bin/python

import subprocess
import sys

current_num_of_screenshot = subprocess.run("ls ~/Pictures/Screenshots | wc -l",
                                       shell=True,
                                       capture_output=True).stdout.decode("utf-8")

current_num_of_screenshot = int(current_num_of_screenshot) + 1

if sys.argv[1] == "full":
    subprocess.run(f"grim ~/Pictures/Screenshots/FullScreenshot-{current_num_of_screenshot}.png",
                   shell=True)
else: 
    subprocess.run(f"grim -g \"$(slurp)\" ~/Pictures/Screenshots/Screenshot-{current_num_of_screenshot}.png",
                   shell=True)
