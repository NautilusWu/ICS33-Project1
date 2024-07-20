"""
SCI 33 Project 1
Part5: AoA(Extra credit) Analyze e time and space complexity for part4.py
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
        # Line 40 to 42 is a nested for loops.
        # Outer loop runs: O(B), where B is the number of buyers.
        # Inner loop runs: O(S), where S is the number of stocks.
        # Therefore, the time complexity of this part is O(B * S).
        # Size of buyer_stock_matrix is (B * S).
        # Therefore, the space complexity of this part is O(B * S).
        for key, value in stocks_preferences.items():
            for i, buyer in enumerate(value):
                buyer_stock_matrix[(buyer, key)] = (
                        buyer_stock_matrix.get((buyer, key), 0) + i
                )
        # Line 49 to 53 is a nested for loops.
        # Outer loop runs: O(S), where S is the number of stocks.
        # Inner loop runs: O(B), where B is the number of buyers.
        # Therefore, the time complexity of this part is O(S * B).
        # Size of buyer_stock_matrix is (B * S).
        # Therefore, the space complexity of this part is O(B * S).
        del_list = []
        for buyer in buyers_preferences.keys():
            b_s_dict = {
                (buyer, stock): buyer_stock_matrix[(buyer, stock)]
                for stock in buyers_preferences[buyer]
                if (buyer, stock) not in del_list
            }
            min_item = min(b_s_dict, key=b_s_dict.get)
            matching[min_item[1]] = min_item[0]
            del_list += [
                key
                for key in buyer_stock_matrix
                if key[0] == min_item[0] or key[1] == min_item[1]
            ]
        # Line 61 to 74 is a nested for loops with 2 inner loops
        # Line 61 Outer loop runs: O(B), where B is the number of buyers.
        # Line 64 Inner loop runs: O(S).
        # Line 71 Inner loop runs: O(B) where B is the number of buyers
        # Therefore, the runs of this part is B * (B + B).
        # The time complexity is O(B^2)
        # Size of del_list is O(B).
        # Size of matching is O(B).
        # Therefore, the space complexity of this part is O(B).

        # This whole program's complexity
        # Total Time Complexity: O(N^2)
        # Total Space Complexity: O(N^2)

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
    matching = stable_stock_matching(buyers_preferences, stocks_preferences)
    print(matching)


if __name__ == "__main__":
    main()
