def create_sandwich(*ingredients):
    print("You've ordered a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
create_sandwich("Lettuce", "Tomato", "Turkey", "Cheese")
print()  # Just for spacing
create_sandwich("Ham", "Mustard")
