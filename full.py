#THIS IS THE FINAL VERSION LESGOOOO

import tkinter as tk
from tkinter import messagebox

class OrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Order App")
        
        self.total_price = 0
        self.my_order = {
            "sandwich type": '',
            "sandwich quantity": 0,
            "beverage size": '',
            "beverage quantity": 0,
            "fries size": '',
            "fries quantity": 0,
            "ketchup packets": 0
        }
        
        self.frames = {}
        self.create_frames()
        self.show_frame("sandwich_frame")

    def create_frames(self):
        self.frames["sandwich_frame"] = tk.Frame(self.root)
        self.create_sandwich_frame(self.frames["sandwich_frame"])

        self.frames["beverage_frame"] = tk.Frame(self.root)
        self.create_beverage_frame(self.frames["beverage_frame"])
        
        self.frames["fries_frame"] = tk.Frame(self.root)
        self.create_fries_frame(self.frames["fries_frame"])
        
        self.frames["ketchup_frame"] = tk.Frame(self.root)
        self.create_ketchup_frame(self.frames["ketchup_frame"])

        self.frames["final_frame"] = tk.Frame(self.root)
        self.create_final_frame(self.frames["final_frame"])

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack()

    def create_sandwich_frame(self, frame):
        tk.Label(frame, text="Select Sandwich Type:").pack()
        self.sandwich_var = tk.StringVar(value="chicken")
        tk.OptionMenu(frame, self.sandwich_var, "chicken", "beef", "tofu").pack()
        tk.Label(frame, text="Enter Sandwich Quantity:").pack()
        self.sandwich_quantity_entry = tk.Entry(frame)
        self.sandwich_quantity_entry.pack()
        tk.Button(frame, text="Next", command=self.add_sandwich).pack()

    def create_beverage_frame(self, frame):
        tk.Label(frame, text="Select Beverage Size:").pack()
        self.beverage_var = tk.StringVar(value="small")
        tk.OptionMenu(frame, self.beverage_var, "small", "medium", "large").pack()
        tk.Label(frame, text="Enter Beverage Quantity:").pack()
        self.beverage_quantity_entry = tk.Entry(frame)
        self.beverage_quantity_entry.pack()
        tk.Button(frame, text="Next", command=self.add_beverage).pack()

    def create_fries_frame(self, frame):
        tk.Label(frame, text="Select Fries Size:").pack()
        self.fries_var = tk.StringVar(value="small")
        tk.OptionMenu(frame, self.fries_var, "small", "medium", "large").pack()
        tk.Label(frame, text="Enter Fries Quantity:").pack()
        self.fries_quantity_entry = tk.Entry(frame)
        self.fries_quantity_entry.pack()
        tk.Button(frame, text="Next", command=self.add_fries).pack()

    def create_ketchup_frame(self, frame):
        tk.Label(frame, text="Enter Number of Ketchup Packets ($0.25 each):").pack()
        self.ketchup_entry = tk.Entry(frame)
        self.ketchup_entry.pack()
        tk.Button(frame, text="Next", command=self.add_ketchup).pack()

    def create_final_frame(self, frame):
        self.final_label = tk.Label(frame, text="")
        self.final_label.pack()
        tk.Button(frame, text="Finish", command=self.root.quit).pack()

    def add_sandwich(self):
        quantity = int(self.sandwich_quantity_entry.get())
        sandwich = self.sandwich_var.get()
        if sandwich == "chicken":
            self.total_price += 5.25 * quantity
        elif sandwich == "beef":
            self.total_price += 6.25 * quantity
        elif sandwich == "tofu":
            self.total_price += 5.75 * quantity
        self.my_order["sandwich type"] = sandwich
        self.my_order["sandwich quantity"] += quantity
        self.show_frame("beverage_frame")

    def add_beverage(self):
        quantity = int(self.beverage_quantity_entry.get())
        beverage = self.beverage_var.get()
        if beverage == "small":
            self.total_price += 1 * quantity
        elif beverage == "medium":
            self.total_price += 1.75 * quantity
        elif beverage == "large":
            self.total_price += 2.25 * quantity
        self.my_order["beverage size"] = beverage
        self.my_order["beverage quantity"] += quantity
        self.show_frame("fries_frame")


    def add_fries(self):
        quantity = int(self.fries_quantity_entry.get())
        fries = self.fries_var.get()
        if fries == "small":
            self.total_price += 1 * quantity
        elif fries == "medium":
            self.total_price += 1.50 * quantity
        elif fries == "large":
            self.total_price += 2 * quantity
        self.my_order["fries size"] = fries
        self.my_order["fries quantity"] += quantity
        self.show_frame("ketchup_frame")


    def add_ketchup(self):
        packets = int(self.ketchup_entry.get())
        self.total_price += 0.25 * packets
        self.my_order["ketchup packets"] += packets
        self.display_final_order()
        self.show_frame("final_frame")


    def display_final_order(self):
        #display the final order summary:
        order_summary = f"Your Order:\n"
        order_summary += f"- {self.my_order['sandwich quantity']} {self.my_order['sandwich type']} sandwich(es)\n"
        if self.my_order["beverage quantity"] > 0:
            order_summary += f"- {self.my_order['beverage quantity']} {self.my_order['beverage size']} beverage(s)\n"
        if self.my_order["fries quantity"] > 0:
            order_summary += f"- {self.my_order['fries quantity']} {self.my_order['fries size']} fries\n"
        if self.my_order["ketchup packets"] > 0:
            order_summary += f"- {self.my_order['ketchup packets']} ketchup packet(s)\n"
        order_summary += f"Total Price: ${self.total_price:.2f}"
        self.final_label.config(text=order_summary)

my_app = OrderApp(tk.Tk())
my_app.root.mainloop()
