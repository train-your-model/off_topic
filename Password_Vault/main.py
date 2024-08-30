from source_code import PasswordVault
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordVault(parent=root)
    app()
    root.mainloop()
