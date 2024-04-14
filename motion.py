import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #tkinder integration
import numpy as np
from settings import goBack
class MotionFrame(tk.Frame):
    def __init__(self, master=None, precision=None, **kwargs):
        super().__init__(master, **kwargs) #initialise before modifying frame
        #Variables
        self.u_units = "ms" #use by default
        self.a_units = "ms²"
        self.t_units = "s"
        self.label_u = tk.Label(self, text=f"Initial speed ({self.u_units}):")
        self.label_u.grid(row=0, column=0)
        self.entry_u = tk.Entry(self)
        self.entry_u.grid(row=0, column=1)
        self.label_a = tk.Label(self, text=f"Acceleration ({self.a_units}):")
        self.label_a.grid(row=1, column=0)
        self.entry_a = tk.Entry(self)
        self.entry_a.grid(row=1, column=1)
        self.label_t = tk.Label(self, text=f"Time ({self.t_units}):")
        self.label_t.grid(row=2, column=0)
        self.entry_t = tk.Entry(self)
        self.entry_t.grid(row=2, column=1)
        #Units of measurement
        self.button_goBack = tk.Button(self, text="Go back", command=lambda: goBack(self)) #switch to precision on click
        self.button_goBack.grid(row=3, column=0)
        self.button_calculate = tk.Button(self, text="Calculate", command=lambda: self.calculate_final_speed(precision))
        self.button_calculate.grid(row=3, column=1)
        #result
        self.label_v_result = tk.Label(self, text="")
        self.label_v_result.grid(row=4, columnspan=2)
        #Matplotlib graph - make new frame
        self.graph_frame = tk.Frame(self)
        self.graph_frame.grid(row=5, columnspan=2)
        self.close_window()
    def calculate_final_speed(self,precision):
        try:
            u = float(self.entry_u.get())
            a = float(self.entry_a.get())
            t = float(self.entry_t.get())
            v = u+a*t
            self.label_v_result.config(text=f'Final speed = {v:.{precision.get()}f} m/s')
            self.label_v_result.grid(row=4, columnspan=2)
            self.plot_graph(u,v,t)
        except ValueError:
            self.label_v_result.config(text='Please enter valid parameters')
            self.label_v_result.grid(row=4, columnspan=2)
    def plot_graph(self,u,v,t):
            #graph result
            #integrate with tkinter check if canvas exists
            if hasattr(self,'canvas'):
                plt.clf()
            else:
                graph = plt.figure()
                self.canvas = FigureCanvasTkAgg(graph, master=self.graph_frame) #get graph
                self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True) #position
            plt.title("Change in velocity over time")
            plt.xlabel("Time (s)")
            plt.ylabel("Velocity (ms)")
            plt.grid(True)
            xpoints = np.array([0,t])
            ypoints = np.array([u,v])
            plt.plot(xpoints,ypoints)
            self.canvas.draw()
    def change_units(self,new_units):
        if(new_units=="m"):
            self.distance_units = "m"
        else:
            self.distance_units = "km"
        self.label_radius.config(text=f"Radius ({self.distance_units}):")
        self.label_g_result.grid_remove()
    def close_window(self): #reference delete_window then close events
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
    def on_close(self):
        plt.close() #close plot
        self.master.destroy() #destroy app
