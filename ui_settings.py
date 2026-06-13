import tkinter as tk
from tkinter import messagebox
from profiles import load_profile, save_profile

profile = load_profile()


def open_settings_window():
    root = tk.Tk()
    root.withdraw()

    window = tk.Toplevel(root)
    window.title("Logitech Assistant")
    window.geometry("460x500")
    window.resizable(False, False)

    # ── PALETTE ─────────────────────────────────────────────
    BG       = "#111318"
    CARD     = "#1c1f26"
    BORDER   = "#2a2d35"
    ACCENT   = "#00b4d8"
    BADGE_BG = "#0a3d4f"
    TEXT     = "#e8eaf0"
    MUTED    = "#6b7280"
    GREEN    = "#22c55e"

    window.configure(bg=BG)
    macros = profile.get("macros", {})

    # ── HELPERS ─────────────────────────────────────────────
    def make_card():
        f = tk.Frame(window, bg=CARD,
                     highlightbackground=BORDER, highlightthickness=1)
        f.pack(fill="x", padx=22, pady=(0, 12))
        return f

    def section_title(text):
        tk.Label(window, text=text,
                 font=("Segoe UI", 8, "bold"),
                 bg=BG, fg=ACCENT).pack(anchor="w", padx=22, pady=(4, 6))

    # ── HEADER ──────────────────────────────────────────────
    header = tk.Frame(window, bg=BG)
    header.pack(fill="x", padx=22, pady=(20, 0))

    icon_box = tk.Frame(header, bg=ACCENT, width=40, height=40)
    icon_box.pack_propagate(False)
    icon_box.pack(side="left")
    tk.Label(icon_box, text="G", font=("Segoe UI", 20, "bold"),
             bg=ACCENT, fg=BG).pack(expand=True, fill="both")

    meta = tk.Frame(header, bg=BG)
    meta.pack(side="left", padx=(12, 0))
    tk.Label(meta, text="Logitech Assistant",
             font=("Segoe UI", 14, "bold"), bg=BG, fg=TEXT).pack(anchor="w")
    tk.Label(meta, text="Mouse Configuration Panel",
             font=("Segoe UI", 9), bg=BG, fg=MUTED).pack(anchor="w")

    # Status dot (top-right)
    status = tk.Frame(header, bg=BG)
    status.pack(side="right")
    tk.Label(status, text="● Connected",
             font=("Segoe UI", 9), bg=BG, fg=GREEN).pack()

    # Divider
    tk.Frame(window, bg=BORDER, height=1).pack(fill="x", padx=22, pady=(16, 14))

    # ── MACROS ──────────────────────────────────────────────
    section_title("MACROS")
    card_m = make_card()

    macro_rows = [
        ("X1 Hold",       macros.get("x1_hold",  "—")),
        ("X2 Hold",       macros.get("x2_hold",  "—")),
        ("Middle Button", macros.get("middle",    "—")),
        ("Middle Button Hold", macros.get("middle_hold",    "—")),
    ]

    for idx, (lbl, val) in enumerate(macro_rows):
        row = tk.Frame(card_m, bg=CARD)
        row.pack(fill="x", padx=14, pady=10)

        tk.Label(row, text="●", font=("Segoe UI", 7),
                 bg=CARD, fg=ACCENT).pack(side="left", padx=(0, 10))

        tk.Label(row, text=lbl, font=("Segoe UI", 10),
                 bg=CARD, fg=TEXT, anchor="w", width=16).pack(side="left")

        badge = tk.Frame(row, bg=BADGE_BG)
        badge.pack(side="right")
        tk.Label(badge, text=str(val),
                 font=("Segoe UI", 9, "bold"),
                 bg=BADGE_BG, fg=ACCENT,
                 padx=12, pady=3).pack()

        if idx < len(macro_rows) - 1:
            tk.Frame(card_m, bg=BORDER, height=1).pack(fill="x", padx=14)

    # ── SETTINGS ────────────────────────────────────────────
    section_title("SETTINGS")
    card_s = make_card()

    top_row = tk.Frame(card_s, bg=CARD)
    top_row.pack(fill="x", padx=14, pady=(12, 2))

    tk.Label(top_row, text="Mouse Speed",
             font=("Segoe UI", 10), bg=CARD, fg=TEXT).pack(side="left")

    speed_var = tk.IntVar(value=profile.get("mouse_speed", 10))

    tk.Label(top_row, text="/ 20", font=("Segoe UI", 9),
             bg=CARD, fg=MUTED).pack(side="right")
    tk.Label(top_row, textvariable=speed_var,
             font=("Segoe UI", 12, "bold"),
             bg=CARD, fg=ACCENT, width=2, anchor="e").pack(side="right", padx=(0, 2))

    slider_row = tk.Frame(card_s, bg=CARD)
    slider_row.pack(fill="x", padx=14, pady=(2, 14))

    tk.Label(slider_row, text="1", font=("Segoe UI", 8),
             bg=CARD, fg=MUTED).pack(side="left", padx=(0, 4))

    tk.Scale(
        slider_row,
        from_=1, to=20,
        orient="horizontal",
        variable=speed_var,
        bg=CARD, fg=ACCENT,
        activebackground=ACCENT,
        highlightthickness=0,
        troughcolor=BORDER,
        showvalue=False,
        sliderlength=18,
        bd=0,
    ).pack(side="left", fill="x", expand=True)

    tk.Label(slider_row, text="20", font=("Segoe UI", 8),
             bg=CARD, fg=MUTED).pack(side="left", padx=(4, 0))

    # ── BUTTONS ─────────────────────────────────────────────
    btn_row = tk.Frame(window, bg=BG)
    btn_row.pack(fill="x", padx=22, pady=(6, 22))

    def save_changes():
        profile["mouse_speed"] = speed_var.get()
        save_profile(profile)
        messagebox.showinfo("Saved", "Settings saved successfully!")

    def close_window():
        window.destroy()
        root.destroy()

    tk.Button(
        btn_row, text="Close",
        command=close_window,
        bg=CARD, fg=MUTED,
        font=("Segoe UI", 10),
        relief="flat", cursor="hand2",
        padx=18, pady=9, bd=0,
        activebackground=BORDER,
        activeforeground=TEXT,
    ).pack(side="left")

    tk.Button(
        btn_row, text="Save Changes",
        command=save_changes,
        bg=GREEN, fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat", cursor="hand2",
        padx=18, pady=9, bd=0,
        activebackground="#16a34a",
        activeforeground="white",
    ).pack(side="right")

    window.mainloop()