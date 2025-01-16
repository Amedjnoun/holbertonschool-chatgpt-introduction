class Checkbook:
	def __init__(self):
		self.balance = 0.0

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError("Amount must be positive")
		self.balance += amount
		print("Deposited ${:.2f}".format(amount))
		print("Current Balance: ${:.2f}".format(self.balance))

	def withdraw(self, amount):
		if amount <= 0:
			raise ValueError("Amount must be positive")
		if amount > self.balance:
			print("Insufficient funds to complete the withdrawal.")
		else:
			self.balance -= amount
			print("Withdrew ${:.2f}".format(amount))
			print("Current Balance: ${:.2f}".format(self.balance))

	def get_balance(self):
		print("Current Balance: ${:.2f}".format(self.balance))

def main():
	cb = Checkbook()
	while True:
		try:
			action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
			if action.lower() == 'exit':
				break
			elif action.lower() == 'deposit':
				try:
					amount = float(input("Enter the amount to deposit: $"))
					cb.deposit(amount)
				except ValueError as e:
					print("Invalid amount. Please enter a valid positive number.")
			elif action.lower() == 'withdraw':
				try:
					amount = float(input("Enter the amount to withdraw: $"))
					cb.withdraw(amount)
				except ValueError as e:
					print("Invalid amount. Please enter a valid positive number.")
			elif action.lower() == 'balance':
				cb.get_balance()
			else:
				print("Invalid command. Please try again.")
		except KeyboardInterrupt:
			print("\nExiting program...")
			break

if __name__ == "__main__":
	main()
