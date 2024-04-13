# settings_frame.py
import tkinter as tk
from tkinter import messagebox
from settings import goBack
class SettingsFrame(tk.Frame):
    def __init__(self, master=None, precision=None, **kwargs):
        super().__init__(master, **kwargs) #initialise before modifying frame
        precision_label = tk.Label(self, text='Set precision')
        precision_label.grid(row=0, column=0)
        self.entry_precision = tk.Entry(self,textvariable="")
        self.entry_precision.grid(row=0, column=1)
        old = self.entry_precision.get()

        self.label_precision_result = tk.Label(self, text="")
        self.label_precision_result.grid(row=1, columnspan=2)

        button_set_precision = tk.Button(self, text=" Set ", command=lambda:self.change_precision(self.label_precision_result,precision,self.entry_precision.get()))
        button_set_precision.grid(row=0, column=2, sticky="ew")

        back_button = tk.Button(self, text="Go back", command=lambda: goBack(self))
        back_button.grid(row=2,column=1, sticky="ew")
    def change_precision(self,label_precision_result,precision,entry_precision):
        '''
        Sets precision between 0 and 15
        '''
        try:
            precision_value = int(entry_precision)
            if 0 <= precision_value <= 15:
                # Proceed with the desired action
                messagebox.showinfo("Success", "Precision set successfully.")
                precision.set(entry_precision) #use .set because IntVar
            else:
                messagebox.showerror("Error", "Precision must be between 0 and 15.")
        except ValueError:
            messagebox.showerror("Error", "Invalid precision value. Please enter a valid integer.")
