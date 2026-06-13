from pynput import mouse
from macros import execute_macro

def on_click(x, y, button, pressed):
    if pressed:
        print(f"{button} Pressed")
        execute_macro(str(button))

def start_listener():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()