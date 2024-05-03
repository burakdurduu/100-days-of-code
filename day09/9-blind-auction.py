logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# import os
# clear = lambda: os.system('cls')
print(logo)
print("Welcome to the secret auction program. \n")

auction_dict = {}


def ah_calc(random_dict):
    max_bid = 0
    winner = ""
    for i in random_dict:
        new_bids = (random_dict[i])
        if new_bids > max_bid:
            max_bid = new_bids
            winner = i
    print(f"The winner is {winner} with a bid of ${max_bid}")


flag = True
while flag:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: "))
    auction_dict[name] = price
    input_continue = input("Are there any other bidders? Type 'yes' or 'no'. : ")
    if input_continue == "no":
        flag = False
        ah_calc(auction_dict)
    else:
        pass
        # clear()
