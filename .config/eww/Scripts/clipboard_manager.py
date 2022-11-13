#!/usr/bin/python

import subprocess


clipboard_history = subprocess.run("cliphist list",
                                   shell=True,
                                   capture_output=True).stdout.decode("utf-8").split("\n")

del clipboard_history[-1]

#Remove Git tokens (or any other desired passwords)
token = ""

index = len(clipboard_history) - 1

while index >= 0:
    
    if token in clipboard_history[index]:
        del clipboard_history[index]
    
    index -= 1

#Select only 5 most recent copied things
if len(clipboard_history) > 5:
    clipboard_history = clipboard_history[0:5]

#Format selected items
for index,item in enumerate(clipboard_history):
    clipboard_history[index] = item[4:]

#Remove any quotes, backslashes and $ signs (dont have the patience to replace them) and shorten the text
for index,item in enumerate(clipboard_history):
    new_item = item.replace("'","")
    new_item = new_item.replace("\\","")
    new_item = new_item.replace("$","")
    new_item = new_item.replace('"','') 
    
    clipboard_history[index] =  new_item

#Remove any blank strings
index = len(clipboard_history) - 1

while index >= 0:
    
    if len(clipboard_history[index]) == 0:
        del clipboard_history[index]
    
    index -= 1

#List of shortened entries to show in eww widget (wont be actually coppied into clipboard)
shortened_text = []

for item in clipboard_history:
    if len(item) > 32:
        item = f"{item[0:29]}..."
    
    shortened_text.append(item)

#Generate buttons for eww
buttons = [f"(button :class \"clipboard-item\" :onclick \"wl-copy \\\"{item}\\\";eww close clipboard_manager\" \"{shortened_text[index]}\")" for index,item in enumerate(clipboard_history)]

#Make string from array
result_string = ""
for item in buttons:
    result_string = f"{result_string} {item}"

subprocess.run(f"echo '(box :spacing \"2\" :orientation \"vertical\" :class \"clipboard_container\" {result_string})'",shell=True)
