from pynput import mouse
import time
from macros import execute_macro
from sensitivity import set_mouse_speed
import threading

HOLD_THRESHOLD = 0.7
middle_pressed = False
middle_pressed_time = 0
precision_active = False

press_times = {}
press_times_middle = {}

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


    if key == "middle":

        global middle_pressed
        global middle_pressed_time
        global precision_active

        if pressed:
            middle_pressed = True
            precision_active = False
            middle_pressed_time = time.time()

            threading.Thread(target=precision_monitor, daemon=True).start()

        else:
            middle_pressed = False

            duration = time.time() - middle_pressed_time

            # precision was active
            if precision_active:
                set_mouse_speed(13)
                precision_active = False
                print("Precision mode OFF")

            # tap action
            else:
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

def precision_monitor():
    global precision_active

    while middle_pressed:

        duration = time.time() - middle_pressed_time

        if duration >= HOLD_THRESHOLD and not precision_active:
            set_mouse_speed(2)
            precision_active = True

        time.sleep(0.01)