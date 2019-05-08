from tkinter import *
import tkinter as tk
import subprocess
import time
ct = 0
time = 9 
window = Tk()
 
window.title("TimeFrame")
 
window.geometry('350x200')
 
lbl = Label(window, text="Select Time Frame:")
 
lbl.grid(column=0, row=0)
class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="sd", width=10)
        self.label.pack()
        self.remaining = 0
#        self.countdown(10)
        
    def fifteen(self):
#        subprocess.call ('sudo -S shutdown -P +15', shell=True) 
        lbl.configure(text="15 Minutes to do work ")
        self.countdown(10)
    def thirty(self):
        subprocess.call ('sudo -S shutdown -P +30', shell=True)
        lbl.configure(text="30 Minutes to do work ")
        
    def fourtyfive(self):
        subprocess.call ('sudo -S shutdown -P +45', shell=True)
        lbl.configure(text="45 Minutes to do work ")
        
    def onehour(self):
        subprocess.call ('sudo -S shutdown -P +60', shell=True)
        lbl.configure(text="1 hour to do work ")
        
    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)       
        
if __name__ == "__main__":
    app = ExampleApp()
    btn = Button(window, text="15", command=app.fifteen)
    btn2 = Button(window, text="30", command=app.thirty)
    btn3 = Button(window, text="45", command=app.fourtyfive)
    btn4 = Button(window, text="60", command=app.onehour)
    btn.grid(column=1, row=0)
    btn2.grid(column=2, row=0)
    btn3.grid(column=3, row=0)
    btn4.grid(column=4, row=0)
    window.mainloop()
    
    app.mainloop()
