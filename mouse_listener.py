from pynput import mouse
import time
from macros import execute_macro

HOLD_THRESHOLD = 0.7

press_times = {}

# store listener globally
listener = None


def on_click(x, y, button, pressed):
    btn = str(button)

    if btn == "Button.x1":
        key = "x1"
    elif btn == "Button.x2":
        key = "x2"
    elif btn == "Button.middle":
        key = "middle"
    else:
        return

    # middle click
    if key == "middle" and pressed:
        execute_macro("middle")
        return

    # hold logic
    if key in ["x1", "x2"]:

        if pressed:
            press_times[key] = time.time()

        else:
            if key not in press_times:
                return

            duration = time.time() - press_times[key]

            if duration >= HOLD_THRESHOLD:
                execute_macro(f"{key}_hold")

            del press_times[key]


def start_listener():
    global listener

    listener = mouse.Listener(on_click=on_click)
    listener.start()   # <-- non-blocking
    print("Listener started")


def stop_listener():
    global listener

    if listener is not None:
        listener.stop()
        listener = None
        print("Listener stopped")