import tkinter as tk
from tkinter import messagebox

class SimpleOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Order App")
        self.root.configure(bg="light blue")
        
        # Dictionary for the menu items and their prices
        self.menu = {
            "Sandwiches": {
                "Chicken Sandwich": 5.25,
                "Beef Sandwich": 6.25,
                "Tofu Sandwich": 5.75,
            },

            "Drinks": {
                "Small Beverage": 1.00,
                "Medium Beverage": 1.75,
                "Large Beverage": 2.25,
            },

            "Appetizers": {
                "Small Fries": 1.00,
                "Medium Fries": 1.50,
                "Large Fries": 2.00,
            },
            
            "Sauces": {
                "Ketchup Packet": 0.25,
            }
        }
        
        self.order = {item: 0 for category in self.menu.values() for item in category}
        self.total_price = 0
        
        self.create_ui()

    def create_ui(self):
        for category, items in self.menu.items():
            # Add category title
            tk.Label(self.root, text=category, font=("Helvetica", 18, "bold"), bg="light blue").pack(anchor="w", padx=10, pady=5)
            
            for item, price in items.items():
                frame = tk.Frame(self.root, bg="light blue")
                frame.pack(anchor="w", padx=10, pady=5)
                
                tk.Label(frame, text=f"{item} (${price:.2f})", font=("Helvetica", 15), bg="light blue").pack(side="left")
                
                # Create a white box to wrap the quantity, plus, and minus buttons
                button_frame = tk.Frame(frame, bg="white", relief="solid", bd=1)
                button_frame.pack(side="left", padx=10)
                
                self.order[item] = tk.IntVar(value=0)
                quantity_label = tk.Label(button_frame, textvariable=self.order[item], font=("Helvetica", 15), bg="white")
                quantity_label.pack(side="left", padx=5)
                
                add_btn = tk.Button(button_frame, text="+", font=("Helvetica", 15), command=lambda i=item: self.update_quantity(i, 1))
                add_btn.pack(side="left", padx=5)
                
                subtract_btn = tk.Button(button_frame, text="-", font=("Helvetica", 15), command=lambda i=item: self.update_quantity(i, -1))
                subtract_btn.pack(side="left", padx=5)
        
        self.total_label = tk.Label(self.root, text="Total: $0.00", font=("Helvetica", 15), bg="light blue")
        self.total_label.pack(pady=10)
        
        tk.Button(self.root, text="Finish", font=("Helvetica", 15), command=self.finish_order).pack(pady=10)

    def update_quantity(self, item, change):
        current_quantity = self.order[item].get()
        new_quantity = max(0, current_quantity + change)
        self.order[item].set(new_quantity)
        self.update_total()

    def update_total(self):
        self.total_price = sum(self.menu[category][item] * self.order[item].get() for category in self.menu for item in self.menu[category])
        self.total_label.config(text=f"Total: ${self.total_price:.2f}")

    def finish_order(self):
        summary = "Your Order:\n"
        for item, quantity in self.order.items():
            if quantity.get() > 0:
                summary += f"- {item}: {quantity.get()}\n"
        summary += f"Total Price: ${self.total_price:.2f}"
        tk.messagebox.showinfo("Order Summary", summary)
        self.root.quit()

root = tk.Tk()
app = SimpleOrderApp(root)
root.mainloop()
