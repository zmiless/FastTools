from customtkinter import *
import customtkinter
import os
from win10toast import ToastNotifier

toast = ToastNotifier()

# Commands For Buttonm


def shutdown():
    os.system("shutdown /s /t 0")


def restart():
    os.system("shutdown /r /t 0")


def logout():
    os.system("shutdown /l")


def open_cmd():
    os.system("start")


def close():
    os.system("taskkill /im FastTools.exe")
    os.system("taskkill /f /im Python.exe")

def open_git():
    os.system("start https://github.com/zmiless?tab=repositories")


# End
root = customtkinter.CTk()
root.geometry("520x520")
root.title("Fast Tools")
root.iconbitmap("icon.ico")
root.resizable(False, False)

Font_tuple = ("Comic Sans MS", 32, "bold")
Title = customtkinter.CTkLabel(master=root, text="Fast Tools", font=Font_tuple)
Title.pack(padx=10, pady=10)

button = ("Comic Sans MS", 16, "bold")

shutdown_button = customtkinter.CTkButton(
    master=root, text="ShutDown PC", font=button, command=shutdown)
shutdown_button.pack(padx=10, pady=12)

restart_button = customtkinter.CTkButton(
    master=root, text="Restart PC", font=button, command=restart)
restart_button.pack(padx=10, pady=12)

logout_button = customtkinter.CTkButton(
    master=root, text="LogOut", font=button, command=logout)
logout_button.pack(padx=10, pady=12)

opencmd_button = customtkinter.CTkButton(
    master=root, text="Open CMD", font=button, command=open_cmd)
opencmd_button.pack(padx=10, pady=12)

close_button = customtkinter.CTkButton(
    master=root, text="Close FastTools", font=button, command=close)
close_button.pack(padx=10, pady=12)

# This Need To Be Here! Stay Organized :D

opengit_button = customtkinter.CTkButton(
    master=root, text="Credits", font=button, command=open_git)
opengit_button.pack(padx=10, pady=12)

credits_font = ("Comic Sans MS", 16)

credits_app = customtkinter.CTkLabel(
    master=root, text="Fast Tools - By zMiles", font=credits_font)
credits_app.pack(padx=10, pady=10, side=BOTTOM, anchor=NW)


root.mainloop()
