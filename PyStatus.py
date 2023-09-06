# you need to install the busylight http app first


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
    
    response = requests.get("http://localhost:8989/", params=params)
    print(f"Response Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    
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
    
    response = requests.get("http://localhost:8989/", params=params)
    print(f"Response Code: {response.status_code}")
    print(f"Response Text: {response.text}")

# Initialize Tkinter window
root = tk.Tk()
root.title("Color Button App")
root.wm_attributes('-topmost', 1)

# Create buttons
button_red = tk.Button(root, bg='red', width=15, height=2, command=lambda: send_request('red'))
button_green = tk.Button(root, bg='green', width=15, height=2, command=lambda: send_request('green'))
button_purple = tk.Button(root, bg='purple', width=15, height=2, command=lambda: send_request('purple'))
button_pulse = tk.Button(root, text='Pulse', width=15, height=2, command=lambda: send_request_pulse('red'))



# Pack buttons onto window
button_red.pack(side=tk.LEFT)
button_green.pack(side=tk.LEFT)
button_purple.pack(side=tk.LEFT)
button_pulse.pack(side=tk.LEFT)

# Start Tkinter event loop
root.mainloop()
