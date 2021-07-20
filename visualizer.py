# // <!--
# //  ============================
# //  @Author  :        Raja Durai M
# //  @Version :        1.0
# //  @Date    :        20 Jul 2021
# //  @Detail  :        visualizer_main
# //  ============================
# //  -->

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time

from bubblesort import bubble_sort
from selectionsort import  selection_sort
from insertionsort import insertion_sort
from mergesort import merge_sort
from quicksort import  quick_sort
from linearSearch import linear_search
from binarySearch import binary_search


root = Tk()
root.title("Sorting & Searching Algorithm Visulaiser")
root.maxsize(1000,600)
# background color
root.config(bg="grey")

# variable
selected_algo = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 20
    spacing = 10
    normalizedData = [ i / max(data) for i in data] #here i is data and not index
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340    # y is calculated from the top
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))  # anchor used to choose relative direction to that point.
                                                                    # Here SW is South West
    root.update_idletasks() #Calls all pending idle tasks, without processing any other events.

def Generate(): #
    global data
    try:
        minVal = max(int(minEntry.get()),0)
    except:
        minVal = 3
    try:
        maxVal = min(int(maxEntry.get()),1000)
    except:
        maxVal = 1000
    try:
        size = min(200,int(sizeEntry.get()))
        if size < 0:
            size=200
    except:
        size = 200

    data = []
    # generating random list
    color=[]
    for _ in range (size):
        data.append(random.randrange(minVal, maxVal + 1))
        color.append('blue')

    drawData(data, color)

def StartAlgorithm():
    global data
    speed=int(speedScale.get())
    if speed==2:
        speed=1.5
    elif speed == 3:
        speed = 0.1
    elif speed == 4:
        speed = 0.05
    elif speed == 5:
        speed = 0.01
    elif speed == 6:
        speed = 0.005
    elif speed == 7:
        speed = 0.001

    search = int(searchEntry.get())
    if selected_algo.get() == "Bubble Sort" :
        bubble_sort(data, drawData, speed)
    elif selected_algo.get() == "Selection Sort" :
        selection_sort(data, drawData, speed)
    elif selected_algo.get() == "Insertion Sort" :
        insertion_sort(data, drawData, speed)
    elif selected_algo.get() == "Merge Sort" :
        merge_sort(data, 0, len(data)-1, drawData, speed)
        drawData(data, ['light green' for x in range(len(data))])
        time.sleep(speed)
    elif selected_algo.get() == "Quick Sort" :
        quick_sort(data, drawData, speed)
    elif algMenu.get() == 'Linear Search':
        linear_search(data, search, drawData, speedScale.get())
    elif algMenu.get() == 'Binary Search':                          #calling Merge Sort before calling binary search
        merge_sort(data, 0, len(data)-1, drawData, speed)
        drawData(data, ['red' for x in range(len(data))])
        binary_search(data, search, drawData, speedScale.get())

def mabout():
    messagebox._show(title="Developers Info", _icon=None, message="Murarry and Raja Durai \n from NITT 2018 Batch")

# frame / base layout
UI_frame = Frame(root, width=600, height=200, bg='blue')
UI_frame.grid(row=0,column=0, padx=0 ,pady=5)

canvas = Canvas(root, width=800, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface

# row[0]
# data Size
Label(UI_frame , text="Size of Data : " , bg='yellow').grid(row=0, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# min data value
Label(UI_frame , text="Minimum Value: " , bg='yellow').grid(row=0, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

# max data value
Label(UI_frame , text="Maximum Value: " , bg='yellow').grid(row=0, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=0, column=5, padx=5, pady=5, sticky=W)

# Generate button
Button(UI_frame, text="Generate", command=Generate, bg='orange').grid(row=0, column=6, padx=5, pady=5)

# row[1]
Label(UI_frame , text="Select Algorithm" , bg='yellow').grid(row=1, column=0, padx=5, pady=5, sticky=W)

# Drop down listbox for algorithm
algMenu=ttk.Combobox(UI_frame, textvariable=selected_algo, values=['Linear Search', 'Binary Search','Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort'])
algMenu.grid(row=1, column=1, padx=5, pady=5)

# If nothing is selected, then by default, value is the first option
algMenu.current(0)

# speed scale
searchEntry = Scale(UI_frame, from_=1, to=100, resolution=1, orient=HORIZONTAL, label="Search Value", bg = "lightgreen")
searchEntry.grid(row=1, column=3, padx=5, pady=5)
speedScale = Scale(UI_frame,from_=1, to=7, length=200, digits=2, resolution=1, orient=HORIZONTAL, label="Select Speed :", bg="pink")
speedScale.grid(row=1, column=2, padx=5, pady=5)
# start button
Button(UI_frame, text="Visualize", command=StartAlgorithm, bg='orange').grid(row=1, column=4, padx=5, pady=5)
# Developers Info
Button(UI_frame, text="Developer Info", command=mabout, bg='red').grid(row=1, column=5, padx=5, pady=5)

root.mainloop()