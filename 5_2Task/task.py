import tkinter
from tkinter import Tk, Radiobutton, IntVar
import RPi.GPIO as gpio

#===funcs===
def setup(pins):
    #sets up the pinboard
    gpio.setmode(gpio.BOARD)
    for pin in pins:
        gpio.setup(pin, gpio.OUT)

def led(val, pins):
    '''
    lights up an led and sets the rest low
    val is an interger index
    pins is a list of led pin numbers
    '''
    #set all pins to LOW
    for pin in pins:
        gpio.output(pin, 0)

    gpio.output(pins[val], 1)
        
#===vars===
PINS = [11,12,13]

#initialise tk window
top = Tk()
top.geometry('200x100')

#set up radio buttons
index = IntVar()
buttons = []
for i, Text in enumerate(["Red LED", "Orange LED", "Blue LED"]):
    buttons.append(Radiobutton(top, text=Text, variable=index, value=i, command=lambda: led(index.get(), PINS)))
    buttons[i].pack()

try:
    setup(PINS)
    top.mainloop()
except:
    gpio.cleanup()
    raise
gpio.cleanup()
