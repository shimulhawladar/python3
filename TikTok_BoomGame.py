import getpass
from typing import List


def styled_message(message: str, style: str = "info") -> str:
    """Return a formatted message with a decorative border."""
    styles = {"warning": "-", "boom": "*", "header": "=", "footer": "_"}
    symbol = styles.get(style, "/")
    line_length = 70 - len(message) // 2
    return f"|| {symbol * line_length} {message} {symbol * line_length} ||"


def get_player_numbers() -> List[str]:
    """Securely get valid 3-digit numbers for both players."""
    players = []
    for turn in ("First Player", "Second Player"):
        while True:
            print(styled_message(turn, "header"))
            secret = getpass.getpass("Enter exactly 3 unique digits (1–9, no 0): ")

            # Validation
            if not (secret.isdigit() and len(secret) == 3):
                print("❌ Invalid — must be exactly 3 digits.")
                continue
            if "0" in secret:
                print("🚫 Number cannot contain 0.")
                continue
            if len(set(secret)) != 3:
                print("🚫 Digits must be unique.")
                continue

            players.append(secret)
            break
    return players


class Player:
    """Represents a player in the Boom game."""

    def __init__(self, name: str, boom_code: str):
        self.name = name
        self.boom_code = boom_code
        self.room = "123456789"
        self.life = 3
        self.entries: List[str] = []

    def __str__(self) -> str:
        return f"{self.name} | Life: {'♡' * self.life} | Room: {self.room}"


def play_game(player1_code: str, player2_code: str) -> None:
    """Run the main Boom game loop."""
    players = [
        Player("Player One", player2_code),
        Player("Player Two", player1_code),
    ]

    turn = 0
    print(styled_message("Game Start!", "footer"))

    while True:
        current = players[turn]
        print(styled_message(current.name, "header"))

        guess = input("→ Choose a number (1–9, no 0): ").strip()

        # Input validation
        if not guess.isdigit() or guess == "0" or not (1 <= int(guess) <= 9):
            print("❌ Invalid input — please enter a number between 1 and 9 (no 0).")
            continue
        if guess in current.entries:
            print("⚠️ Duplicate entry — try a new number.")
            continue

        current.entries.append(guess)

        # Check hit/miss
        if guess in current.boom_code:
            print(styled_message("💥 BOOM!", "boom"))
            current.life -= 1
            current.room = current.room.replace(guess, "*")
        else:
            current.room = current.room.replace(guess, "-")

        print(styled_message(str(current), "footer"))

        # Check lose condition
        if current.life <= 0:
            print(styled_message(f"💀 {current.name} loses!", "warning"))
            break

        # Check win condition (when 6 or more rooms are cleared)
        if current.room.count("-") >= 6:
            print(styled_message(f"🏆 {current.name} wins!", "header"))
            break

        # Switch turns
        turn = 1 - turn
        print("\n" + styled_message("Next Turn", "footer") + "\n")

    print(styled_message("Game Over", "boom"))


if __name__ == "__main__":
    codes = get_player_numbers()
    play_game(codes[0], codes[1])
