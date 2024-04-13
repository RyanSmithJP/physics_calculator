import tkinter as tk
from gravity import calculate_gravity
from settings import showSettings
#from settings import goBack
from settings_frame import SettingsFrame
def main():
    root = tk.Tk()
    root.title("Physics app")
    #make frames
    precision = tk.IntVar(value=2)
    gravity_frame = tk.Frame(root)
    settings_frame = SettingsFrame(root,precision)
    #gravity
    label_mass = tk.Label(gravity_frame, text="Mass (kg):")
    label_mass.grid(row=0, column=0)
    entry_mass = tk.Entry(gravity_frame)
    entry_mass.grid(row=0, column=1)
    label_radius = tk.Label(gravity_frame, text="Radius (m):")
    label_radius.grid(row=1, column=0)
    entry_radius = tk.Entry(gravity_frame)
    entry_radius.grid(row=1, column=1)
    #precision


    button_calculate = tk.Button(gravity_frame, text="Calculate", command=lambda: calculate_gravity(entry_mass,entry_radius,precision,label_g_result))
    button_calculate.grid(row=2, columnspan=2)
    button_precision = tk.Button(gravity_frame, text="Precision", command=lambda: showSettings(gravity_frame,settings_frame)) #switch to precision on click
    button_precision.grid(row=3, columnspan=2)
    #result
    label_g_result = tk.Label(gravity_frame, text="")
    label_g_result.grid(row=4, columnspan=2)
    #***********************************************
    
    #show gravity_frame
    gravity_frame.grid(row=0,column=0,sticky="nsew")
    root.mainloop()
main()