from app_architecture import *
import tkinter as tk
import tkinter.messagebox as tm
from pwd_generator import *
import csv
import os


class PasswordVault(AppArchitecture, PasswordGen):
    # Class Attribute
    record = []

    def __init__(self, parent):
        # Initialization
        self.parent = parent
        PasswordVault.record = []

        # Architecture
        super().__init__(self.parent)

        # Variables
        self.site_var = tk.StringVar()
        self.user_var = tk.StringVar()
        self.password_var = tk.StringVar()

    def __call__(self):
        self.base_page()

    def base_page(self):
        """
        :return: The First Page to greet the User
        """
        # Labels
        label1 = tk.Label(self.parent, text="Welcome to Password Vault",
                          font=self.LARGE_FONTS)

        label_user = tk.Label(self.parent, text="username",
                              font=self.NORMAL_FONTS)

        label_site = tk.Label(self.parent, text="site name",
                              font=self.NORMAL_FONTS)

        label_password = tk.Label(self.parent, text="password",
                                  font=self.NORMAL_FONTS)

        label1.pack()
        label_site.place(x=5, y=45)
        label_user.place(x=5, y=65)
        label_password.place(x=5, y=85)

        # Entry Fields
        site_entry = tk.Entry(self.parent, font=self.SMALL_FONTS,
                              textvariable=self.site_var)
        user_entry = tk.Entry(self.parent, font=self.SMALL_FONTS,
                              textvariable=self.user_var)
        password_entry = tk.Entry(self.parent, font=self.SMALL_FONTS,
                                  textvariable=self.password_var)

        site_entry.place(x=85, y=45)
        user_entry.place(x=85, y=65)
        password_entry.place(x=85, y=85)

        # Buttons
        add_btn = tk.Button(self.parent, text="Add", command=self.add_details)
        add_more_btn = tk.Button(self.parent, text="Add More", command=self.add_more)
        generate_pwd_btn = tk.Button(self.parent, text="Generate Password",
                                     command=self.set_generated_pwd)
        save_btn = tk.Button(self.parent, text="Save",
                             command=self.save_details)

        generate_pwd_btn.place(x=90, y=100)
        add_btn.place(x=90, y=126)
        add_more_btn.place(x=135, y=126)
        save_btn.place(x=110, y=152)

    def add_details(self):
        add_lst = [self.site_var.get(),
                   self.user_var.get(),
                   self.password_var.get()]
        PasswordVault.record.append(add_lst)
        tm.showinfo("Confirmation", "Added Successfully")

    def add_more(self):
        add_lst = [self.site_var.get(),
                   self.user_var.get(),
                   self.password_var.get()]
        PasswordVault.record.append(add_lst)
        self.site_var.set("")
        self.user_var.set("")
        self.password_var.set("")

    def save_details(self):
        """
        Save the details into the default Excel Worksheet
        """
        if not os.path.isfile("data_entry.csv"):
            with open("data_entry.csv", "w", newline='') as file:
                write = csv.writer(file)
                write.writerow(["Site Name", "Username",
                                "Password"])
                write.writerows(PasswordVault.record)
                tm.showinfo("Confirmation", "Record(s) Saved Successfully")

        else:
            with open("data_entry.csv", "a", newline='') as file:
                write = csv.writer(file)
                write.writerows(PasswordVault.record)
                tm.showinfo("Confirmation", "Record(s) Saved Successfully")

    def set_generated_pwd(self):
        gen_pwd = self.final_pwd()
        self.password_var.set(value=gen_pwd)
