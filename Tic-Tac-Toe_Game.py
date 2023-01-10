import numpy as num
import colorama as color
from colorama import Fore,Back,Style
color.init()



blocks = {str(key + 1): str(value) for key,value in enumerate(range(1,10))}
cPoint = [[0,1,2],[3,4,5],[6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
rounds = 0
loop = []
mark= {0:[0]*9,1:[0]*9}
winner = ""


def result(player,pInput,blocks):
    for each in blocks:
        if sum(pInput[each]) == 3:
            globals()['winner'] = player
            return True
    return False

def box():
    box = f"""
     {blocks['1']} | {blocks['2']} | {blocks['3']} 
    -----------
     {blocks['4']} | {blocks['5']} | {blocks['6']} 
    -----------
     {blocks['7']} | {blocks['8']} | {blocks['9']}
    """
    return box

def players(x):
    if x % 2 == 0:
        return "X"
    return "@"

while rounds < 9:
    print(Fore.LIGHTWHITE_EX+box())

    for player in mark:
        if result(player, num.array(mark[player]), cPoint) == True:
            print(f"{Fore.LIGHTGREEN_EX}Winner: Player One" if winner == 0 else "Winner: Player Tow")
            rounds = 10
            break

    if rounds >=9: break

    play = Fore.GREEN+"| Player One |" if players(rounds) == "X" else Fore.GREEN+"| Player Tow |"
    inp = input(f"{play} {Fore.YELLOW}Enter Block Number: ")
    if (inp[0] > '0' and inp[0] <='9') and inp[0] not in loop:
        loop.append(inp[0])
        blocks[inp[0]] = players(rounds)
        mark[rounds % 2][int(inp)-1] = 1
        rounds += 1
    else:
        print(f"{Fore.RED}!!!!!>>>>>>> Wrong Entry <<<<<<<!!!!!")
        continue

print(box())
if winner == "":print(f"{Fore.LIGHTCYAN_EX}DRAW!")



