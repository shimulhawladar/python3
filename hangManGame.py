from getpass import getpass

print("Welcome to Hang Man Game!")

word = ""
while word == "": word = getpass("Guess a word: ").lower()
word = list(word); word_pop = word.copy()

targeted = []
hint = input("later you want thow show : ").lower()
if hint != "":
    for w in word:
        if hint[0] == w: targeted.append(hint[0]); word_pop.remove(hint[0])
        else: targeted.append("_")
else:
    print("No Hint")
    targeted = list("-"*len(word))

print(" ".join(targeted))

sign = list("HangMan")
gameStaatus = ""

while len(sign) > 0 and gameStaatus != "HangMan" and word_pop != []:
    try:
        char = input("Guess char : ").lower()[0]
        if word.count(char) == 1:
            i = word.index(char) ; targeted[i] = char; word_pop.remove(char)
            print(" ".join(targeted))

        elif word.count(char) > 1:
            for w in enumerate(word):
                if w[1] == char: targeted[w[0]] = char ; word_pop.remove(char)
            print(" ".join(targeted))

        else:
            print("Wrong!")
            gameStaatus += sign.pop(0)
            print(gameStaatus)
    except:
        print("Try Again")


if gameStaatus == "HangMan":
    print(f"Loser..!! {''.join(word).upper()}")
else:
    print("*** Winner ***")


