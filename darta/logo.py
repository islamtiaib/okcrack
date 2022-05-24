import sys, os
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel
biru_m = '[bold cyan]'
hapus  = '[/]'


class Logo:

    def __init__(self):
        if "linux" in sys.platform.lower():
            try:os.system("clear")
            except:pass
        elif "win" in sys.platform.lower():
            try:os.system("cls")
            except:pass
        else:
            try:os.system("clear")
            except:pass

    def log(self):
        prints(Panel(f"""{biru_m} __  __        __  ______  ____{hapus}
{biru_m} \ \/ / ____  /  |/  / _ )/ __/ ® {hapus}|| Created By YayanXD X Chinda
{biru_m}  \  / /___/ / /|_/ / _  / _/     {hapus}|| Github.com/GoodboyC
{biru_m}  /_/       /_/  /_/____/_/ v3.0  {hapus}|| Facebook.com/KM39453"""))
