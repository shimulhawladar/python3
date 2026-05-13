import random
from typing import Dict, List, Optional


class MatkaKingGame:
    """
    Matka King Game

    Rules:
    - Randomly pick 3 unique card suits
    - Each card gets a random value between 1 and 10
    - Sum all values
    - Winning digit:
        * If total is 10, 20, 30 -> first digit
        * Otherwise -> last digit
    """

    CARDS = {
        1: "heart",
        2: "diamond",
        3: "club",
        4: "spade",
    }

    def __init__(self, low: int = 1, high: int = 10) -> None:
        self.low = low
        self.high = high

    @staticmethod
    def choose_random(options: Optional[List[int]] = None,
                      low: int = 1,
                      high: int = 10) -> int:
        """
        Return a random value.

        Args:
            options: Optional list to randomly choose from
            low: Minimum integer value
            high: Maximum integer value

        Returns:
            Random integer
        """
        if options:
            return random.choice(options)

        return random.randint(low, high)

    def draw_cards(self) -> Dict[str, int]:
        """
        Draw 3 unique cards with random values.

        Returns:
            Dictionary of card_name -> value
        """
        selected_card_ids = random.sample(list(self.CARDS.keys()), 3)

        return {
            self.CARDS[card_id]: self.choose_random(
                low=self.low,
                high=self.high
            )
            for card_id in selected_card_ids
        }

    @staticmethod
    def calculate_winner(total: int) -> int:
        """
        Calculate winning number from total.

        Args:
            total: Sum of card values

        Returns:
            Winning digit
        """
        if total in (10, 20, 30):
            return int(str(total)[0])

        if total <= 9:
            return total

        return int(str(total)[-1])

    def play(self) -> Dict[str, object]:
        """
        Play one round of the game.

        Returns:
            Game result dictionary
        """
        cards = self.draw_cards()
        total = sum(cards.values())
        winning_number = self.calculate_winner(total)

        return {
            "cards": cards,
            "total": total,
            "winning_number": winning_number,
        }


def get_user_bet() -> int:
    """
    Get validated user bet input.

    Returns:
        User selected number between 0 and 9
    """
    while True:
        try:
            user_input = int(input("Place your bet (0-9): "))

            if 0 <= user_input <= 9:
                return user_input

            print("Please enter a number between 0 and 9.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_result(result: Dict[str, object], user_bet: int) -> None:
    """
    Display formatted game result.

    Args:
        result: Game result dictionary
        user_bet: User selected number
    """
    print("\n========== GAME RESULT ==========")

    cards = result["cards"]

    print("\nPicked Cards:")
    for card_name, value in cards.items():
        print(f"  - {card_name.capitalize():8} : {value}")

    print(f"\nTotal Sum      : {result['total']}")
    print(f"Winning Number : {result['winning_number']}")

    if user_bet == result["winning_number"]:
        print("\n🎉 Congratulations! You won!")
    else:
        print("\n❌ Better luck next time!")

    print("=================================\n")


def main() -> None:
    """
    Main application entry point.
    """
    print("=================================")
    print("     Welcome to Matka King")
    print("=================================")

    user_bet = get_user_bet()

    game = MatkaKingGame()
    result = game.play()

    display_result(result, user_bet)


if __name__ == "__main__":
    main()