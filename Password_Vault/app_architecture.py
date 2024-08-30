import tkinter.font as tfont


class AppArchitecture:

    def __init__(self, parent):
        self.parent = parent
        self.layout()

        self.LARGE_FONTS = tfont.Font(family="Arial", size=15, weight="bold")
        self.NORMAL_FONTS = tfont.Font(family="Helvetica", size=10, weight="normal")
        self.SMALL_FONTS = tfont.Font(family="Vedanta", size=7, weight="normal")

    def layout(self):
        self.parent.wm_title("Password Vault")
        self.parent.geometry("270x180")
