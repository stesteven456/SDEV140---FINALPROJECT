#SDEV 140
#Author: Steven Chen
#Version 1.0.0
#Write a GUI program 


#Imported Libraries
import tkinter as tk
import time
import math


# Dimensions of window size of Digital analog Clock
WIDTH = 400
HEIGHT = 400

# Creates the root window for the Tkiner Application using the variable "root" as the name to be referenced to
root = tk.Tk()
# Defines the title of the application
root.title("Analog Clock")
# Simplifies the process of calling back to the canvas module of Tkinter 
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
# Displays Tkinter canvas widget
canvas.pack()


# Defining the conditions of what allows the clock to basically "reload" itself so that it displays the current time
def update_clock():
    # Deletes all of the previously displayed information on the analog clock
    canvas.delete("all")
    # Records the current time stored in a varible referred to as "now"
    now = time.localtime()
    # Defining each data needed for th sake of creating a clock. Each variable below operates as a way to store the current time in the divided categories of hours, minutes, and seconds
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec
 
    # Draws clock face using a precoded "create_oval" method stored in the canvas class.
    canvas.create_oval(2, 2, WIDTH, HEIGHT, outline="black", width=2)
 
    # Draws hour numbers using a for loop
    for i in range(12):
        # Defining the value of the angular intervals between each number on an analog clock
        angle = i * math.pi/6 - math.pi/2
        # Defines the x-location of the digits
        x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(angle)
        # Defines the x-location of the digits
        y = HEIGHT/2 + 0.7 * WIDTH/2 * math.sin(angle)
        # Uses stored data created by the formulas above to dictate the exact locations of the displayed digits of the analog clock.
        if i == 0:
            canvas.create_text(x, y-10, text=str(i+12), font=("Helvetica", 12))
        else:
            canvas.create_text(x, y, text=str(i), font=("Helvetica", 12))
 
    # Draws minute lines
    for i in range(60):
        # Defining the value of the angular intervals between each minute on an analog clock
        angle = i * math.pi/30 - math.pi/2
        # Defines the end and beginning points of the each minute line
        x1 = WIDTH/2 + 0.8 * WIDTH/2 * math.cos(angle)
        y1 = HEIGHT/2 + 0.8 * HEIGHT/2 * math.sin(angle)
        x2 = WIDTH/2 + 0.9 * WIDTH/2 * math.cos(angle)
        y2 = HEIGHT/2 + 0.9 * HEIGHT/2 * math.sin(angle)
        # Defines every fifth line as a bolder line and every other line a thinner line
        if i % 5 == 0:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
        else:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=1)
 
    # Draws hour hand
    hour_angle = (hour + minute/60) * math.pi/6 - math.pi/2
    hour_x = WIDTH/2 + 0.5 * WIDTH/2 * math.cos(hour_angle)
    hour_y = HEIGHT/2 + 0.5 * HEIGHT/2 * math.sin(hour_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, hour_x, hour_y, fill="black", width=6)
 
    # Draws minute hand
    minute_angle = (minute + second/60) * math.pi/30 - math.pi/2
    minute_x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(minute_angle)
    minute_y = HEIGHT/2 + 0.7 * HEIGHT/2 * math.sin(minute_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, minute_x, minute_y, fill="black", width=4)
 
    # Draws second hand
    second_angle = second * math.pi/30 - math.pi/2
    second_x = WIDTH/2 + 0.6 * WIDTH/2 * math.cos(second_angle)
    second_y = HEIGHT/2 + 0.6 * WIDTH/2 * math.sin(second_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, second_x, second_y, fill="red", width=2)
 
    canvas.after(1000, update_clock)
 
update_clock()
root.mainloop()