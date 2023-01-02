import time
from pynput import keyboard
import os
from win10toast import ToastNotifier
from customtkinter import *
import customtkinter

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.end}
]



    # The currently active modifiers
current = set()
 
 
def execute():
    print ("Comand Executed!")
    exec(open("window.pyw").read())
 
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
 
def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)
 
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
