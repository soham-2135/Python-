# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

month=["January","February","March","April","May"]
expense=[2200,2350,2600,2130,2190]

for i in range(len(month)):
    print(month[i],"-",expense[i])
# 1)
difference= expense[1]-expense[0]
print(f"\nIn Feb, total dollars spent extra compared to January is {difference}")

#2)
total=0
for i in range(3):
    total=total+expense[i]
print(f"\nTotal expense in first quarter (first three months) of the year is {total}")

#3)
found= False # t check if 2000 exist, if didnt statement outside loop will be executed
for i in range(len(month)):
    if expense[i]==2000: # if yes, found becomes true, and not found=not false=true and print will only execute if not found = true,i.e found=false so if there's 2000 in the list below print statement will be skipped
        print("\n")
        print(month[i], "-", expense[i],",In this month money spent is exactly 2000 dollars")
        found=True
        break

if not found: # or you can use if found==false, but both become very different, if "if not found" is used at that time print will only execute if found=true
 print("\nDidnt find any month where total money spent is exactly 2000 dollars")

#4)
month.append("June")
expense.append(1980)
print("\n")
print(month)
print(expense)

#5)
expense[3]=expense[3]-200
print("\n", expense)

# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
#
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# Solution
#1)
print("\n")
heros=['spider man','thor','hulk','iron man','captain america']
print(f"the length of the list is {len(heros)}")

#2)
heros.append("black panther")
print(f"\nThe updated list is:{heros}")

#3)
heros.remove("black panther")
heros.insert(2,"black panther")
print(f"\nThe newly updated list is{heros}")

#4)cant be done in one line as black panther comes in between the both, for previous list heros[1:3]="doctor strange", for previous list it was feasible to do it in one line
heros.remove("thor")
heros[2]="doctor strange"
print(f"\nI don't like thor and hulk because they get angry easily, so im replacing them with {heros[2]} because he is just a cool guy")
print("\n")
print(heros)

#5)
heros.sort()
print("\n")
print(heros)
