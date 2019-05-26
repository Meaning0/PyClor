import platform
from color import Color

color = Color()

def print_red_text(text):
    if "Windows" in platform.platform():
        color.print_red_text(text)
    else:
        print('\033[31m这是前景色1')

def print_green_text(text):
    if "Windows" in platform.platform():
        color.print_green_text(text)
    else:
        print('\033[32m这是前景色1')
