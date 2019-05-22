from tkinter import *
from time import sleep
import RPi.GPIO as gpio


        
#===vars===
pin = 13
MORSE = {'A': '.-',     'B': '-...',   'C': '-.-.',
         'D': '-..',    'E': '.',      'F': '..-.',
         'G': '--.',    'H': '....',   'I': '..',
         'J': '.---',   'K': '-.-',    'L': '.-..',
         'M': '--',     'N': '-.',     'O': '---',
         'P': '.--.',   'Q': '--.-',   'R': '.-.',
         'S': '...',    'T': '-',      'U': '..-',
         'V': '...-',   'W': '.--',    'X': '-..-',
         'Y': '-.--',   'Z': '--..',   ' ': ' '}

#===funcs===
def setup(pins):
    #sets up the pinboard
    gpio.setmode(gpio.BOARD)
    for pin in pins:
        gpio.setup(pin, gpio.OUT)

def blink_morse(component):
    UNIT = 0.1
    if component == '.':
        #dot
        gpio.output(13, 1)
        sleep(UNIT)
    if component == '-':
        #dash
        gpio.output(13, 1)
        sleep(UNIT*3)
    if component == '_':
        #letter space
        sleep(UNIT*2)
    if component == ' ':
        #word space
        sleep(UNIT*6)

    gpio.output(13, 0)
    sleep(UNIT)
    
#initialise tk window
top = Tk()
top.geometry('500x100')

var = StringVar()
entry = Entry(top, textvariable=var)
entry.pack()

def submit():
    text = var.get().upper()
    if len(text) > 12:
        return
    
    morse_text = ''
    prev_c = ''
    for c in text:
        morse_text += MORSE[c]
        if c != ' ':
            morse_text += '_'

    print(morse_text)
    for component in morse_text:
        blink_morse(component)

    

button = Button(top, text='Print to morse', command=submit)
button.pack()


try:
    setup([pin])
    top.mainloop()
except:
    gpio.cleanup()
    raise
gpio.cleanup()
