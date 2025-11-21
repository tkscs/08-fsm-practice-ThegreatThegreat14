# write code to implement a turnstile

State = None
Coin = 0
Experience = None

def Another(Experience):
    if Experience == None:
        return ("")
    elif Experience == "Returning":
        return ("nother")
    
def Still(Experience):
    if Experience == None:
        return ("")
    elif Experience == "Returning":
        return ("still ")

State = "Locked"
Request = input("Hello, this is a turnstile. Please respond C to insert a coin, P to push through, and N to leave. ")

while True:
    if State == ("Locked"):
        if Request == ("C"):
            Coin = Coin + 1
            State = ("Unlocked")
            Request = input(f"You have inserted a{Another(Experience)} coin. The turnstile is {Still(Experience)}unlocked. What would you like to do now? ")
            Experience = "Returning"
        elif Request == ("P"):
            State = "Locked"
            Request = input("The turnstile is locked. You need to enter a coin to unlock it. What would you like to do? ")
        elif Request == ("N"):
            print("Okay. Goodbye.")
            break
        else:
            Request = input("Please enter C, P, or N. ")

    elif State == ("Unlocked"):
        if Request == ("C"):
            Coin = Coin + 1
            State = ("Unlocked")
            Request = input(f"You have inserted a{Another(Experience)} coin. The turnstile is {Still(Experience)}unlocked. What would you like to do now? ")
            Experience = "Returning"
        elif Request == ("P"):
            Coin = 0
            State = "Locked"
            Request = input("You have pushed through the turnstile and entered to your destination. You continue on and at the end of the day have looped back to the turnstile. What would you like to do? ")
            Experience = None
        elif Request == ("N"):
            print("Okay. Goodbye.")
            break
        else:
            Request = input("Please enter C, P, or N. ")