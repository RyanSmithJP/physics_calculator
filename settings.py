def showSettings(frame1, frame2):
    global lastFrame
    frame1.grid_forget()
    frame2.grid(row=0,column=0,sticky='nsew')
    lastFrame = frame1
def goBack(frame):
    frame.grid_forget()
    lastFrame.grid(row=0,column=0,sticky='nsew')