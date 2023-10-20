import tkinter as tk
import pyautogui
import time
import threading
import os

pyautogui.FAILSAFE = False
is_running = False

def move_cursor():
    while is_running:
        pyautogui.moveRel(4, 4)
        time.sleep(2)

def start_script():
    global is_running
    if not is_running:
        is_running = True
        t = threading.Thread(target=move_cursor)
        t.start()

def stop_script():
    global is_running
    is_running = False

# Bilgisayar adını al
computer_name = os.environ['COMPUTERNAME']

app = tk.Tk()
app.title("AMC")

# Bilgisayar adını gösteren etiket
computer_name_label = tk.Label(app, text="PC Name: " + computer_name)
computer_name_label.pack()

start_button = tk.Button(app, text="___Run___", command=start_script)
start_button.pack()

stop_button = tk.Button(app, text="___Stop___", command=stop_script)
stop_button.pack()

# Bilgisayar adı kontrolü
if computer_name not in ("DESKTOP-R904F1U", "DESKTOP-R933"):
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.DISABLED)
    
    error_label = tk.Label(app, text="The license key is incorrect. A valid license key is required to run the script.", fg="red", font=("Helvetica", 12, "bold"))
    error_label.pack()

app.mainloop()
