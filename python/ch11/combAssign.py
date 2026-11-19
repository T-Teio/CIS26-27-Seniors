##
# Section 11.4 Practice: Combining Assignment and Arithmetic


#basic idea -------------------------
total = 10
cans = 4
total += cans
print("total += cans -->", total)

total *= 2
print("total *= 2 -->", total)

# ---- Count by one -------------------------
count = 0
count += 1
count += 1
count += 1
count += 1
count += 1
count += 1
print("count =", count)

#------ realistic use: a running total (shopping cart) -------------------------
cartTotal = 0.0
cartTotal += 3.49
cartTotal += 12.99
cartTotal += 1.25
print("Your cart total today is: $", cartTotal)