from attr.setters import convert

user_favorite_fruit = input("What is your favorite fruit?")

if user_favorite_fruit == "banana":
    print("Banana is awsome!")
elif user_favorite_fruit == "strawberry":
    print("Strawberry for the win!")
else:
    print("Interesting choice!")

users_number = input("Give me a number")
number = int(users_number)
if number % 2 == 0:
    print("That's even.")
else:
    print("that's odd.")
print("Thanks for playing!")
