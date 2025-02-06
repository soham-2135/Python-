# After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
total=0

for i in result:
    if i == "heads": # The in(if i in result==0) operator is used to check if an element exists in a list
        total=total+1
print("No of times we got head is",total)
#
# #2)Print square of all numbers between 1 to 10 except even numbers
print("Square of all numbers from 1-10 excluding even numbers are below:")
for i in range(11):
    if i%2 == 0:
        continue
    print(i,":",i*i)
#
# # 3. Your monthly expense list (from Jan to May) looks like this,
# # expense_list = [2340, 2500, 2100, 3100, 2980]
# # Write a program that asks you to enter an expense amount
# # and program should tell you in which month that expense occurred.
# # If expense is not found then it should print that as well.
month=["January","February","March","April","May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
expense=int(input("Enter the expenses:"))
available = False

for i in range(len(expense_list)):
    if expense == expense_list[i] :
        print(f"You spent {expense_list[i]} in {month[i]}")
        available = True
        break

if not available:
        print(f"You didnt spend {expense} in any month")

#4) Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

for i in range(1,6):
    print(f"you ran {i}km")
    tired = input("Are you tired ?")
    if i == 5:
        break
    if tired == "yes" or tired == "Yes":
        print("You didnt finish the race")
        break
    elif tired == "no" or tired == "No":
        continue
if i == 5:
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print(f"You didn't finish 5 km race but hey congrats anyways! You still ran {i} km")

#modified version of the above program:
for i in range(1,6):
    print(f"you ran {i}km")
    tired = input("Are you tired ?")
    if i ==5:
        break
    if tired == "yes" or tired == "Yes":
        print("You didnt finish the race")
        break
    while True:
        if tired == "no" or tired == "No":
            break
        else:
            print("Enter between yes/no:")
            tired = input("Are you tired? ")
if i == 5:
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print(f"You didn't finish 5 km race but hey congrats anyways! You still ran {i} km")




# 5) #Soham's creativity => You are running a 5 km race, and after completing each kilometer,
# you are asked whether you're tired and if you want to continue running.
# After completing each 1 km, the program should ask, "Are you tired?"
# If you reply "yes," the program should encourage you with a motivational message:
# "C'mon, you got this in you, don't quit, just push for it!" and continue to the next kilometer.
# If you reply "no," the program should praise you with the message:
# "That's what I expected from you" and continue to the next kilometer.
# If you finish all 5 kilometers without quitting, the program should print:
# "Doesn't matter, you finished the race."

for i in range (1,6):
    print(f"You ran {i}km:")
    if i == 5:
      break

    while True:
        tired = input("Are you tired ?")
        if tired =="yes" or tired == "Yes":
            print("C'mon you got this into you,dont quit just push for it")
            break
        elif tired == "no" or tired == "No":
            print("That's what i expected from you")
            break
        else:
            print("Enter between yes/no")
tired = input("Are you tired ?")
print("Doesnt matter,you finished the race")

# 6) Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```

for i in range(1,6):
    s = ''             # s='' specifies it is a string
    for j in range(i): # range cant be (1,6)
        s += '*'       # += concatenates, it does not add '*' as it is string
    print(s)
