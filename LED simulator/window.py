# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:39:05 2016

@author: Gordan
"""

#%%
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
    
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

import numpy as np

class simGUI():
    def __init__(self,rows,cols):
        self.root = tk.Tk()
        
        self.leds = []
        self.vals = []
        for x in range(cols):
            self.leds.append([])
            self.vals.append([])
            for y in range(rows):
                self.vals[x].append(1)
                if x < (1/3.0)*cols:
                    self.leds[x].append(self.led(1,[x+1,y+1],'g'))
                elif x > (1/3.0)*cols and x < (2/3.0)*cols:
                    self.leds[x].append(self.led(1,[x+1,y+1],'b'))
                elif x > (2/3.0)*cols and x < cols:
                    self.leds[x].append(self.led(1,[x+1,y+1],'r'))
        
        self.fig1 = Figure(figsize=(5, 4), dpi=100)
        self.sub = self.fig1.add_subplot(111)
        
        self.canvas = FigureCanvasTkAgg(self.fig1, master=self.root)
        self.canvas = self.canvas.get_tk_widget().pack(side = tk.TOP)
        
        self.button1 = tk.Button(self.root,text='shiftZero',command=self.shiftZero)
        self.button1.pack(side = tk.LEFT)
        
        self.button2 = tk.Button(self.root,text='shiftOne',command=self.shiftOne)
        self.button2.pack(side = tk.LEFT)
        
        self.display()
        
        self.root.mainloop()
        
    def display(self):
        for cols in self.leds:
            for led in cols:
                if led.val == 1:
                    if led.color == 'g':
                        self.sub.plot(led.position[0],led.position[1],'go',markersize = 7)
                    if led.color == 'b':
                        self.sub.plot(led.position[0],led.position[1],'bo',markersize = 7)
                    if led.color == 'r':
                        self.sub.plot(led.position[0],led.position[1],'ro',markersize = 7)
                        
                else:
                    self.sub.plot(led.position[0],led.position[1],'wo',markersize = 7)
                self.sub.set_xlim(0,len(self.leds)+1)
                self.sub.set_ylim(0,len(self.leds[0])+1)
        self.fig1.canvas.draw()
        
    def updateLEDs(self):
        for x in range(len(self.leds)):
            for y in range(len(self.leds[0])):
                self.leds[x][y].val = self.vals[x][y]
        
    def shiftOne(self):
        self.vals.pop(-1)
        ones = []
        for rows in self.vals:
            ones.append(1)
        self.vals.insert(0,ones)
        self.updateLEDs()
        self.display()
        
    def shiftZero(self):
        self.vals.pop(-1)
        zeros = []
        for rows in self.vals:
            zeros.append(0)
        self.vals.insert(0,zeros)
        self.updateLEDs()
        self.display()
        
    class led():
        def __init__(self,val,position,color):
            self.val = val
            self.position = position
            self.color = color
        
#%%
simGUI(5,32)