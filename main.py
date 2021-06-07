# main.py
import PySimpleGUI as sg
import subprocess as sp
import os
sg.theme('DarkAmber')
layout = [[sg.Text("If you're in the normal os, use these:")], [sg.Button("Reboot to System (adb)")],
          [sg.Button("Reboot to Fastboot (adb)")], [sg.Text("If you're in fastboot mode, use these:")]]

# Create the window
window = sg.Window("ADB Toolkit", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Reboot to System (adb)":
        os.system('data\\adb.exe reboot system')
    if event == "Reboot to Fastboot (adb)":
        os.system('data\\adb.exe reboot bootloader')
    if event == "Fastboot Commands":
        fastboot_layout = [[sg.Text("If you're in fastboot mode, use these:")], [sg.Button("Reboot to System")],
                           [sg.Button("Reboot to Fastboot")], [sg.Button("ADB Commands")]]
        fastboot_window = sg.Window("ADB Toolkit: Fastboot Mode", fastboot_layout)
    if event == sg.WIN_CLOSED:
        break
window.close()
