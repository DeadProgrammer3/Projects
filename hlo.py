 import tkinter
try:
 import tkinter as tk
except ImportError:
 import Tkinter as tk
class Timer:
 def __init__(self, parent):

 self.seconds = 0
 # label displaying time
 self.label = tk.Label(parent, text="0 s", font="Arial 30", width=10)
 self.label.pack()
 # start the timer
 self.label.after(1000, self.refresh_label)
 def refresh_label(self):
