# Exercise 1:
# You have a football field that is 92 meter long and 48.8 meter wide.
# Find out total area using python and print it.

length_of_football_pitch=92
breadth_of_football_pitch=48.8
total_area=(length_of_football_pitch)*(breadth_of_football_pitch)
print("Total area of football pitch is",round(total_area,1),"meter")

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?

potato_chips_bought= 9
one_packet = 1.49
total_chips_price=potato_chips_bought*one_packet
shopkeeper= 20
money_return= shopkeeper-total_chips_price
print("Shopkeeper is going to give me",money_return,"usd back")

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square

length=5.5
area=length**2
cost=area*500
print("Total cost to replace all the tiles would be",cost,"rs")

# 4. Print binary representation of number 17
num=17
print(f"Binary representation of number {num} is {format(num,'b')}")
