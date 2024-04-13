import tkinter as tk
from settings import showSettings
#from settings import goBack
from settings_frame import SettingsFrame
from gravity import GravityFrame
def main():
    root = tk.Tk()
    root.title("Physics app")
    #make frames
    global precision
    precision = tk.IntVar(value=2)
    home_frame = tk.Frame(root)
    gravity_frame = GravityFrame(root,precision)
    settings_frame = SettingsFrame(root,precision)

    home_label = tk.Label(home_frame, text="Home page")
    home_label.grid(row=0, column=0)
    button_gravity = tk.Button(home_frame, text="Gravity calculator", command=lambda: showSettings(home_frame,gravity_frame))
    button_gravity.grid(row=1, columnspan=2)
    button_precision = tk.Button(home_frame, text="Precision", command=lambda: showSettings(home_frame,settings_frame)) #switch to precision on click
    button_precision.grid(row=2, columnspan=2)
    #***********************************************
    
    #show gravity_frame
    home_frame.grid(row=0,column=0,sticky="nsew")
    root.mainloop()
main()