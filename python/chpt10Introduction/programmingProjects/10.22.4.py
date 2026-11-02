#Programming Project 10.22.4: ••.
# Write a program that prints the balance of an account after the first, second, and third year. The account has an initial balance of $1,000 and earns 5 percent interest per year.

# Set year to 0, balance to 1000.
year = 0
balance = 1000

# While the balance is less than 20000
while year < 3: # the loop will run until the year is 4
        # Add 1 to the year.
        # year = year + 1
        year += 1
        # set the interest rate to balance x 0.05
        interest = balance * 0.05
        # Add the interest to the balance
        balance = balance + interest
        print("new balance at year ", year, ": ", balance)