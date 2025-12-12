import time
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("350x300")
root.title("Time Counter & Stopwatch")

image = Image.open("assets/image.jpg")  
image = image.resize((350, 300))
img = ImageTk.PhotoImage(image)

canvas = Canvas(root, width=300, height=250, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor=NW, image=img)

heading = Label(root, text="TIME COUNTDOWN & STOPWATCH", font=("Arial", 14, "bold"))
heading.place(x=10, y=30)

hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(root, width=3, font=("Arial", 25, ""), textvariable=hour, justify="center")
hourEntry.place(x=70, y=100)

minuteEntry = Entry(root, width=3, font=("Arial", 25, ""), textvariable=minute, justify="center")
minuteEntry.place(x=145, y=100)

secondEntry = Entry(root, width=3, font=("Arial", 25, ""), textvariable=second, justify="center")
secondEntry.place(x=220, y=100)

running = False
stopwatch_running = False
stopwatch_start_time = 0
stopwatch_pause_time = 0

def submit():
    global running
    try:
        # the input provided by the user is stored in here: temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
        return
    
    running = True
    while temp >= 0 and running:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            hours, mins = divmod(mins, 60)
        hour.set("{0:02d}".format(hours))
        minute.set("{0:02d}".format(mins))
        second.set("{0:02d}".format(secs))
        root.update()
        time.sleep(1)
        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's up")
            break
        temp -= 1

def stop():
    global running
    running = False

def reset():
    hour.set("00")
    minute.set("00")
    second.set("00")

def start_stopwatch():
    global stopwatch_running, stopwatch_start_time, stopwatch_pause_time
    if not stopwatch_running:
        if stopwatch_pause_time == 0:
            stopwatch_start_time = time.time()
        else:
            stopwatch_start_time += time.time() - stopwatch_pause_time
        stopwatch_running = True
        update_stopwatch()

def stop_stopwatch():
    global stopwatch_running, stopwatch_pause_time
    stopwatch_running = False
    stopwatch_pause_time = time.time()

def resume_stopwatch():
    global stopwatch_running, stopwatch_start_time, stopwatch_pause_time
    if not stopwatch_running:
        stopwatch_start_time += time.time() - stopwatch_pause_time
        stopwatch_running = True
        update_stopwatch()

def update_stopwatch():
    if stopwatch_running:
        elapsed_time = int(time.time() - stopwatch_start_time)
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        hour.set("{:02d}".format(hours))
        minute.set("{:02d}".format(minutes))
        second.set("{:02d}".format(seconds))
        root.after(1000, update_stopwatch)

btn_start = Button(root, text='Start Countdown', bd='2.5', command=submit)
btn_start.place(x=8, y=180)

btn_stop = Button(root, text='Stop Countdown', bd='2.5', command=stop)
btn_stop.place(x=123, y=180)

btn_reset = Button(root, text='Reset Countdown', bd='2.5', command=reset)
btn_reset.place(x=238, y=180)

btn_start_stopwatch = Button(root, text='Start Stopwatch', bd='2.5', command=start_stopwatch)
btn_start_stopwatch.place(x=15, y=220)

btn_stop_stopwatch = Button(root, text='Stop Stopwatch', bd='2.5', command=stop_stopwatch)
btn_stop_stopwatch.place(x=120, y=220)

btn_resume_stopwatch = Button(root, text='Resume Stopwatch', bd='2.5', command=resume_stopwatch)
btn_resume_stopwatch.place(x=225, y=220)

root.mainloop()
