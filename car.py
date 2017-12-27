from tkinter import *
from time import gmtime, strftime, localtime, sleep
from pygame import mixer
from PIL import Image, ImageTk
from os import listdir
import datetime, json, os, requests

class auto:
    def __init__(self, master):
        self.master = master
        master.title("MemeOS Auto")

root = Tk()
root.resizable(0,0)
root.attributes("-fullscreen", True)

global screen_width
global screen_height

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

draw = Canvas(root, width=screen_width, height=screen_height, )
draw.pack()

background = draw.create_rectangle(0, 0, screen_width, screen_height, fill="black")

global timeDisplay
global dateDisplay

def load_json(file):
    with open(file) as data_file:
        date = json.load(data_file)
    return data

def initScreen():
    global timeDisplay
    global dateDisplay
    global screen_width
    global screen_height
    timeDisplay = draw.create_text(screen_width / 2, screen_height / 2 - 64, text="The time goes here.", font=("Ubuntu", 64), fill="white")
    dateDisplay = draw.create_text(screen_width / 2, screen_height / 2, text="The date goes here.", font=("Ubuntu"), fill="white")

def updateScreen():
    global timeDisplay
    global dateDisplay

    try:
        current_time = strftime("%I:%M")
        if(int(strftime("%H")) > 12):
            suffix = "PM"
        else:
            suffix = "AM"

        current_time = current_time + " " + suffix
        current_date = datetime.date.today().strftime("%B %d, %Y")

        draw.itemconfigure(timeDisplay, text=current_time)
        draw.itemconfigure(dateDisplay, text=current_date)
        draw.after(1000, updateScreen)
    except StopIteration:
        pass

def updateSoftware():
    r = requests.get("https://raw.github.com/wipsdafox/carputer/update.sh")
    directory = getcwd()
    filename = directory + 'update.sh'
    r = requests.get(url)
    f = open(filename,'w')
    f.write(r.content)
    os.system("chmod +x update.sh")
    subprocess.Popen(['/bin/bash', os.path.expanduser(filename)])
    sys.exit()

initScreen()
updateScreen()
ui = auto(root)
root.mainloop()
