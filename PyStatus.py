# you need to install the busylight http app first
# 
# https://www.plenom.com/downloads/download-software/#tab-f8e88e2f7eaf18f25df
import tkinter as tk
import requests

def send_request(color):
    params = {
        'action': 'light',
        'red': 0,
        'green': 0,
        'blue': 0
    }
    
    if color == 'red':
        params.update({'red': 100})
    elif color == 'green':
        params.update({'green': 100})
    elif color == 'purple':
        params.update({'red': 50, 'blue': 50})
    elif color == 'yellow':
        params.update({'red': 100, 'green': 100})
    
    response = requests.get("http://localhost:8989/", params=params)
    print(f"Response Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    print(f"{color}")
    
def send_request_pulse(color):
    params = {
        'action': 'pulse',
        'red': 0,
        'green': 0,
        'blue': 0
    }
    
    if color == 'red':
        params.update({'red': 100})
    elif color == 'green':
        params.update({'green': 100})
    elif color == 'purple':
        params.update({'red': 50, 'blue': 50})
    elif color == 'yellow':
        params.update({'red': 100, 'green': 100})
    
    response = requests.get("http://localhost:8989/", params=params)
    print(f"Response Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    print(f"{color} pulsing")

# Initialize Tkinter window
root = tk.Tk()
root.title("PyStatus")
root.wm_attributes('-topmost', 1)
root.resizable(False,False)

# Create buttons
button_red = tk.Button(root, bg='red', width=7, height=1, command=lambda: send_request('red'))
button_green = tk.Button(root, bg='green', width=7, height=1, command=lambda: send_request('green'))
button_purple = tk.Button(root, bg='purple', width=7, height=1, command=lambda: send_request('purple'))
button_yellow = tk.Button(root, bg='yellow', width=7, height=1, command=lambda: send_request('yellow'))
button_RedPulse = tk.Button(root, text='Pulse', width=7, height=1, command=lambda: send_request_pulse('red'))
button_GreenPulse = tk.Button(root, text='Pulse', width=7, height=1, command=lambda: send_request_pulse('green'))
button_YellowPulse = tk.Button(root, text='Pulse', width=7, height=1, command=lambda: send_request_pulse('yellow'))
button_PurplePulse = tk.Button(root, text='Pulse', width=7, height=1, command=lambda: send_request_pulse('purple'))



# Pack buttons onto window
# button_red.pack(side=tk.LEFT)
# button_green.pack(side=tk.LEFT)
# button_purple.pack(side=tk.LEFT)
# button_yellow.pack(side=tk.LEFT)
# button_RedPulse.pack(side=tk.LEFT)
# button_GreenPulse.pack(side=tk.LEFT)
# button_YellowPulse.pack(side=tk.LEFT)
# button_PurplePulse.pack(side=tk.LEFT)
button_red.grid(row=0, column=0)
button_green.grid(row=0, column=1)
button_purple.grid(row=0, column=2)
button_yellow.grid(row=0, column=3)

button_RedPulse.grid(row=1, column=0)
button_GreenPulse.grid(row=1, column=1)
button_PurplePulse.grid(row=1, column=2)
button_YellowPulse.grid(row=1, column=3)


# Start Tkinter event loop
root.mainloop()

