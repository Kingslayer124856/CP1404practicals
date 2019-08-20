total = 0
number = int(input("Number of items: "))
while number <= 0:
    print("You have no Items")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Item Price: "))
    # float not int for decimal places or when
    # decimals are used it will break
    total += price
if total > 100:
    total *= 0.9
# (*= 0.9) was used as a basicly a representaion of making the total
# become a pecentage of the total, so we wanted 10% off,
# so if total = 1 then discounted price would be 0.9 of the total
print("Total price for {} items is ${:.2f}".format(number, total))
# {:.2f} brings the intiger to a two decimal places instead of a
# long string of numbers


