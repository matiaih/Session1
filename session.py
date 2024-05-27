# Write a program to input age of a user and let them know if they have diabetes risk or not. Use case is that a user with more than 65 is risky else not risky.
age = 55
if age >= 65
print("This is Risky")
else 
print("Not Risky")

# Write a program to calculate the GST tax of two products, apple and pie
# Apple has 10% GST and pie has 8%
# Calculate total GST that need to be deducted from the bill
# Apple gross sale is $75, pie gross is $100

apple_gross = 75
pie_gross = 100
total_gst = (apple_gross/100*10) + (pie_gross/100*8)
print(total_gst)
