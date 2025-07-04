import math

# The board
board = [" "] * 9

# Print the board
def show():
    print(f"""
 {board[0]} | {board[1]} | {board[2]} 
---+---+---
 {board[3]} | {board[4]} | {board[5]} 
---+---+---
 {board[6]} | {board[7]} | {board[8]} 
""")

# Check winner
def check_winner():
    wins = [
        [0,1,2],[3,4,5],[6,7,8], # rows
        [0,3,6],[1,4,7],[2,5,8], # cols
        [0,4,8],[2,4,6]          # diagonals
    ]
    for line in wins:
        if board[line[0]] == board[line[1]] == board[line[2]] != " ":
            return board[line[0]]
    return None

# Get empty spots
def empty():
    return [i for i in range(9) if board[i] == " "]

# Minimax
def minimax(is_ai):
    win = check_winner()
    if win == "O": return 1
    if win == "X": return -1
    if not empty(): return 0

    if is_ai:
        best = -math.inf
        for i in empty():
            board[i] = "O"
            best = max(best, minimax(False))
            board[i] = " "
        return best
    else:
        best = math.inf
        for i in empty():
            board[i] = "X"
            best = min(best, minimax(True))
            board[i] = " "
        return best

# AI move
def ai():
    best = -math.inf
    move = -1
    for i in empty():
        board[i] = "O"
        score = minimax(False)
        board[i] = " "
        if score > best:
            best = score
            move = i
    board[move] = "O"

# Main game
def play():
    print("Tic-Tac-Toe: You are X, AI is O")
    show()

    while True:
        # Player move
        try:
            pos = int(input("Your move (0-8): "))
            if pos not in empty():
                print("Invalid. Try again.")
                continue
            board[pos] = "X"
        except:
            print("Enter a number 0-8.")
            continue

        show()
        if check_winner() == "X":
            print("You win! 🎉")
            break
        if not empty():
            print("Draw!")
            break

        # AI move
        print("AI's move:")
        ai()
        show()
        if check_winner() == "O":
            print("AI wins! 🤖")
            break
        if not empty():
            print("Draw!")
            break

if __name__ == "__main__":
    play()
