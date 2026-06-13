import threading
import pystray
from pystray import MenuItem, Menu
from PIL import Image, ImageDraw

from mouse_listener import start_listener, stop_listener
from mouse_detector import detect_logitech_devices
from profiles import load_profile
from ui_settings import open_settings_window


# ── STARTUP ─────────────────────────────────────────────────
profile = load_profile()
devices = detect_logitech_devices()

# ── STATE ───────────────────────────────────────────────────
tray_icon: pystray.Icon | None = None
running = False


# ── ICONS ───────────────────────────────────────────────────
def _make_icon(fill: tuple, size: int = 64) -> Image.Image:
    """Smooth circular tray icon with a soft highlight dot."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = 3
    draw.ellipse([pad, pad, size - pad, size - pad], fill=(*fill, 255))
    # Subtle top-left highlight
    h = size // 5
    draw.ellipse(
        [pad + h, pad + h, pad + h * 2, pad + h * 2],
        fill=(255, 255, 255, 70),
    )
    return img


def _active_icon()   -> Image.Image: return _make_icon((34, 197, 94))   # green-500
def _inactive_icon() -> Image.Image: return _make_icon((100, 116, 139)) # slate-500


# ── HELPERS ─────────────────────────────────────────────────
def open_ui_thread():
    threading.Thread(target=open_settings_window, daemon=True).start()


# ── ACTIONS ─────────────────────────────────────────────────
def start_macros(icon=None, menu_item=None):
    global running
    if running:
        return
    running = True
    start_listener()
    tray_icon.icon = _active_icon()
    tray_icon.title = "Logitech Assistant — Active"


def stop_macros(icon=None, menu_item=None):
    global running
    if not running:
        return
    running = False
    stop_listener()
    tray_icon.icon = _inactive_icon()
    tray_icon.title = "Logitech Assistant — Inactive"


def exit_app(icon, menu_item):
    stop_macros()
    icon.stop()


# ── MENU ────────────────────────────────────────────────────
def _build_menu() -> pystray.Menu:
    device_label = f"Device: {devices[0]["product"]}" if devices else "No device detected"

    return pystray.Menu(
        # Read-only status row — text updates dynamically each time menu opens
        MenuItem(
            lambda _: "● Macros active" if running else "○ Macros inactive",
            lambda *_: None,
            enabled=False,
        ),
        MenuItem(device_label, lambda *_: None, enabled=False),
        Menu.SEPARATOR,
        MenuItem("Enable",   start_macros, enabled=lambda _: not running),
        MenuItem("Disable",  stop_macros,  enabled=lambda _: running),
        Menu.SEPARATOR,
        MenuItem("Settings", lambda *_: open_ui_thread()),
        Menu.SEPARATOR,
        MenuItem("Exit", exit_app),
    )


# ── ENTRY ───────────────────────────────────────────────────
def setup_tray():
    global tray_icon
    tray_icon = pystray.Icon(
        name="logitech_assistant",
        icon=_inactive_icon(),
        title="Logitech Assistant — Inactive",
        menu=_build_menu(),
    )
    tray_icon.run()


if __name__ == "__main__":
    setup_tray()