# colorfusion/colorfusion.py
class ColorFusion:
    def __init__(self):
        self.RED = "\033[91m"
        self.GREEN = "\033[92m"
        self.YELLOW = "\033[93m"
        self.BLUE = "\033[94m"
        self.MAGENTA = "\033[95m"
        self.CYAN = "\033[96m"
        self.WHITE = "\033[97m"
        self.RESET = "\033[0m"

    def colorize(self, text, color):
        return f"{color}{text}{self.RESET}"

fuse = ColorFusion()