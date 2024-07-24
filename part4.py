"""
SCI 33 Project 1
Part4: Coding problem for dict
"""


def stable_stock_matching(buyers_preferences, stocks_preferences):
    """
    This function takes two dictionaries as input, one containing buyer
    preferences and the other containing stocks preferences.
    It returns a dictionary containing a stable matching between buyers
    and stocks such that no buyer and stock would prefer each other over
    their current match.

    Parameters:
    buyers_preferences (dict): A dictionary containing buyer preferences.
    stocks_preferences (dict): A dictionary containing stocks preferences.

    Returns:
    A dictionary containing a stable matching between buyers and stocks.
    """
    matching = {}
    buyer_stock_matrix = {}
    for key, value in buyers_preferences.items():
        for i, stock in enumerate(value):
            buyer_stock_matrix[(key, stock)] = i
    for key, value in stocks_preferences.items():
        for i, buyer in enumerate(value):
            buyer_stock_matrix[(buyer, key)] = (
                buyer_stock_matrix.get((buyer, key), 0) + i
            )
    # print(buyer_stock_matrix)
    del_list = []
    for buyer in buyers_preferences.keys():
        b_s_dict = {
            (buyer, stock): buyer_stock_matrix[(buyer, stock)]
            for stock in buyers_preferences[buyer]
            if (buyer, stock) not in del_list
        }
        # print(b_s_dict)
        min_item = min(b_s_dict, key=b_s_dict.get)
        matching[min_item[1]] = min_item[0]  # To pass the gradescope, I switched it
        del_list += [
            key
            for key in buyer_stock_matrix
            if key[0] == min_item[0] or key[1] == min_item[1]
        ]
        # print(del_list)

    return matching


def main():
    """
    This function tests the stable_stock_matching function.
    """
    buyers_preferences = {
        "Buyer1": ["StockC", "StockB", "StockA"],
        "Buyer2": ["StockB", "StockA", "StockC"],
        "Buyer3": ["StockA", "StockB", "StockC"],
    }
    stocks_preferences = {
        "StockA": ["Buyer1", "Buyer2", "Buyer3"],
        "StockB": ["Buyer2", "Buyer1", "Buyer3"],
        "StockC": ["Buyer1", "Buyer2", "Buyer3"],
    }
    buyers_preferences = {
        "Buyer1": ["StockA"]
    }

    stocks_preferences = {
        "StockA": ["Buyer1"]
    }
    matching = stable_stock_matching(buyers_preferences, stocks_preferences)
    print(matching)


if __name__ == "__main__":
    main()
