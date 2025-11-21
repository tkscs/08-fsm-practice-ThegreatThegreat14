# states - black, white, red, put away
def Black():
    Light = "Off"
    Current_Input = input("enter smth")
    #experience state, collect input, transition to next state
    if Current_Input == "c":
        White()
    elif Current_Input == "h":
        Red()
    elif Current_Input == "n":
        Black()
    elif Current_Input == "p":
        Away()
    else:
        print(f"Error! I don't recognize the input {Current_Input}")
        Black()

def White():
    Light = "White"
    Current_Input = input("enter smth")
    #experience state, collect input, transition to next state
    if Current_Input == "c":
        Black()
    elif Current_Input == "h":
        Red()
    elif Current_Input == "n":
        White()
    elif Current_Input == "p":
        Away()
    else:
        print(f"Error! I don't recognize the input {Current_Input}")
        White()

def Red():
    Light = "Red"
    Current_Input = input("enter smth")
    #experience state, collect input, transition to next state
    if Current_Input == "c":
        Black()
    elif Current_Input == "h":
        White()
    elif Current_Input == "n":
        Red()
    elif Current_Input == "p":
        Away()
    else:
        print(f"Error! I don't recognize the input {Current_Input}")
        Red()

def Away():
    Light = "Away"