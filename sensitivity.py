import ctypes

SPI_SETMOUSESPEED = 113

def set_mouse_speed(speed):
    """
    Speed range: 1-20
    Windows default is 10
    """

    speed = max(1, min(20, speed))

    ctypes.windll.user32.SystemParametersInfoA(
        SPI_SETMOUSESPEED,
        0,
        speed,
        0
    )

    # print(f"Mouse speed set to {speed}")