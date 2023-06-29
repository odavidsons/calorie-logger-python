"""
Author: David Santos
Repository: https://github.com/odavidsons/calorie-logger-python
Year: 2023

File imported by mainView.py. Renders all of the widgets belonging to the settings window. Also has the controller functions for this window.
"""
import customtkinter as ctk

class settings(ctk.CTkToplevel):

    def __init__(self,master):
        super().__init__(master)
        self.title("Settings")