#!/usr/bin/python

import subprocess

active_layout = subprocess.run("hyprctl devices | grep Slovak",
                               shell = True,
                               capture_output = True).stdout.decode("utf-8")
if active_layout == "":
    subprocess.run("hyprctl keyword input:kb_layout sk",shell = True)

else:
    subprocess.run("hyprctl keyword input:kb_layout us",shell = True)
