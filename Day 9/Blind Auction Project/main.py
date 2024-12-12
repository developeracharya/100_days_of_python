import art
bidder_data = {}
# TODO-1: Ask the user for input
more_bidders = "yes"
print(art.logo)
while more_bidders == "yes":
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    more_bidders = input("Are there more bidders? Type 'yes' or 'no'.").lower()
    # TODO-2: Save data into dictionary {name: price}
    bidder_data[name] = bid
    # TODO-3: Whether if new bids need to be added
    if more_bidders == "no":
        highest_bid = 0
        highest_bidder = ""
        for name, bid in bidder_data.items():
            if bid > highest_bid:
                highest_bidder = name
                highest_bid = bid
        print(f"The winner is {highest_bidder} with a bid of {highest_bid}")
    # TODO-4: Compare bids in dictionary
    else:
        print("\n" * 20)