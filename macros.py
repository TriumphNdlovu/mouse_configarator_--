import keyboard

macros = {
    "Button.x1": "ctrl+c",
    "Button.x2": "ctrl+v"
}

def execute_macro(button_name):
    if button_name in macros:
        keyboard.send(macros[button_name])
        print(f"Executed macro: {macros[button_name]}")