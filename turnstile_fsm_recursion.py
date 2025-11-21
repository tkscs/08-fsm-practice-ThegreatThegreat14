# write code to implement a turnstile

State = None
Coin = 0

def Locked():
    if Request == ("C"):
        Coin = Coin + 1
        Request = input(f"You have inserted a coin. The turnstile is unlocked. What would you like to do now? ")
        Unlocked()
    elif Request == ("P"):
        Request = input("The turnstile is locked. You need to enter a coin to unlock it. What would you like to do? ")
        Locked()
    elif Request == ("N"):
        print("Okay. Goodbye.")
    else:
        Request = input("Please enter C, P, or N. ")
        Locked()

def Unlocked():
    if Request == ("C"):
        Coin = Coin + 1
        Request = input(f"You have inserted another coin. The turnstile is still unlocked. What would you like to do now? ")
        Unlocked()
    elif Request == ("P"):
        Coin = 0
        Request = input("You have pushed through the turnstile and entered to your destination. You continue on and at the end of the day have looped back to the turnstile. What would you like to do? ")
        Locked()
    elif Request == ("N"):
        print("Okay. Goodbye.")
    else:
        Request = input("Please enter C, P, or N. ")
        Unlocked()

Request = input("Hello, this is a turnstile. Please respond C to insert a coin, P to push through, and N to leave. ")
Locked()