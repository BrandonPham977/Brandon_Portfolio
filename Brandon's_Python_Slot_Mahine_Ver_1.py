### Brandon Python Slot Machine
import random
#Variables
wallet = 10
spin_counter = 0

output_list = ["@", "#", "7"]
output_1 = output_list[random.randrange(len(output_list))]
output_2 = output_list[random.randrange(len(output_list))]
output_3 = output_list[random.randrange(len(output_list))]

print("Welcome To Brandon Python Slot Machine!")
print("Here's 10 Coins On The House! ")
print("Cain Wallet = ", wallet)

def gamestart():
    global coin_input
    try:
        coin_input = int(input("Insert Coins (insert 0 to end game): "))
    except ValueError:
        print("Give Me A Number!")
        gamestart()

    if coin_input > wallet:
        print(coin_input, "Is Not Enough!")
        gamestart()
    elif coin_input == wallet:
        print("All Or Nothing Baby!")
        slot_spin()
    elif coin_input == 0:
        print("You Came Out With: ", wallet, "Coins!")
        print("See You Next Time!")
        quit()
    else:
        slot_spin()

def slot_spin():
    global coin_input
    global wallet
    global spin_counter
    wallet -= coin_input
    while coin_input > 0:
        global output_1
        output_1 = output_list[random.randrange(len(output_list))]
        global output_2
        output_2 = output_list[random.randrange(len(output_list))]
        global output_3
        output_3 = output_list[random.randrange(len(output_list))]

        coin_input = coin_input - 1
        spin_counter += 1

        print(f"     Spin:", spin_counter)
        print("     +=======+")
        print(f"     [", output_1, output_2, output_3, "]")
        print("     +=======+")

        if output_1 == output_2 and output_1 == output_3:
            wallet += 10
            print("     JACKPOT!!!!")
        else:
            print("     Better Luck Next Time!")
            print(" ")
        print("Wallet = ", wallet)

    if wallet == 0:
        print("     GAME OVER")
        quit()

    gamestart()

gamestart()

print("end")