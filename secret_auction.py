import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def secret_auction():
    bids = {}
    bidding_finished = False

    while not bidding_finished:
        clear_console()
        print("Welcome to the Secret Auction!")
        name = input("Enter your name: ")
        bid = int(input("Enter your bid: $"))
        bids[name] = bid

        more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
        if more_bidders.lower() == 'no':
            bidding_finished = True

    clear_console()
    highest_bid = 0
    winner = ""

    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}!")


# Run the secret auction
secret_auction()
