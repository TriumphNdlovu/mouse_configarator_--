import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw

from mouse_listener import start_listener, stop_listener
from mouse_detector import detect_logitech_devices
from sensitivity import set_mouse_speed
from profiles import load_profile

# -----------------------
# LOAD CONFIG
# -----------------------
profile = load_profile()
devices = detect_logitech_devices()

set_mouse_speed(profile.get("mouse_speed", 10))

# -----------------------
# STATE
# -----------------------
tray_icon = None
running = False


# -----------------------
# ICONS
# -----------------------
def create_green_icon():
    image = Image.new("RGB", (64, 64), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill=(0, 255, 0))
    return image


def create_red_icon():
    image = Image.new("RGB", (64, 64), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill=(255, 0, 0))
    return image


# -----------------------
# START MACROS
# -----------------------
def start_macros(icon=None, item=None):
    global running, tray_icon

    if running:
        return

    running = True
    start_listener()

    tray_icon.icon = create_green_icon()
    tray_icon.title = "Logitech Assistant (ON)"

    print("Macros ENABLED")


# -----------------------
# STOP MACROS
# -----------------------
def stop_macros(icon=None, item=None):
    global running, tray_icon

    if not running:
        return

    running = False
    stop_listener()

    tray_icon.icon = create_red_icon()
    tray_icon.title = "Logitech Assistant (OFF)"

    print("Macros DISABLED")


# -----------------------
# EXIT APP
# -----------------------
def exit_app(icon, item):
    stop_macros()
    icon.stop()


# -----------------------
# TRAY SETUP
# -----------------------
def setup_tray():
    global tray_icon

    tray_icon = pystray.Icon(
        "Logitech Assistant",
        create_red_icon(),
        "Logitech Assistant (OFF)",
        menu=pystray.Menu(
            item("Enable Macros", start_macros),
            item("Disable Macros", stop_macros),
            item("Exit", exit_app)
        )
    )

    tray_icon.run()


# -----------------------
# MAIN
# -----------------------
if __name__ == "__main__":
    setup_tray()