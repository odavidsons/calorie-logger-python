"""
Author: David Santos
Repository: https://github.com/odavidsons/calorie-logger-python
Year: 2023

This application is a calorie logger, where you can register days and add all of the food that you consumed and it's calorie values.
You can view the total macros for each day and export the data to text files.
"""
from calorieLogger import calorieLogger

app = calorieLogger()
app.mainloop()