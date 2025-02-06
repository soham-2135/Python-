# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#i)
city=input("Enter the name of city:")

if city in india:
    print(f"{city} belongs in india")
elif city in pakistan:
    print(f"{city} belongs in pakistan")
elif city in bangladesh:
    print(f"{city} belongs in bangladesh")
else:
    print("enter the valid city ")

#ii)
city=input("Enter the name of city:")
City=input("Enter the name of city:")

if city in india and City in india:
    print(f"{city} and {City} are located in india")
elif city in pakistan and City in pakistan:
    print(f"{city} and {City} are located in pakistan")
elif city in bangladesh and City in bangladesh:
    print(f"{city} and {City} are located in bangladesh")
else:
    if  (city in india or city in pakistan or city in bangladesh) and \
        (City in india or City in pakistan or City in bangladesh):
             print(f"{city} and {City} don't belong to same country ")
    else:
        print(f"At least one of the cities is not in the list")


#2)
# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

sugar_level=int(input("Enter your fasting sugar level:"))

if sugar_level < 80:
    print("Sugar level is low")
elif sugar_level > 100:
    print("Sugar level is high")
elif 80 <= sugar_level <= 100:               #can directly use else statement as well, cuz condition is already met
    print("Sugar level is normal")
