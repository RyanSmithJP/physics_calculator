import tkinter as tk
from settings import goBack
from settings import showSettings
from settings_frame import SettingsFrame
class GravityFrame(tk.Frame):
    def __init__(self, master=None, precision=None, **kwargs):
        super().__init__(master, **kwargs) #initialise before modifying frame
        #gravity
        label_mass = tk.Label(self, text="Mass (kg):")
        label_mass.grid(row=0, column=0)
        entry_mass = tk.Entry(self)
        entry_mass.grid(row=0, column=1)
        label_radius = tk.Label(self, text="Radius (m):")
        label_radius.grid(row=1, column=0)
        entry_radius = tk.Entry(self)
        entry_radius.grid(row=1, column=1)
        #precision

        button_calculate = tk.Button(self, text="Calculate", command=lambda: self.calculate_gravity(entry_mass,entry_radius,precision,label_g_result))
        button_calculate.grid(row=2, columnspan=2)
        button_goBack = tk.Button(self, text="Go Back", command=lambda: goBack(self)) #switch to precision on click
        button_goBack.grid(row=3, columnspan=2)
        #result
        label_g_result = tk.Label(self, text="")
        label_g_result.grid(row=4, columnspan=2)
    def calculate_gravity(self,entry_mass, entry_radius, precision, label_result):
        try:
            mass = float(entry_mass.get())
            radius = float(entry_radius.get())
            grav_constant = 6.674*(10**-11)
            result = (grav_constant*mass)/(radius**2)
            label_result.config(text=f'Acceleration due to gravity = {result:.{precision.get()}f} m/s^2')
        except ValueError:
            label_result.config(text='Please enter valid parameters')
