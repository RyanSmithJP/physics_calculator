import tkinter as tk
from tkinter import ttk #button styles
from tkinter import font
from settings import showSettings
from settings_frame import SettingsFrame
from gravity import GravityFrame
from gravitational_force import GravitationalFrame
from motion import MotionFrame
def main():
    root = tk.Tk()
    root.title("Physics app")
    #make frames
    global precision
    precision = tk.IntVar(value=2)
    home_frame = tk.Frame(root, bg="#7AA2E3")
    gravity_frame = GravityFrame(root,precision)
    gravitational_frame = GravitationalFrame(root,precision)
    motion_frame = MotionFrame(root,precision)
    settings_frame = SettingsFrame(root,precision)
    '''
    colors:
    darker blue/purple:#7AA2E3
    '''
    #styles
    button_style = ttk.Style()
    button_style.configure("Custom.TButton", background="blue", foreground="blue", font=("Helvetica", 10), padding=10)
    title_font = font.Font(family="Helvetica", size=12, weight="bold")
    #home page
    home_label = tk.Label(home_frame,bg="#7AA2E3", text="Home page", font=title_font, fg="white")
    home_label.grid(row=0, column=0)
    button_gravity = ttk.Button(home_frame,style="Custom.TButton", text="Surface Gravity Calculator", command=lambda: showSettings(home_frame,gravity_frame))
    button_gravity.grid(row=1, columnspan=2, sticky="ew")
    button_gravitational_force = ttk.Button(home_frame,style="Custom.TButton", text="Gravitational Force Calculator", command=lambda: showSettings(home_frame,gravitational_frame))
    button_gravitational_force.grid(row=2, columnspan=2)
    button_motion = ttk.Button(home_frame,style="Custom.TButton", text="Motion Calculator", command=lambda: showSettings(home_frame,motion_frame))
    button_motion.grid(row=3, columnspan=2)
    button_precision = ttk.Button(home_frame,style="Custom.TButton", text="Precision", command=lambda: showSettings(home_frame,settings_frame)) #switch to precision on click
    button_precision.grid(row=4, columnspan=2,sticky="ew")
    #***********************************************
    
    #show gravity_frame
    home_frame.grid(row=0,column=0,sticky="nsew")
    root.mainloop()
main()