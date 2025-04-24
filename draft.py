#WARNING: This code isn't really complete and may not run as expected. THIS IS NOT THE FULL VERSION, go to full.py

total_price = 0

my_order = {"sandwich type": '', "sandwich quantity": 0, "beverage size": 0, "beverage quantity": 0, "fries size": 0, "fries quantity": 0, "ketchup packets": 0}

def menu_sandwich():
    global total_price
    global sandwich

    sandwich = input("""What sandwich would you like to order:
                     - chicken ($5.25)
                     - beef ($6.25)
                     - tofu ($5.75) 
""")
    
    if sandwich.lower() == "chicken": 
        total_price += 5.25
        my_order["sandwich type"] = "chicken"
        my_order["sandwich quantity"] += 1
    elif sandwich.lower() == "beef":
        total_price += 6.25
        my_order["sandwich type"] = "beef"
        my_order["sandwich quantity"] += 1
    elif sandwich.lower() == "tofu":
        total_price += 5.75
        my_order["sandwich quantity"] += 1
    else:
        print("The sandwich choice is invalid!")
        return menu_sandwich()
    
print(menu_sandwich())





def menu_drink():
    global total_price
    global bev_choice
    global bev_size

    bev_choice = input("Would you like a drink with that? (yes/no): ")
    
    if bev_choice.lower() == "yes":
        bev_size = input("""What size beverage would you like:
                        - small ($1)
                        - medium ($1.75)
                        - large ($2.25)
""")
    
        if bev_size.lower() == "small":
            total_price += 1
            total_quantity["beverage"] += 1
        elif bev_size.lower() == "medium":
            total_price += 1.75
            total_quantity["beverage"] += 1
        elif bev_size.lower() == "large":
            total_price += 2.25
            total_quantity["beverage"] += 1
        else:
            print("That beverage size choice is invalid!")
            return menu_drink()
    
    
        
    else:
        
        return "You did not order a beverage."

print(menu_drink())





def menu_fries():
    global total_price
    global fries_choice
    global fries_size

    fries_choice = input("Would you like fries with that? (yes/no): ")
    
    if fries_choice.lower() == "yes":
        fries_size = input("""What size fries would you like:
                        - small ($1)
                        - medium ($1.50)
                        - large ($2)
""")
        if fries_size.lower() == "small":
            mega_choice = input("Do you want a mega-size instead? (yes/no): ")
            if mega_choice.lower() == "yes":
                fries_size = "large"
                total_price += 2
            else:
                total_price += 1
        
        elif fries_size.lower() == "medium":
            total_price += 1.50
        elif fries_size.lower() == "large":
            total_price += 2
        else:
            print("Your fries size choice is invalid!")
            return menu_fries()
        
        return "You have ordered a " + fries_size + " fries." 
        
    else:
        return "You did not order fries." 
    
print(menu_fries())




def menu_ketchup():
    global packet_num
    global total_price


    packet_num = input("How many ketchup packets would you like? ($0.25): ")

    if packet_num.isdigit() and int(packet_num) >= 0:
        total_price += 0.25 * int(packet_num)
        return "You have ordered " + packet_num + " ketchup packets." 
    else:
        print("The ketchup packet choice is invalid!")
        return menu_ketchup()

print(menu_ketchup())



def order_sum():
    global total_price
    global bev_choice
    global fries_choice
    global bev_size
    global fries_size
    global packet_num

    if bev_choice.lower() == "yes" and fries_choice.lower() == "yes":
        total_price -= 1.00
    
    print("You have ordered: " + "\n- " + sandwich + " sandwich." )
    if bev_choice.lower() == "yes":
        print("- " + bev_size + " beverage.")
    if fries_choice.lower() == "yes":
        print("- " + fries_size + " fries.")
    if packet_num.isdigit() and int(packet_num) >= 0:
        print("- " + packet_num + " ketchup packets.")
    
    
    return "Your total price is: $" + str(total_price)

print(order_sum())

