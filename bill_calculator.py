"""
Bill Calculator Script

This Python script efficiently calculates the number of bills needed to dispense a target amount using available denominations of currency. It provides a clear breakdown for multiple requested amounts, making it useful for various scenarios like cash register management or budgeting calculations.

Features:

Calculates individual bill counts: Determines the optimal number of bills for each denomination (e.g., $100, $50, $20, etc.) to reach the desired amount.
Handles multiple requests: Processes a list of requested amounts, providing a consolidated summary for all.
Descending denomination order: Considers denominations in descending order ($100 first, then $50, and so on) for a more intuitive bill distribution.
Easy to use: Requires minimal setup - just save the script, run it, and provide the requested amounts and available denominations.
How to Use:

Save the script as bill_calculator.py.
Open your terminal or command prompt and navigate to the directory where you saved the script.

"""


def calculate_bill_counts(target_amount, available_denominations):
    """Calculates the number of bills needed for a given target amount with available denominations.

    Args:
        target_amount (int): The target amount of money.
        available_denominations (list[int]): A list of available denominations.

    Returns:
        dict: A dictionary containing the number of bills for each denomination.
    """

    individual_bill_counts = {}
    for denomination in available_denominations:
        if target_amount >= denomination:
            individual_bill_counts[denomination] = target_amount // denomination
            target_amount %= denomination
    return individual_bill_counts


def summarize_bill_counts(requested_amounts, available_denominations):
    """Calculates the total bill counts for multiple requested amounts.

    Args:
        requested_amounts (list[int]): A list of requested amounts.
        available_denominations (list[int]): A list of available denominations.

    Returns:
        list: A list containing three strings summarizing the results.
    """

    individual_calculations = [calculate_bill_counts(amount, available_denominations) for amount in requested_amounts]
    total_bill_counts = {}

    for calculation in individual_calculations:
        for denomination, count in calculation.items():
            if denomination in total_bill_counts:
                total_bill_counts[denomination] += count
            else:
                total_bill_counts[denomination] = count

    requested_text = f"Requested bill amounts: {requested_amounts}"
    total_amount_text = f"Total requested amount: {sum(requested_amounts)}"

    def format_bill_count(key, value):
        return f"${key}: {value}"

    result_text = " | ".join(format_bill_count(key, value) for key, value in sorted(total_bill_counts.items()))

    return [requested_text, total_amount_text, result_text]


if __name__ == "__main__":
    requested_amounts = list(range(7, 23))
    available_denominations = [100, 50, 20, 10, 5, 1]  # $2 bill ignored
    for line in summarize_bill_counts(requested_amounts, available_denominations):
        print(line)