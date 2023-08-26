print("IMPLEMENT THE MINMAX ALGORITHM FOR GAMING")
print("B.SHRUTHIKA-192110238")
def minimax(state, depth, is_maximizing):
    if state == 0:
        return -1 if is_maximizing else 1
    if depth == 0:
        return 0
    if is_maximizing:
        max_eval = float("-inf")
        for move in [1, 2]:
            eval = minimax(state - move, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for move in [1, 2]:
            eval = minimax(state - move, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval
def best_move(state):
    best_val = float("-inf")
    best_move = None
    for move in [1, 2]:
        eval = minimax(state - move, 3, False)
        if eval > best_val:
            best_val = eval
            best_move = move
    return best_move
def main():
    starting_number = 10
    while starting_number > 0:
        print(f"Current number: {starting_number}")
        if starting_number == 1:
            print("You win!")
            break
        player_move = int(input("Enter your move (1 or 2): "))
        if player_move < 1 or player_move > 2:
            print("Invalid move. Please enter 1 or 2.")
            continue
        starting_number -= player_move
        if starting_number == 0:
            print("You lose!")
            break
        computer_move = best_move(starting_number)
        print(f"Computer plays: {computer_move}")
        starting_number -= computer_move
if __name__ == "__main__":
    main()
