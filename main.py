# main.py
import PySimpleGUI as sg
import subprocess as sp
import os

layout = [[sg.Text("If you're in the normal os, use these:")], [sg.Button("Reboot to System")], [sg.Button("Reboot to Fastboot")]]

# Create the window
window = sg.Window("ADB Toolkit", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Reboot to System":
        os.system('adb.exe reboot system')
    if event == "Reboot to Fastboot":
        os.system('adb.exe reboot bootloader')
    if event == sg.WIN_CLOSED:
        break
window.close()