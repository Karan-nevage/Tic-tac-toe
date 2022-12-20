# TIC TAC TOE IN PYTHON WITHOUT USING ANY MODULE
# python LANGUAGE PROJECT 
# https://github.com/tueuer/Tic-tac-toe
# https://github.com/tueuer
# AUTHOR:-Karankumar Nevage 



def sum(x, y, z ):
    return x + y + z



def print_tic_tac_toe_box(stateA, stateB):

    zero = 'X' if stateA[0] else ('O' if stateB[0] else 0)
    one  = 'X' if stateA[1] else ('O' if stateB[1] else 1)
    two  = 'X' if stateA[2] else ('O' if stateB[2] else 2)
    three= 'X' if stateA[3] else ('O' if stateB[3] else 3)
    four = 'X' if stateA[4] else ('O' if stateB[4] else 4)
    five = 'X' if stateA[5] else ('O' if stateB[5] else 5)
    six  = 'X' if stateA[6] else ('O' if stateB[6] else 6)
    seven= 'X' if stateA[7] else ('O' if stateB[7] else 7)
    eight= 'X' if stateA[8] else ('O' if stateB[8] else 8)

# printing in mesh form
    print(f"{zero} | {one} | {two} ")
    print(f"==|===|===")
    print(f"{three} | {four} | {five} ")
    print(f"==|===|===")
    print(f"{six} | {seven} | {eight} ") 

# defining wins conditions
def checkWin(stateA, stateB):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if(sum(stateA[win[0]], stateA[win[1]], stateA[win[2]]) == 3):
            print("Player 1 Won the match")
            return 1

        if(sum(stateB[win[0]], stateB[win[1]], stateB[win[2]]) == 3):
            print("Player 2 Won the match")
            return 0

    return -1


# main   
if __name__ == "__main__":

    stateA = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    stateB = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 
    print("------Tic Tac Toe------")
    print("Player 1: X")
    print("Player 2: O")
    while(True):

        print_tic_tac_toe_box(stateA, stateB)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            stateA[value] = 1

        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            stateB[value] = 1
        cwin = checkWin(stateA, stateB)


        if(cwin != -1):
            print("CONGRATULATION")
            print("    (❁´◡`❁)")
            print("==>Match over<==")

            break
        
        turn = 1 - turn