"""Componet 1 (How much) v3
More efficient method - includes valid range as the basis of the while loop
while eliminates the need to use the 'valid' variable"""

# Main routine
error = "That was not balid input\n"
user_balance = 0

# Keep asking until a valid amount (1-10) is entered
while not 1 <= user_balance <= 10:
    try:
        # ask for amount
        user_balance = int(input("Please enter a whole number betwwen 1 and 10"
                                 "\nHow much do you want to play with? $"))
        print()

    except ValueError:
        print(error)

print(f"You are playing with ${user_balance}")
