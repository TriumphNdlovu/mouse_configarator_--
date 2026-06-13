# 🖱️ Logitech Mouse Configurator 0.1

A lightweight Python-based tool to customize Logitech mouse behavior, including:
- Hold-based macros
- Keyboard shortcuts
- Mouse sensitivity control
- System tray background control


# ⚙️ Installation

## 1. Install Python

Download Python from:
https://www.python.org/downloads/


## 2. Install dependencies

``` pip install hidapi pynput keyboard pystray pillow pyautogui ```


# 📦 Required libraries

## HID device access (mouse communication)
``` pip install hidapi pynput ```

## Keyboard automation
``` pip install keyboard ```

## System tray support
``` pip install pystray pillow ```


# 📁 Configuration (Profiles)

All settings are stored in the profiles/ folder.

## Example: profiles/default.json
``` json
{
    "mouse_speed": 18,
    "macros": {
        "x1_hold": "ctrl+c",
        "x2_hold": "ctrl+v",
        "middle": "win+shift+s",
        "middle_hold": "precision sensitivity"
    }
}
```

# 🧠 How it works

| Button | Action |
|--------|--------|
| X1 (hold 0.7s+) | Copy (Ctrl + C) |
| X2 (hold 0.7s+) | Paste (Ctrl + V) |
| Middle click | Snipping Tool |
| Middle (hold 0.7s+)  | Slows down|
you can add as many micros as you please using the config


# 🚀 Running on Startup (Windows)

## Step 1
Press Win + R

Type:
shell:startup

## Step 2
Create file: mouse_macros_startup.bat

Content:

@echo off
cd /d "C:\path\to\your\project"
pythonw main.py


# ⚠️ Important
- Replace the path with your actual project path
- Use pythonw so no console window opens

- Enable / disable macros at runtime


# 🛠️ Editing Macros

Edit this file:

profiles/default.json

You can change:
- button mappings
- hold actions
- system shortcuts

# 👨‍💻 Author
by @realtriumphndlovu@gmail.com 
Take KARE and Enjoy ;)
