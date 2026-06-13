from mouse_detector import detect_logitech_devices
from mouse_listener import start_listener
from sensitivity import set_mouse_speed
from profiles import load_profile

profile = load_profile()

# print("=== Logitech Assistant v1 ===")

devices = detect_logitech_devices()

# for device in devices:
    # print(device)

set_mouse_speed(profile["mouse_speed"])

# print("Listening for mouse events...")
start_listener()