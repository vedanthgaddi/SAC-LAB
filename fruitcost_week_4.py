fruit_type = input("Enter the fruit type: ").strip().title()
'''.strip().title() on input to make input case-insensetive and trim spaces'''
if fruit_type == "Oranges":
    print("Oranges are 50rs per kilogram")
elif fruit_type == "Apples":
    print("Apples are 120rs per kilogram")
elif fruit_type == "Bananas":
    print("Bananas are 40rs per dozen")
elif fruit_type == "Cherries":
    print("Cherries are 600rs per kilogram")
else:
    print(f"Sorry, we are out of {fruit_type}")
