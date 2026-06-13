import keyboard
from profiles import load_profile

profile = load_profile()

def execute_macro(button_name):
    macros = profile.get("macros", {})

    if button_name in macros:
        keyboard.send(macros[button_name])
        # print(f"Executed macro: {macros[button_name]}")