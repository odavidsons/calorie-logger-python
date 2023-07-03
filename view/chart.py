"""
Author: David Santos
Repository: https://github.com/odavidsons/calorie-logger-python
Year: 2023

File imported by mainView.py. Renders a pie chart with the macros of the selected date.
"""
import customtkinter as ctk
import matplotlib.pyplot as plt

class chart():

    def __init__(self,carbs,proteins,fats):
        data = [carbs,proteins,fats]
        plt.pie(data,labels=[f"Carbs ({carbs}g)",f"Proteins ({proteins}g)",f"Fats ({fats}g)"],autopct="%1.1f%%")
        plt.show()