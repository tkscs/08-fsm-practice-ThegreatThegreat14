#balance
#pick items and their stock and price
#restock
#enter different bills
#check current stock
#check last request prompt and answer choices
#undo selection
#add different item price
#restart if money 0

#guys this is reealliissticcc okay, that's why the system sucks
Money = 0
Item_1_Stock = 5
Item_2_Stock = 5
Selection = None

Request = input("Hello, I am a vending machine. Insert a dollar by replying D, select an item by replying S, purchase by replying B, and leave by replying E. ")
while True:
    if Request == "D":
        if Selection == "1" or Selection == "2":
            Request = input("You have an item selected. You cannot insert more money currently. What would you like to do now? ")
        else:
            Money = Money + 1
            Request = input(f"You have inserted 1 dollar. Your balance is now {Money}. What would you like to do now? ")
    elif Request == "S":
        if Selection == "1" or Selection == "2":
            Request = input("You have an item selected. You cannot make another selection currently. What would you like to do now? ")
        else:
            Item_Request = input("To select Item 1, which costs 2 dollars, reply with 1. To select Item 2, which costs 2 dollars, reply with 2. To leave the selection menu, reply E. ")
            while True:
                if Item_Request == "1":
                    if Item_1_Stock >= 1:
                        Selection = "1"
                        Request = input("You have selected item 1. What would you like to do now? ")
                        break
                    else:
                        Item_Request = input("This item is out of stock, please select something else. ")
                elif Item_Request == "2":
                    if Item_2_Stock >= 1:
                        Selection = "2"
                        Request = input("You have selected item 2. What would you like to do now? ")
                        break
                    else:
                        Item_Request = input("This item is out of stock, please select something else. ")
                elif Item_Request == "E":
                    Request = input(f"You have exited the selection menu. Your balance is {Money}. What would you like to do now? ")
                    break
                else:
                    Item_Request = input("Please reply with 1, 2, or E. ")
    elif Request == "B":
        if Selection == "1":
            if Money >= 2:
                Money = Money - 2
                Request = input("You have purchased Item 1. You can retrieve it from the small flap below. What would you like to do now? ")
                Item_1_Stock = Item_1_Stock - 1
                Selection = None
            else:
                Request = input("You do not have enough money to purchase Item 1. Your interaction with the vending machine has restarted, what would you like to do? ")
                Money = 0
                Selection = None
        elif Selection == "2":
            if Money >= 2:
                Money = Money - 2
                Request = input("You have purchased Item 2. You can retrieve it from the small flap below. What would you like to do now? ")
                Item_2_Stock = Item_2_Stock - 1
                Selection = None
            else:
                Request = input("You do not have enough money to purchase Item 2. Your interaction with the vending machine has restarted, what would you like to do? ")
                Money = 0
                Selection = None
        else:
            Request = input("You have not selected an item. You cannot make a purchase currently. What would you like to do now? ")
    elif Request == "E":
        print("Okay. Goodbye.")
        break
    else:
        Request = input("Please reply with D, S, B, or E. ")