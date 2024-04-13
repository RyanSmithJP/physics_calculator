import tkinter as tk
from settings import goBack
class GravitationalFrame(tk.Frame):
    def __init__(self, master=None, precision=None, **kwargs):
        super().__init__(master, **kwargs) #initialise before modifying frame
        #Variables
        self.distance_units = "km" #use by default
        self.weight_units = "kg"
        self.label_mass_1 = tk.Label(self, text="Mass 1 (kg):")
        self.label_mass_1.grid(row=0, column=0)
        self.label_mass_2 = tk.Label(self, text="Mass 2 (kg):")
        self.label_mass_2.grid(row=1, column=0)
        self.entry_mass_1 = tk.Entry(self)
        self.entry_mass_1.grid(row=0, column=1)
        self.entry_mass_2 = tk.Entry(self)
        self.entry_mass_2.grid(row=1, column=1)
        self.label_radius = tk.Label(self, text=f"Radius ({self.distance_units}):")
        self.label_radius.grid(row=2, column=0)
        self.entry_radius = tk.Entry(self)
        self.entry_radius.grid(row=2, column=1)
        #Units of measurement
        self.label_units = tk.Label(self, text="Units: ")
        self.label_units.grid(row=3,column=0)
        self.button_m = tk.Button(self,text="Metres", command=lambda: self.change_units("m"))
        self.button_m.grid(row=3, column=1)
        self.button_km = tk.Button(self,text="Kilometres", command=lambda: self.change_units("km"))
        self.button_km.grid(row=3, column=2)
        self.button_goBack = tk.Button(self, text="Go back", command=lambda: goBack(self)) #switch to precision on click
        self.button_goBack.grid(row=4, column=0)
        self.button_calculate = tk.Button(self, text="Calculate", command=lambda: self.calculate_gravity(precision))
        self.button_calculate.grid(row=4, column=1)
        #result
        self.label_g_result = tk.Label(self, text="")
        self.label_g_result.grid(row=5, columnspan=2)
    def calculate_gravity(self,precision):
        try:
            m1 = float(self.entry_mass_1.get())
            m2 = float(self.entry_mass_2.get())
            radius = float(self.entry_radius.get())
            if(self.distance_units=="km"):
                radius *=1000
            grav_constant = 6.674*(10**-11)
            result = (grav_constant*m1*m2)/(radius**2)
            self.label_g_result.config(text=f'Force = {result:.{precision.get()}f} m/s^2')
            self.label_g_result.grid(row=5, columnspan=2)
        except ValueError:
            self.label_g_result.config(text='Please enter valid parameters')
            self.label_g_result.grid(row=5, columnspan=2)
    def change_units(self,new_units):
        if(new_units=="m"):
            self.distance_units = "m"
        else:
            self.distance_units = "km"
        self.label_radius.config(text=f"Radius ({self.distance_units}):")
        self.label_g_result.grid_remove()
