print("Hi there, welcome to the shopping list")

shopping_list = {}
status = input("Type 'NEW' for new Shopping List or Type 'ADD' to add items to the existing Shopping List: ").strip().lower()

while True:
    item_to_buy = input("What are you planning to buy? Enter an Item name or type 'done' to finish."
                        "\nProduct: ")
    if item_to_buy.strip().lower() == "done":
        break

    if item_to_buy in shopping_list:
        print(f"\nYou already have {item_to_buy.upper()} on the list. Actual amount: {shopping_list[item_to_buy.lower()]}\n")
        adjust = input("Adjust the quantity? (yes/no): ").strip().lower()

        if adjust in ("yes", "y"):
            quantity = input("Enter new quantity: ")
            shopping_list[item_to_buy] = quantity.upper()

    else:
        quantity = input("How many items do you want? Qs: ")
        shopping_list[item_to_buy.lower()] = quantity.upper()

if status == "new":
    mode = "w"
elif status == "add":
    mode = "a"
else:
    print("Invalid option chosen. New Shopping List will be created.")
    mode = "w"


with open("Data/shopping_list.txt", mode) as file:
    if mode == "w":
        file.write("SHOPPING LIST:\n\n")
    for i, (product, quantity) in enumerate(shopping_list.items(), start=1):
        print(f"{i}. {product.capitalize()}: {quantity}")
        file.write(f"{i}. {product}: {quantity}\n")

# import pywhatkit as kit
#
# try:
#     with open("Data/shopping_list.txt", "r") as file:
#         message = file.read()
#     kit.sendwhatmsg_instantly("+421951717455", message, wait_time=10, tab_close=True)
# except FileNotFoundError:
#     print("Sorry, something went wrong. Try again later.")




