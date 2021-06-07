# main.py
import PySimpleGUI as sg
import os
sg.theme('GreenMono')
layout = [[sg.Text("If you're in the normal os, use these:")], [sg.Button("Reboot to System (adb)")],
          [sg.Button("Reboot to Fastboot (adb)")], [sg.Text("If you're in fastboot mode, use these:")], [sg.Button("Reboot to System (fastboot)")],
          [sg.Button("Reboot to Fastboot (fastboot)")], [sg.Button("Continue to System (fastboot)")]]
advanced_layout = [[sg.Text("If you're in the normal os, use these:")], [sg.Button("Reboot to System (adb)")],
          [sg.Button("Reboot to Fastboot (adb)")], [sg.Text("If you're in fastboot mode, use these:")], [sg.Button("Reboot to System (fastboot)")],
          [sg.Button("Reboot to Fastboot (fastboot)")], [sg.Button("Continue to System (fastboot)")]]

# Create the window
window = sg.Window("ADB Toolkit", layout)
advanced_window = sg.Window("[ADVANCED] ADB Toolkit", advanced_layout)

# Create an event loop
while True:
    event, values = window.read()
    if event == "Reboot to System (adb)":
        os.system('data\\adb.exe reboot system')
    if event == "Reboot to Fastboot (adb)":
        os.system('data\\adb.exe reboot bootloader')
    if event == "Reboot to System (fastboot)":
        os.system('data\\fastboot.exe reboot system')
    if event == "Reboot to Fastboot (fastboot)":
        os.system('data\\fastboot.exe reboot bootloader')
    if event == "Continue to System (fastboot)":
        os.system('data\\fastboot.exe continue')
    if event == sg.WIN_CLOSED:
        break
window.close()
