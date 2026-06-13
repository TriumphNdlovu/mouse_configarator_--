from pynput import mouse
import time
from macros import execute_macro

HOLD_THRESHOLD = 0.7  # 1 second hold

# store press timestamps
press_times = {}

def on_click(x, y, button, pressed):
    btn = str(button)

    # map mouse buttons
    if btn == "Button.x1":
        key = "x1"
    elif btn == "Button.x2":
        key = "x2"
    elif btn == "Button.middle":
        key = "middle"
    else:
        return

    # -------------------------
    # MIDDLE BUTTON (instant action)
    # -------------------------
    if key == "middle" and pressed:
        # print("Middle button pressed")
        execute_macro("middle")
        return

    # -------------------------
    # X1 / X2 HOLD LOGIC
    # -------------------------
    if key in ["x1", "x2"]:

        if pressed:
            press_times[key] = time.time()
            # print(f"{key} pressed")

        else:
            if key not in press_times:
                return

            duration = time.time() - press_times[key]
            # print(f"{key} released after {duration:.2f}s")

            # HOLD ACTION ONLY
            if duration >= HOLD_THRESHOLD:
                execute_macro(f"{key}_hold")
            # else:
                # TAP = DO NOTHING (default system behaviour)
                # print(f"{key} tap ignored (default OS behavior)")

            del press_times[key]


def start_listener():
    with mouse.Listener(on_click=on_click) as listener:
        # print("Logitech Assistant v1 running...")
        listener.join()