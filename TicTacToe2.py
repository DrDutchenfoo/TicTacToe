import random
plist = []
clist = []

print("   1   │   2   │   3 ")
print("───────────────────────")
print("   4   │   5   │   6 ")
print("───────────────────────")
print("   7   │   8   │   9 ")

while True:
    tiles = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    win = 0
    pscore = 0
    cscore = 0
    for item in plist:
        pscore = pscore + 1
    for ite in clist:
        cscore = cscore + 1
    print(f'''
Here are the scores! 
You: {str(pscore)} 
Computer: {str(cscore)}
''')
    while True:
        p = 1
        c = 1

        while p == 1:
            pchoice = input("Choose a tile: ")
            if tiles[int(pchoice) - 1] == " ":
                tiles[int(pchoice) - 1] = "X"
                p = 0
            else:
                print("Invalid, try again")

        if " " in tiles:
            c = 1
        else:
            c = 0
            win = 3
        while c == 1:
            cchoice = random.randrange(1, 9)
            if tiles[int(cchoice) - 1] == " ":
                tiles[int(cchoice) - 1] = "O"
                print(f"The computer chose: {str(cchoice)}")
                c = 0

        print(f"   {tiles[0]}   │   {tiles[1]}   │   {tiles[2]}")
        print("───────────────────────")
        print(f"   {tiles[3]}   │   {tiles[4]}   │   {tiles[5]}")
        print("───────────────────────")
        print(f"   {tiles[6]}   │   {tiles[7]}   │   {tiles[8]}")

        if tiles[0] == tiles[1] == tiles[2] == "O":
            win = 2
        elif tiles[3] == tiles[4] == tiles[5] == "O":
            win = 2
        elif tiles[6] == tiles[7] == tiles[8] == "O":
            win = 2
        elif tiles[0] == tiles[3] == tiles[6] == "O":
            win = 2
        elif tiles[1] == tiles[4] == tiles[7] == "O":
            win = 2
        elif tiles[2] == tiles[5] == tiles[8] == "O":
            win = 2
        elif tiles[0] == tiles[4] == tiles[8] == "O":
            win = 2
        elif tiles[2] == tiles[4] == tiles[6] == "O":
            win = 2

        if tiles[0] == tiles[1] == tiles[2] == "X":
            win = 1
        elif tiles[3] == tiles[4] == tiles[5] == "X":
            win = 1
        elif tiles[6] == tiles[7] == tiles[8] == "X":
            win = 1
        elif tiles[0] == tiles[3] == tiles[6] == "X":
            win = 1
        elif tiles[1] == tiles[4] == tiles[7] == "X":
            win = 1
        elif tiles[2] == tiles[5] == tiles[8] == "X":
            win = 1
        elif tiles[0] == tiles[4] == tiles[8] == "X":
            win = 1
        elif tiles[2] == tiles[4] == tiles[6] == "X":
            win = 1

        if win == 1:
            print(" * YOU WIN * ")
            plist.append("E")
            break
        elif win == 2:
            print(" * YOU LOOSE * ")
            clist.append("E")
            break
        elif win == 3:
            print(" * CATS GAME * ")
            break
