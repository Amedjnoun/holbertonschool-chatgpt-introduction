#!/usr/bin/python3
import random
import os

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
	def __init__(self, width=10, height=10, mines=10):
		self.width = width
		self.height = height
		self.mines = set(random.sample(range(width * height), mines))
		self.field = [[' ' for _ in range(width)] for _ in range(height)]
		self.revealed = [[False for _ in range(width)] for _ in range(height)]
		self.num_mines = mines

	def is_game_won(self):
		# Game is won if all non-mine cells are revealed
		revealed_count = sum(sum(1 for x in row if x) for row in self.revealed)
		return revealed_count == (self.width * self.height - self.num_mines)

	def play(self):
		while True:
			self.print_board()
			try:
				x = int(input("Enter x coordinate: "))
				y = int(input("Enter y coordinate: "))
				if not (0 <= x < self.width and 0 <= y < self.height):
					print("Coordinates out of bounds. Try again.")
					continue
				if not self.reveal(x, y):
					self.print_board(reveal=True)
					print("Game Over! You hit a mine.")
					break
				if self.is_game_won():
					self.print_board(reveal=True)
					print("Congratulations! You've won the game.")
					break
			except ValueError:
				print("Invalid input. Please enter numbers only.")
