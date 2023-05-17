import tkinter as tk
import datetime, os
from tools.jsonmaker import jsonMaker
from tools.jsonreader import jsonReader
from tkinter import ttk

cwd = os.getcwd()

jsonwriter = jsonMaker(cwd)
jsonreader = jsonReader(cwd)

def start_work_click():
    date = str(datetime.date.today())
    current_data = jsonreader.read(date)
    if current_data == {}:
        current_data = jsonwriter.create_new()
        print("Created new json")

    # JSON file operations
    idx = int(current_data["markings_count"])
    current_data["work_times"].append({})
    current_data["work_times"][idx]["start"] = str(datetime.datetime.now().time())
    current_data["markings_count"] = current_data["markings_count"] + 1

    current_data = jsonwriter.save(current_data)
    print("Start work clicked!")

    button_endwork.state(["!disabled"])
    button_startwork.state(["disabled"])


def end_work_click():
    date = str(datetime.date.today())
    current_data = jsonreader.read(date)

    idx = int(current_data["markings_count"]) - 1
    current_data["work_times"][idx]["end"] = str(datetime.datetime.now().time())

    current_data = jsonwriter.save(current_data)
    print("End work clicked!")

    button_startwork.state(["!disabled"])
    button_endwork.state(["disabled"])


def on_button3_click():
    print("Button 3 clicked!")


def set_button_states():
    # This gets played at first.
    if jsonreader.readMarkingStatus(str(datetime.date.today())):
        button_startwork.state(["!disabled"])
        button_endwork.state(["disabled"])
    else:
        button_endwork.state(["!disabled"])
        button_startwork.state(["disabled"])

# Create the main window
root = tk.Tk()
root.title("Histogram GUI")

# Create a frame for the histogram screen
histogram_frame = ttk.Frame(root)
histogram_frame.pack(padx=10, pady=10)

# Create buttons
button_startwork = ttk.Button(root, text="Start work", command=start_work_click)
button_startwork.pack(side=tk.LEFT, padx=5, pady=5)

button_endwork = ttk.Button(root, text="End work", command=end_work_click, state="disabled")
button_endwork.pack(side=tk.LEFT, padx=5, pady=5)

button3 = ttk.Button(root, text="Button 3", command=on_button3_click)
button3.pack(side=tk.LEFT, padx=5, pady=5)

set_button_states()

# Create a disabled slider
slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", state="disabled")
slider.pack(padx=10, pady=10)

slider.state(["!disabled"])

# Start the main event loop
root.mainloop()