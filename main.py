import tkinter as tk
from tkinter import ttk #button styles
from settings import showSettings
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
    #styles
    button_style = ttk.Style()
    button_style.configure("Custom.TButton", background="blue", foreground="blue", font=("Helvetica", 12), padding=10)

    #home page
    home_label = tk.Label(home_frame, text="Home page")
    home_label.grid(row=0, column=0)
    button_gravity = ttk.Button(home_frame,style="Custom.TButton", text="Gravity calculator", command=lambda: showSettings(home_frame,gravity_frame))
    button_gravity.grid(row=1, columnspan=2)
    button_precision = ttk.Button(home_frame,style="Custom.TButton", text="Precision", command=lambda: showSettings(home_frame,settings_frame)) #switch to precision on click
    button_precision.grid(row=2, columnspan=2,sticky="ew")
    #***********************************************
    
    #show gravity_frame
    home_frame.grid(row=0,column=0,sticky="nsew")
    root.mainloop()
main()