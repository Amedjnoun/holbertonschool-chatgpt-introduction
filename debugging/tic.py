#!/usr/bin/python3

def print_board(board):
	print("\n")
	for i, row in enumerate(board):
		print(" | ".join(row))
		if i < 2:  # Don't print line after last row
			print("-" * 9)

def check_winner(board):
	# Check rows
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True

	# Check columns
	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return True

	# Check diagonals
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return True
	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return True

	return False

def is_board_full(board):
	return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
	board = [[" "]*3 for _ in range(3)]
	current_player = "X"

	while True:
		print_board(board)
		print(f"Player {current_player}'s turn")

		try:
			row = int(input("Enter row (0, 1, or 2): "))
			col = int(input("Enter column (0, 1, or 2): "))

			if not (0 <= row <= 2 and 0 <= col <= 2):
				print("Invalid input! Row and column must be between 0 and 2.")
				continue

			if board[row][col] != " ":
				print("That spot is already taken! Try again.")
				continue

			board[row][col] = current_player

			if check_winner(board):
				print_board(board)
				print(f"Player {current_player} wins!")
				break

			if is_board_full(board):
				print_board(board)
				print("It's a tie!")
				break

			current_player = "O" if current_player == "X" else "X"

		except ValueError:
			print("Invalid input! Please enter numbers only.")
		except KeyboardInterrupt:
			print("\nGame aborted!")
			break

if __name__ == "__main__":
	tic_tac_toe()
