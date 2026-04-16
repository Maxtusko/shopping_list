import os

print("Hi there, welcome to the shopping list\n")
file_path = "Data/shopping_list.txt"

# Check ifa the directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

print("You have following items saved in your list:")

# Load existing items from file (normalized to lowercase for comparison)
if os.path.isfile(file_path):
    with open(file_path, "r") as file:
        existing_items = {line.strip().lower() for line in file if line.strip()}


def parse_line(line: str):
    clean = line.strip()
    # Remove numbering like "1. " or "2. "
    if ". " in clean:
        clean = clean.split(". ", 1)[1]
    # Split into product + quantity
    if ":" in clean:
        product, quantity = clean.split(":", 1)
        return product.strip(), quantity.strip()
    return None, None

shopping_list = {}

# Print items for the user
if existing_items:
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())
    print("\n")
else:
    print("Your list is currently empty")

status = input(
    "Type 'NEW' for new Shopping List or Type 'ADD' to add items to the existing Shopping List: ").strip().lower()

while True:
    item_to_buy = input("What are you planning to buy? Enter an Item name or type 'done' to finish.\nProduct: ")
    if item_to_buy.strip().lower() == "done":
        break

    for line in existing_items:
        product, quantity = parse_line(line)
        if item_to_buy == product:
            print(f"\nYou already have {item_to_buy.upper()} on the list. Actual amount: {quantity}\n")
            # print(item_to_buy)
            adjust = input(f"Adjust the quantity for {item_to_buy.upper()}? (yes/no): ").strip().lower()
            if adjust in ("yes", "y"):
                quantity = input("Enter new quantity: ")
                shopping_list[item_to_buy.lower()] = quantity.upper()
            break

    quantity = input("How many items do you want? Qs: ")
    shopping_list[item_to_buy.lower()] = quantity.upper()

if status == "new":
    mode = "w"
elif status == "add":
    mode = "a"
else:
    print("Invalid option chosen. New Shopping List will be created.")
    mode = "w"

if status == "new":
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("**********SAVED SHOPPING LIST ITEMS**********\n")
        for i, (product, quantity) in enumerate(shopping_list.items(), start=1):
            print(f"{i}. {product.capitalize()}: {quantity}")
            file.write(f"{i}. {product}: {quantity}\n")
elif status == "add":
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("+++++ADDED ITEMS+++++\n")
        for i, (product, quantity) in enumerate(shopping_list.items(), start=1):
            print(f"{i}. {product.capitalize()}: {quantity}")
            file.write(f"{i}. {product}: {quantity}\n")
else:
    print("Invalid option chosen. New Shopping List will be created.")


# Print items for the user
with open(file_path, "r") as file:
    for line in file:
        print(line.strip())
print()

# Send a shopping list to WhatsApp
# import pywhatkit as kit
#
# try:
#     with open(file_path, "r") as file:
#         message = file.read()
#     kit.sendwhatmsg_instantly("+421951717455", message, wait_time=10, tab_close=True)
# except FileNotFoundError:
#     print("Sorry, something went wrong. Try again later.")
