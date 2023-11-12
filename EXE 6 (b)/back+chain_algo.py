database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary"]
color = ["Green", "Yellow"]

def display():
    print("\n X is \n1.frog \n2.canary ", end='')
    print("\n Select One ", end='')

def main():
    print("*-----Backward--Chaining --- *", end='')
    display()
    x = int(input())
    print(" \n", end='')

    if x == 1:
        print(" Chance Of eating flies ", end='')
    elif x == 2:
        print(" Chance of shrimping ", end='')
    else:
        print("\n-------In Valid Option Select ------ ", end='')

    if x >= 1 and x <= 2:
        print("\n X is ", end='')
        print(knowbase[x-1], end='')
        print("\n1.green \n2.yellow")
        k = int(input())

        if k == 1 and x == 1: # frog0 and green1
            print(" yes it is in ", end='')
            print(color[0], end='')
            print(" colour and will ", end='')
            print(database[0])
        elif k == 2 and x == 2: # canary1 and yellow3
            print(" yes it is in", end='')
            print(color[1], end='')
            print(" Colour and will ", end='')
            print(database[1])
        else:
            print("\n -- InValid Knowledge Database", end='')

if __name__ == "__main__":
    main()
